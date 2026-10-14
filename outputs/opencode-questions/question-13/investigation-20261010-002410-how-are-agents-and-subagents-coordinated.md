# Repository Investigation Report

**Question:** How are agents and subagents coordinated?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 37130 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `packages/opencode/src/session/prompt/gpt-astra.txt` — score 4
Reason: matched: agents, are, subagents
Preview: You are an AI agent powered by OpenCode, a coding agent harness. Help the user accomplish their goals using the tools you have available. # Harness - Responses are rendered as GitHub-flavored Markdown. - `<system-reminder>` blocks are harne

### `.github/workflows/docs-locale-sync.yml` — score 3
Reason: matched: are, subagents
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.opencode/command/learn.md` — score 3
Reason: matched: agents, are
Preview: --- description: Extract non-obvious learnings from session to AGENTS.md files to build codebase understanding --- Analyze this session and extract non-obvious learnings to add to AGENTS.md files. AGENTS.md files can exist at any directory 

### `AGENTS.md` — score 3
Reason: matched: agents, are
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `CONTEXT.md` — score 3
Reason: matched: agents, are
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `CONTRIBUTING.md` — score 3
Reason: matched: agents, are
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `README.md` — score 3
Reason: matched: agents, are
Preview: <p align="center"> <a href="https://opencode.ai"> <picture> <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)"> <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" med

### `packages/app/AGENTS.md` — score 3
Reason: matched: agents, are
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/codemode/AGENTS.md` — score 3
Reason: matched: agents, are
Preview: # @opencode-ai/codemode - This local package owns confined execution over explicit schema-described tools. Applications own authorization, persistence, external authority, and tool-specific delivery semantics. - Do not add a speculative gen

### `packages/core/src/plugin/command/initialize.txt` — score 3
Reason: matched: agents, are
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/core/src/plugin/command/review.txt` — score 3
Reason: matched: agents, are
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/core/src/plugin/skill/customize-opencode.md` — score 3
Reason: matched: agents, are
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/core/src/tool/AGENTS.md` — score 3
Reason: matched: agents, are
Preview: # Core Tool Architecture This folder owns Core's one local tool representation, process and Location registration, effective lookup, and settlement. ## Representations - `tool.ts` defines the opaque canonical `Tool.make({ description, input

### `packages/core/src/v1/config/config.ts` — score 3
Reason: matched: agents, are, subagents
Preview: export * as ConfigV1 from "./config" import { Schema } from "effect" import { NonNegativeInt, PositiveInt, type DeepMutable } from "../../schema" import { ConfigExperimental } from "../../config/experimental" import { ConfigReference } from

### `packages/llm/AGENTS.md` — score 3
Reason: matched: agents, are
Preview: # LLM Package Guide ## Effect - Prefer `HttpClient.HttpClient` / `HttpClientResponse.HttpClientResponse` over web `fetch` / `Response` at package boundaries. - Use `Stream.Stream` for streaming data flow. Avoid ad hoc async generators or ma

### `packages/llm/README.md` — score 3
Reason: matched: agents, are
Preview: # @opencode-ai/llm Schema-first LLM core for opencode. One typed request, response, event, and tool language; provider quirks live in adapters, not in calling code. ```ts import { Effect } from "effect" import { LLM, LLMClient } from "@open

### `packages/opencode/AGENTS.md` — score 3
Reason: matched: agents, are
Preview: # opencode database guide ## Database - **Schema**: Drizzle schema lives in `packages/core/src/**/*.sql.ts`. - **Migrations**: database migrations live in `packages/core` and are applied by core. ## Development server - Running `bun dev` fr

### `packages/opencode/specs/effect/errors.md` — score 3
Reason: matched: agents, are
Preview: # Typed Error Migration This note expands the `ERR`, `RENDER`, and `HTTP` tracks from [`todo.md`](./todo.md). It is the current reference for expected failures, typed service errors, and HTTP error boundaries. For the migration architecture

### `packages/opencode/specs/effect/todo.md` — score 3
Reason: matched: are, subagents
Preview: # Effect TODO Short roadmap for Effect cleanup in `packages/opencode`. Current patterns and examples live in [`guide.md`](./guide.md). Error boundary migration details live in [`error-boundaries-plan.md`](./error-boundaries-plan.md). Test m

### `packages/opencode/src/agent/generate.txt` — score 3
Reason: matched: agents, are
Preview: You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability. 

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `.opencode/command/learn.md`
- `packages/core/src/plugin/command/initialize.txt`
- `packages/core/src/plugin/command/review.txt`
- `packages/core/src/tool/AGENTS.md`
- `packages/opencode/src/agent/generate.txt`

### Scout: Compare documentation and configuration with the implementation.
- `README.md`
- `packages/core/src/v1/config/config.ts`
- `packages/llm/README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/gpt-astra.txt`
- `.github/workflows/docs-locale-sync.yml`
- `AGENTS.md`
- `CONTEXT.md`
- `CONTRIBUTING.md`
- `packages/app/AGENTS.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
