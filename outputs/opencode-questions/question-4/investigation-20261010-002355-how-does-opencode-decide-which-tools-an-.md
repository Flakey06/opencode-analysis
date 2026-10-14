# Repository Investigation Report

**Question:** How does OpenCode decide which tools an agent can use?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 50779 tokens
- Estimated reduction: 99.5%

## Evidence selected

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 7
Reason: matched: agent, can, decide, opencode, tools, which
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `packages/codemode/README.md` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: # @opencode-ai/codemode Effect-native confined code execution over explicit, schema-described tools. CodeMode lets a model write a small JavaScript program that can call only the tools supplied by the host. The program can sequence calls, t

### `packages/codemode/codemode.md` — score 6
Reason: matched: agent, can, decide, opencode, tools
Preview: # CodeMode Design and Status This is the living design and status document for `@opencode-ai/codemode` and its existing V2 OpenCode adapter. It records current behavior, intentional boundaries, durable rationale, and material remaining work

### `packages/core/src/plugin/command/review.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/specs/effect/todo.md` — score 6
Reason: matched: can, decide, opencode, tools, which
Preview: # Effect TODO Short roadmap for Effect cleanup in `packages/opencode`. Current patterns and examples live in [`guide.md`](./guide.md). Error boundary migration details live in [`error-boundaries-plan.md`](./error-boundaries-plan.md). Test m

### `packages/opencode/src/command/template/review.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/src/session/prompt/anthropic.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/session/prompt/codex.txt` — score 6
Reason: matched: agent, can, decide, opencode, tools
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. ## Editing constraints - 

### `packages/opencode/src/session/prompt/gemini.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/opencode/src/session/prompt/kimi.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/trinity.txt` — score 6
Reason: matched: can, decide, opencode, tools, which
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `packages/opencode/src/tool/task.txt` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: Launch a new agent to handle complex, multistep tasks autonomously. When using the Task tool, you must specify a subagent_type parameter to select which agent type to use. When NOT to use the Task tool: - If you want to read a specific file

### `specs/tui-package.md` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: # TUI Package Extraction ## Goal Move the canonical OpenCode terminal application from `packages/opencode/src/cli/cmd/tui` into a self-contained workspace package while the legacy CLI and the new CLI continue to use the same implementation.

### `specs/v2/config.md` — score 6
Reason: matched: agent, can, decide, opencode, which
Preview: # V2 Config Review This document breaks the legacy configuration schema into small review groups. Work through one group at a time and decide whether each field should be ported as-is, removed, or redesigned for v2. ## Status Labels - `pend

### `specs/v2/session.md` — score 6
Reason: matched: agent, can, decide, opencode, tools
Preview: # Session API ## Current V2 Core Slice The Effect-native core facade treats prompt recording and execution as separate responsibilities: ```text sessions.create({ id?, location, ... }) -> omitted ID generates one internal Session ID -> supp

### `specs/v2/tools.md` — score 6
Reason: matched: agent, can, opencode, tools, which
Preview: # V2 Tools ## Design V2 has one opaque type for locally executable tools: ```ts type Definition<Input, Output> type AnyTool = Definition<any, any> const make: < Input extends Schema.Codec<any, any, never, never>, Output extends Schema.Codec

### `.opencode/command/learn.md` — score 5
Reason: matched: agent, can, opencode, which
Preview: --- description: Extract non-obvious learnings from session to AGENTS.md files to build codebase understanding --- Analyze this session and extract non-obvious learnings to add to AGENTS.md files. AGENTS.md files can exist at any directory 

### `CONTEXT.md` — score 5
Reason: matched: agent, can, opencode, which
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `CONTRIBUTING.md` — score 5
Reason: matched: can, decide, opencode, which
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/app/AGENTS.md` — score 5
Reason: matched: agent, can, opencode, tools
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/core/src/plugin/command/review.txt`
- `packages/opencode/src/command/template/review.txt`
- `packages/opencode/src/tool/task.txt`
- `.opencode/command/learn.md`

### Scout: Compare documentation and configuration with the implementation.
- `packages/codemode/README.md`
- `specs/v2/config.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/copilot-gpt-5.txt`
- `packages/codemode/codemode.md`
- `packages/opencode/specs/effect/todo.md`
- `packages/opencode/src/session/prompt/anthropic.txt`
- `packages/opencode/src/session/prompt/codex.txt`
- `packages/opencode/src/session/prompt/gemini.txt`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
