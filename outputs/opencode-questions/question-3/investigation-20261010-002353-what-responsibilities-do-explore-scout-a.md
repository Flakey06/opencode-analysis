# Repository Investigation Report

**Question:** What responsibilities do Explore, Scout, and other agents have?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 42299 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `packages/opencode/src/agent/generate.txt` — score 5
Reason: matched: agents, have, other, responsibilities
Preview: You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability. 

### `packages/opencode/src/session/prompt/plan-mode.txt` — score 5
Reason: matched: agents, explore, have, other
Preview: <system-reminder> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs 

### `packages/opencode/src/session/prompt/plan-reminder-anthropic.txt` — score 5
Reason: matched: agents, explore, have, other
Preview: <system-reminder> # Plan Mode - System Reminder Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tool

### `packages/opencode/src/session/prompt/plan.txt` — score 5
Reason: matched: agents, explore, have, other
Preview: <system-reminder> # Plan Mode - System Reminder CRITICAL: Plan mode ACTIVE - you are in READ-ONLY phase. STRICTLY FORBIDDEN: ANY file edits, modifications, or system changes. Do NOT use sed, tee, echo, cat, or ANY other bash command to mani

### `CONTRIBUTING.md` — score 4
Reason: matched: agents, have, other
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/app/create-effect-simplification-spec.md` — score 4
Reason: matched: have, other, responsibilities
Preview: # CreateEffect Simplification Implementation Spec Reduce reactive misuse across `packages/app`. --- ## Context This work targets `packages/app/src`, which currently has 101 `createEffect` calls across 37 files. The biggest clusters are `pag

### `packages/core/src/plugin/command/review.txt` — score 4
Reason: matched: agents, explore, other
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: agents, explore, other
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/llm/AGENTS.md` — score 4
Reason: matched: agents, have, other
Preview: # LLM Package Guide ## Effect - Prefer `HttpClient.HttpClient` / `HttpClientResponse.HttpClientResponse` over web `fetch` / `Response` at package boundaries. - Use `Stream.Stream` for streaming data flow. Avoid ad hoc async generators or ma

### `packages/opencode/src/command/template/review.txt` — score 4
Reason: matched: agents, explore, other
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/src/session/prompt/anthropic.txt` — score 4
Reason: matched: agents, have, other
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/session/prompt/beast.txt` — score 4
Reason: matched: explore, have, other
Preview: You are opencode, an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Your thinking should be thorough and so it's fine if it's very long. However, avoid unneces

### `packages/opencode/src/session/prompt/codex.txt` — score 4
Reason: matched: explore, have, other
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. ## Editing constraints - 

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 4
Reason: matched: explore, have, other
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `packages/opencode/src/session/prompt/default.txt` — score 4
Reason: matched: agents, have, other
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/gpt.txt` — score 4
Reason: matched: agents, have, other
Preview: You are OpenCode, You and the user share the same workspace and collaborate to achieve the user's goals. You are a deeply pragmatic, effective software engineer. You take engineering quality seriously, and collaboration comes through as dir

### `packages/opencode/src/session/prompt/kimi.txt` — score 4
Reason: matched: agents, have, other
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/meta.txt` — score 4
Reason: matched: explore, have, other
Preview: You are OpenCode, a coding agent that helps users with software engineering tasks. You are powered by {{MODEL_NAME}}, a large language model trained by Meta MSL. Use the instructions below and the tools available to assist the user. # Commu

### `packages/opencode/src/session/prompt/trinity.txt` — score 4
Reason: matched: agents, have, other
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `packages/opencode/src/tool/task.txt` — score 4
Reason: matched: agents, have, other
Preview: Launch a new agent to handle complex, multistep tasks autonomously. When using the Task tool, you must specify a subagent_type parameter to select which agent type to use. When NOT to use the Task tool: - If you want to read a specific file

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/opencode/src/agent/generate.txt`
- `packages/core/src/plugin/command/review.txt`
- `packages/opencode/src/command/template/review.txt`
- `packages/opencode/src/tool/task.txt`

### Scout: Compare documentation and configuration with the implementation.

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/plan-mode.txt`
- `packages/opencode/src/session/prompt/plan-reminder-anthropic.txt`
- `packages/opencode/src/session/prompt/plan.txt`
- `CONTRIBUTING.md`
- `packages/app/create-effect-simplification-spec.md`
- `packages/core/src/plugin/skill/customize-opencode.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
