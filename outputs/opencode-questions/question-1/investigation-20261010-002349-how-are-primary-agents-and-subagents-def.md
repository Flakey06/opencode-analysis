# Repository Investigation Report

**Question:** How are primary agents and subagents defined?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 39700 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `.github/workflows/docs-locale-sync.yml` — score 5
Reason: matched: are, defined, primary, subagents
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `packages/opencode/test/agent/agent.test.ts` — score 5
Reason: matched: agents, are, defined, primary, subagents
Preview: import { afterEach, expect } from "bun:test" import { LayerNode } from "@opencode-ai/core/effect/layer-node" import { Cause, Effect, Exit, Layer } from "effect" import path from "path" import { disposeAllInstances, TestInstance } from "../f

### `packages/core/src/plugin/command/review.txt` — score 4
Reason: matched: agents, are, primary
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: agents, are, primary
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/core/src/v1/config/config.ts` — score 4
Reason: matched: agents, are, primary, subagents
Preview: export * as ConfigV1 from "./config" import { Schema } from "effect" import { NonNegativeInt, PositiveInt, type DeepMutable } from "../../schema" import { ConfigExperimental } from "../../config/experimental" import { ConfigReference } from

### `packages/llm/AGENTS.md` — score 4
Reason: matched: agents, are, primary
Preview: # LLM Package Guide ## Effect - Prefer `HttpClient.HttpClient` / `HttpClientResponse.HttpClientResponse` over web `fetch` / `Response` at package boundaries. - Use `Stream.Stream` for streaming data flow. Avoid ad hoc async generators or ma

### `packages/opencode/src/agent/generate.txt` — score 4
Reason: matched: agents, are, primary
Preview: You are an elite AI agent architect specializing in crafting high-performance agent configurations. Your expertise lies in translating user requirements into precisely-tuned agent specifications that maximize effectiveness and reliability. 

### `packages/opencode/src/command/template/review.txt` — score 4
Reason: matched: agents, are, primary
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/opencode/src/session/prompt/default.txt` — score 4
Reason: matched: agents, are, defined
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/gpt-astra.txt` — score 4
Reason: matched: agents, are, subagents
Preview: You are an AI agent powered by OpenCode, a coding agent harness. Help the user accomplish their goals using the tools you have available. # Harness - Responses are rendered as GitHub-flavored Markdown. - `<system-reminder>` blocks are harne

### `packages/opencode/src/session/prompt/gpt.txt` — score 4
Reason: matched: agents, are, primary
Preview: You are OpenCode, You and the user share the same workspace and collaborate to achieve the user's goals. You are a deeply pragmatic, effective software engineer. You take engineering quality seriously, and collaboration comes through as dir

### `packages/opencode/src/session/prompt/kimi.txt` — score 4
Reason: matched: agents, are, primary
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/trinity.txt` — score 4
Reason: matched: agents, are, defined
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `.opencode/agent/duplicate-pr.md` — score 3
Reason: matched: are, primary
Preview: --- mode: primary hidden: true model: opencode/claude-haiku-4-5 color: "#E67E22" tools: "*": false "github-pr-search": true --- You are a duplicate PR detection agent. When a PR is opened, your job is to search for potentially duplicate or 

### `.opencode/agent/triage.md` — score 3
Reason: matched: are, primary
Preview: --- mode: primary hidden: true model: opencode/gpt-6-luna color: "#44BA81" tools: "*": false "github-triage": true --- You are a triage agent responsible for triaging github issues. Use your github-triage tool to triage issues. This file is

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

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/opencode/test/agent/agent.test.ts`
- `packages/core/src/plugin/command/review.txt`
- `packages/opencode/src/agent/generate.txt`
- `packages/opencode/src/command/template/review.txt`
- `.opencode/agent/duplicate-pr.md`
- `.opencode/agent/triage.md`

### Scout: Compare documentation and configuration with the implementation.
- `packages/core/src/v1/config/config.ts`
- `README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `.github/workflows/docs-locale-sync.yml`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `packages/llm/AGENTS.md`
- `packages/opencode/src/session/prompt/default.txt`
- `packages/opencode/src/session/prompt/gpt-astra.txt`
- `packages/opencode/src/session/prompt/gpt.txt`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
