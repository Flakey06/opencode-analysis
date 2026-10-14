# Repository Investigator: Focused Context for OpenCode

## Executive summary

Large repositories contain more information than an AI coding agent can efficiently process in a single interaction. When a user asks OpenCode to investigate or modify a project, the agent must decide which files and documentation are relevant to the task.

This project investigates the question: How might OpenCode coordinate subagents and select repository context more effectively?

I built Repository Investigator, a transparent command-line prototype. Given a local GitHub repository and a natural-language question, it discovers relevant files, ranks them using explainable evidence, estimates context reduction, assigns files to focused Explore, Scout, and Review roles, and creates JSON and Markdown investigation reports.

The prototype does not claim to answer the user’s question automatically. Its purpose is to improve the stage before AI reasoning: deciding what evidence an agent should inspect.

## 1. Reason for Problem statement

Large software repositories contain more information than an AI coding agent can efficiently process in a single interaction. When a user asks OpenCode to investigate or modify a project, the agent must decide which files and documentation are relevant to the task.

This creates several challenges. Different subagents may inspect the same files and duplicate work. Irrelevant context can consume tokens, increase latency, and reduce the quality of the final response. It can also be difficult for the user to understand which files and findings influenced the agent’s conclusion.

This investigation explores whether focused task assignment, relevance-based file selection, and explainable evidence could help OpenCode produce more efficient, transparent, and reliable results.

## 2. User story

As a developer exploring an unfamiliar GitHub repository, I want to provide the repository and ask a natural-language question, so that I receive a focused, explainable evidence bundle instead of overwhelming an AI agent with the entire codebase.

## 3. Why I chose OpenCode

OpenCode is an appropriate subject because it is an AI coding agent with publicly available source code and documentation. Its open implementation makes it possible to compare intended behavior with technical evidence and investigate how agents, tools, permissions, and context are organized.

## 4. Proposed workflow

1. Local GitHub repository + user question
2. Discover source, documentation, and configuration files
3. Ignore dependencies and generated folders
4. Rank files using question/file evidence
5. Estimate broad versus focused context
6. Assign non-overlapping Explore, Scout, and Review roles
7. Save JSON evidence bundle and Markdown report
8. Use the focused evidence for AI-assisted investigation

## 5. Prototype behavior

### Repository discovery

The prototype recursively scans a local repository. It includes common source-code, documentation, and configuration files and skips folders such as `.git`, `node_modules`, build output, and Python caches.

This addresses the problem of irrelevant context entering the investigation.

### Relevance scoring

The user’s question is converted into keywords. Each candidate file is also converted into keywords. The prototype gives a file a score based on shared words and provides the matching words as an explanation.

This is deliberately simple and transparent. A user can inspect why a file was selected instead of trusting an unexplained ranking.

### Role assignment

Selected files are assigned to one of three focused roles:

- **Explore:** implementation, agents, tools, commands, and permissions.
- **Scout:** documentation and configuration describing intended behavior.
- **Review:** tests, APIs, integrations, and supporting modules.

Each file is assigned to one role to reduce duplicate investigation.

### Reports

The prototype produces:

- A JSON file for programmatic use.
- A Markdown report for human review.

The reports contain selected files, scores, matching keywords, previews, import hints, role assignments, and estimated context reduction.

## 6. How to use it

First clone a GitHub repository locally: (enter into githubrepo_pulls file)

git clone https://github.com/anomalyco/opencode.git
vs
git clone https://github.com/Flakey06/pip-install

Then run the investigator from the case-study project:

```bash
python3 prototype/repository_investigator.py \
  "github-repos/opencode" \
  "How are subagents coordinated and how are permissions enforced?"
```

The user can replace the repository path and question without changing the Python code.

## 7. Evaluation plan

To test whether the prototype addresses the problem, I will compare three workflows on the same repository and question:

| Workflow                  | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| Broad investigation       | Give an agent a large repository scope without planning.  |
| Independent investigation | Ask several agents to investigate without coordination.   |
| Repository Investigator   | Select focused evidence and assign non-overlapping roles. |

I will record:

- Number of candidate and selected files
- Estimated context size
- Duplicate files or findings
- Time required to reach a useful explanation
- Whether the evidence behind the conclusion is easy to identify

## 8. AI-assisted workflow

I used AI to help translate my planned logic into Python, explain unfamiliar syntax, debug errors, design the role structure, and improve the documentation. I did not treat generated code or explanations as automatically correct. I ran the program against real repositories, inspected the output, and corrected bugs such as a sorting function returning `None` instead of the sorted list.

My contribution was the problem framing, user story, workflow design, role definitions, evaluation criteria, testing decisions, and review of the implementation.

## 9. Limitations

The current prototype is a transparent baseline rather than a production integration with OpenCode.

- Keyword matching can miss semantically relevant files.
- File names do not always reveal a file’s purpose.
- Import hints are not a complete dependency graph.
- The prototype plans subagent work but does not launch real subagents.
- Estimated token counts are approximate.
- Duplicate findings still need to be compared after agents produce their conclusions.

## 10. Next steps

The next version could add semantic retrieval, dependency-graph analysis, configurable role rules, real OpenCode integration, evidence citations, and automated comparison of subagent findings.

## 11. Conclusion

Repository Investigator explores a practical improvement to AI coding-agent workflows: make context selection and task assignment explicit before asking an agent to reason. The prototype is intentionally understandable and measurable. Its value is not that keyword matching solves repository understanding, but that it creates a testable baseline for studying how focused context and coordinated subagents could improve AI-assisted software investigation.
