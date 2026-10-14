"""Repository Investigator: a transparent context planner for AI-assisted research.

The program accepts any local GitHub repository and a natural-language question.
It does not pretend to answer the question itself. Instead, it builds an evidence
bundle that tells a human or AI agent what to inspect first and why.
"""

import argparse # reads questions and options typed in the terminal
import json
import re # finds words and creates safe filenames
from datetime import datetime
from pathlib import Path # handles files and folders safely.

# These folders usually contain dependencies, generated output, or cache files, so js ignore
IGNORED_DIRECTORIES = {".git", "node_modules", "dist", "build", ".venv", "__pycache__"}

# These are the file types most useful for software investigation.
SOURCE_EXTENSIONS = {".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java"} # implementation logic
DOCUMENT_EXTENSIONS = {".md", ".txt", ".rst"} # to explain the project
CONFIG_EXTENSIONS = {".json", ".toml", ".yaml", ".yml", ".ini"} # files to configure the project (how to run and behave)
SUPPORTED_EXTENSIONS = SOURCE_EXTENSIONS | DOCUMENT_EXTENSIONS | CONFIG_EXTENSIONS # rhe union 

# Generic words add little value when matching a question to a file.
STOPWORDS = {
    "the", "and", "for", "with", "from", "this", "that", "what", "how",
    "does", "does", "into", "use", "using", "show", "explain", "find",
}

# Each role receives a distinct investigation goal and vocabulary.
ROLES = {
    "explore": {
        "goal": "Trace implementation, agents, tools, commands, and permissions.",
        "keywords": {"agent", "tool", "command", "permission", "workflow", "execute"},
    },
    "scout": {
        "goal": "Compare documentation and configuration with the implementation.",
        "keywords": {"readme", "doc", "config", "package", "manifest", "setup"},
    },
    "review": {
        "goal": "Inspect tests, integrations, APIs, and supporting modules.",
        "keywords": {"test", "integration", "api", "client", "server", "session"},
    },
}


# Convert text into unique lowercase keywords.
def tokens(text: str) -> set[str]:
    # Find words containing at least three letters, numbers, underscores, or hyphens.
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", text.lower())
    # Start with an empty set so repeated words appear only once.
    useful_words = set()
    # Examine each word found in the input.
    for word in words:
        # Keep the word only if it is not generic filler.
        if word not in STOPWORDS:
            useful_words.add(word)
    # Return the final set of meaningful words.
    return useful_words


# Find files that could contain useful technical evidence.
def discover(repository: Path) -> list[Path]:
    # Start an empty list for files that pass our filters.
    files = []
    # Walk through the repository and every nested directory.
    for path in repository.rglob("*"):
        # Ignore folders because only files contain evidence we can read.
        if not path.is_file():
            continue
        # Ignore unsupported files such as images, binaries, and lock databases.
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        # Ignore dependencies and generated directories to reduce noise.
        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue
        # Keep this file as a candidate for investigation.
        files.append(path)
    # Return every candidate file.
    return files


# Read a file safely and return a limited amount of content.
def read_preview(path: Path, characters: int = 16000) -> str:
    # Try to read text while ignoring unusual bytes.
    try:
        return path.read_text(errors="ignore")[:characters]
    # If a file cannot be read, return empty text instead of crashing the scan.
    except OSError:
        return ""


# Extract simple import statements as dependency clues.
def imports_from(content: str) -> list[str]:
    # Keep only common Python, JavaScript, and TypeScript import lines.
    lines = [line.strip() for line in content.splitlines()]
    imports = [line for line in lines if line.startswith(("import ", "from ", "require("))]
    # Limit the preview so one large file does not dominate the report.
    return imports[:10]


# Score one file against the user's question and explain the score.
def inspect_file(path: Path, repository: Path, question: str) -> dict:
    # Read a bounded preview to keep the scan predictable.
    content = read_preview(path)
    # Convert the question into meaningful keywords.
    question_words = tokens(question)
    # Search both the path and content because filenames often communicate purpose.
    file_words = tokens(str(path) + " " + content)
    # Find the words shared by the question and this file.
    matches = sorted(question_words & file_words)
    # Give documentation and configuration files a small evidence bonus.
    type_bonus = 1 if path.suffix.lower() in DOCUMENT_EXTENSIONS | CONFIG_EXTENSIONS else 0
    # Calculate a simple, explainable relevance score.
    score = len(matches) + type_bonus
    # Return evidence that can be inspected by a human.
    return {
        "path": str(path.relative_to(repository)),
        "score": score,
        "matches": matches,
        "reason": f"matched: {', '.join(matches)}" if matches else "type bonus only",
        "bytes": path.stat().st_size,
        "estimated_tokens": max(1, len(content) // 4),
        "imports": imports_from(content),
        "preview": " ".join(content.split())[:240],
    }


# Select the strongest evidence files for the question.
def rank_files(repository: Path, question: str, limit: int) -> list[dict]:
    # Discover all possible files first.
    candidates = discover(repository)
    # Inspect every candidate and calculate its evidence score.
    inspected = [inspect_file(path, repository, question) for path in candidates]
    # Remove files with no connection to the question.
    relevant = [item for item in inspected if item["score"] > 0]
    # Sort by score and then alphabetically for stable, repeatable results.
    relevant.sort(key=lambda item: (-item["score"], item["path"]))
    # Return only the context budget requested by the user.
    return relevant[:limit]


# Assign each selected file to exactly one focused role.
def assign_roles(files: list[dict], budget: int) -> dict:
    # Create an empty task list for every role.
    tasks = {
        role: {"goal": details["goal"], "files": []}
        for role, details in ROLES.items()
    }
    # Consider each selected file once, preventing duplicate assignment.
    for item in files:
        # Convert the path into words for role matching.
        path_words = tokens(item["path"])
        # Start with Review as the fallback role.
        chosen_role = "review"
        best_match_count = 0
        # Compare the path with every role's vocabulary.
        for role, details in ROLES.items():
            match_count = len(path_words & details["keywords"])
            # Keep the role with the strongest path-level evidence.
            if match_count > best_match_count:
                chosen_role = role
                best_match_count = match_count
        # Respect each role's context budget.
        if len(tasks[chosen_role]["files"]) < budget:
            tasks[chosen_role]["files"].append(item)
    # Return the focused, non-overlapping task plan.
    return tasks


# Build a complete evidence bundle for one user question.
def build_bundle(repository: Path, question: str, limit: int, budget: int) -> dict:
    # Discover the whole candidate set for comparison metrics.
    candidates = discover(repository)
    # Select and rank only the most relevant evidence.
    selected = rank_files(repository, question, limit)
    # Estimate how much context a broad scan would expose.
    broad_tokens = sum(max(1, path.stat().st_size // 4) for path in candidates)
    # Estimate how much context the focused plan exposes.
    focused_tokens = sum(item["estimated_tokens"] for item in selected)
    # Return the complete result for JSON and Markdown output.
    return {
        "question": question,
        "repository": str(repository),
        "repository_summary": {
            "candidate_files": len(candidates),
            "selected_files": len(selected),
            "broad_estimated_tokens": broad_tokens,
            "focused_estimated_tokens": focused_tokens,
            "estimated_token_reduction_percent": round(
                100 * (1 - focused_tokens / max(1, broad_tokens)), 1
            ),
        },
        "selected_evidence": selected,
        "roles": assign_roles(selected, budget),
        "next_action": "Give each role its assigned evidence, collect findings, and compare overlap.",
    }


# Turn the evidence bundle into a report a person can read.
def write_report(bundle: dict, output_path: Path) -> None:
    # Read the summary once so the report stays easy to compose.
    summary = bundle["repository_summary"]
    # Start the report with the question and measurable context comparison.
    lines = [
        "# Repository Investigation Report", "",
        f"**Question:** {bundle['question']}", "",
        "## Context comparison", "",
        f"- Candidate files: {summary['candidate_files']}",
        f"- Focused files: {summary['selected_files']}",
        f"- Broad estimate: {summary['broad_estimated_tokens']} tokens",
        f"- Focused estimate: {summary['focused_estimated_tokens']} tokens",
        f"- Estimated reduction: {summary['estimated_token_reduction_percent']}%", "",
        "## Evidence selected", "",
    ]
    # Add a short explanation for every selected file.
    for item in bundle["selected_evidence"]:
        lines.extend([
            f"### `{item['path']}` — score {item['score']}",
            f"Reason: {item['reason']}",
            f"Preview: {item['preview']}",
            "",
        ])
    # Add the role assignments for the next investigation step.
    lines.extend(["## Focused roles", ""])
    for role, details in bundle["roles"].items():
        lines.append(f"### {role.title()}: {details['goal']}")
        for item in details["files"]:
            lines.append(f"- `{item['path']}`")
        lines.append("")
    # Explain what the current prototype does not automate yet.
    lines.extend([
        "## Boundary of this prototype", "",
        "This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.",
        "",
    ])
    # Save the report as Markdown.
    output_path.write_text("\n".join(lines))


# Run the command-line application.
def main() -> None:
    # Create a terminal argument parser with a useful help description.
    parser = argparse.ArgumentParser(description=__doc__)
    # Accept the local GitHub repository to investigate.
    parser.add_argument("repository", type=Path)
    # Accept any natural-language question about that repository.
    parser.add_argument("question")
    # Let the user control how many files become context.
    parser.add_argument("--limit", type=int, default=20)
    # Let the user control how many files each role receives.
    parser.add_argument("--budget", type=int, default=6)
    # Save results in the project's outputs folder by default.
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    # Parse the actual terminal arguments.
    args = parser.parse_args()
    # Build the evidence bundle.
    bundle = build_bundle(args.repository, args.question, args.limit, args.budget)
    # Ensure the output directory exists.
    args.output.mkdir(parents=True, exist_ok=True)
    # Convert the question into a safe, readable filename.
    slug = re.sub(r"[^a-z0-9]+", "-", args.question.lower()).strip("-")[:40] or "question"
    # Add a timestamp so repeated questions do not overwrite earlier results.
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # Define both machine-readable and human-readable output files.
    json_path = args.output / f"investigation-{timestamp}-{slug}.json"
    markdown_path = args.output / f"investigation-{timestamp}-{slug}.md"
    # Save the structured bundle.
    json_path.write_text(json.dumps(bundle, indent=2) + "\n")
    # Save the readable report.
    write_report(bundle, markdown_path)
    # Print the most important result for the terminal user.
    print(f"JSON saved to: {json_path}")
    print(f"Report saved to: {markdown_path}")
    print(f"Selected {len(bundle['selected_evidence'])} files from {len(discover(args.repository))} candidates.")
    print(f"Estimated context reduction: {bundle['repository_summary']['estimated_token_reduction_percent']}%.")


# Only run the application when this file is executed directly.
if __name__ == "__main__":
    main()

