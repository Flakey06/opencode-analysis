# Repository Investigation Report

**Question:** What prevents agents from receiving too much irrelevant context?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 42847 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `CONTRIBUTING.md` — score 5
Reason: matched: agents, context, prevents, too
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/core/src/plugin/command/review.txt` — score 5
Reason: matched: agents, context, much, too
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/src/command/template/review.txt` — score 5
Reason: matched: agents, context, much, too
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/src/session/prompt/default.txt` — score 5
Reason: matched: agents, context, much, too
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/trinity.txt` — score 5
Reason: matched: agents, context, much, too
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `specs/v2/todo.md` — score 5
Reason: matched: context, much, prevents, too
Preview: # TODO ok we need to work towards a launch of v2 so we can get out of this rebuild phase ## Post-Hono cleanup - Kit The opencode server has moved to the Effect HttpApi backend. Remaining work is mostly cleanup: delete compatibility shims, s

### `AGENTS.md` — score 4
Reason: matched: agents, context, much
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `CONTEXT.md` — score 4
Reason: matched: agents, context, too
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `packages/opencode/AGENTS.md` — score 4
Reason: matched: agents, context, prevents
Preview: # opencode database guide ## Database - **Schema**: Drizzle schema lives in `packages/core/src/**/*.sql.ts`. - **Migrations**: database migrations live in `packages/core` and are applied by core. ## Development server - Running `bun dev` fr

### `packages/opencode/src/session/prompt/gpt-astra.txt` — score 4
Reason: matched: agents, context, much
Preview: You are an AI agent powered by OpenCode, a coding agent harness. Help the user accomplish their goals using the tools you have available. # Harness - Responses are rendered as GitHub-flavored Markdown. - `<system-reminder>` blocks are harne

### `packages/opencode/src/session/prompt/kimi.txt` — score 4
Reason: matched: agents, context, too
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/test/AGENTS.md` — score 4
Reason: matched: agents, context, much
Preview: # Test Fixtures Guide ## Temporary Directory Fixture The `tmpdir` function in `fixture/fixture.ts` creates temporary directories for tests with automatic cleanup. ### Basic Usage ```typescript import { tmpdir } from "./fixture/fixture" test

### `packages/plugin/src/v2/effect/PLAN.md` — score 4
Reason: matched: agents, context, prevents
Preview: # V2 Plugin System Implementation Plan ## Status This document describes the agreed target design for the V2 plugin system. It is an implementation plan, not documentation for the current API. ## Goals - Internal and external plugins use th

### `specs/v2/session.md` — score 4
Reason: matched: agents, context, too
Preview: # Session API ## Current V2 Core Slice The Effect-native core facade treats prompt recording and execution as separate responsibilities: ```text sessions.create({ id?, location, ... }) -> omitted ID generates one internal Session ID -> supp

### `.opencode/command/changelog.md` — score 3
Reason: matched: context, too
Preview: --- model: opencode/gpt-6-luna --- Create `UPCOMING_CHANGELOG.md` from the structured changelog input below. If `UPCOMING_CHANGELOG.md` already exists, ignore its current contents completely. Do not preserve, merge, or reuse text from the e

### `.opencode/command/learn.md` — score 3
Reason: matched: agents, context
Preview: --- description: Extract non-obvious learnings from session to AGENTS.md files to build codebase understanding --- Analyze this session and extract non-obvious learnings to add to AGENTS.md files. AGENTS.md files can exist at any directory 

### `packages/app/AGENTS.md` — score 3
Reason: matched: agents, context
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/console/app/src/i18n/en.ts` — score 3
Reason: matched: agents, context, much
Preview: export const dict = { "go.referral.ended.label": "Warning", "go.referral.ended": "The referral program has ended. Referral links no longer earn credit for you or the person who shared them.", "go.graph.bonus": "{{count}}× usage", "nav.githu

### `packages/core/src/plugin/command/initialize.txt` — score 3
Reason: matched: agents, context
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/core/src/plugin/skill/customize-opencode.md` — score 3
Reason: matched: agents, context
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/core/src/plugin/command/review.txt`
- `packages/opencode/src/command/template/review.txt`
- `.opencode/command/changelog.md`
- `.opencode/command/learn.md`
- `packages/core/src/plugin/command/initialize.txt`

### Scout: Compare documentation and configuration with the implementation.

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `CONTRIBUTING.md`
- `packages/opencode/src/session/prompt/default.txt`
- `packages/opencode/src/session/prompt/trinity.txt`
- `specs/v2/todo.md`
- `AGENTS.md`
- `CONTEXT.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
