# Repository Investigation Report

**Question:** How does OpenCode handle failed tool calls?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 62747 tokens
- Estimated reduction: 99.4%

## Evidence selected

### `packages/opencode/src/session/prompt/anthropic.txt` — score 6
Reason: matched: calls, failed, handle, opencode, tool
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/core/src/github-copilot/chat/openai-compatible-chat-language-model.ts` — score 5
Reason: matched: calls, failed, handle, opencode, tool
Preview: import { APICallError, InvalidResponseDataError, type LanguageModelV3, type LanguageModelV3CallOptions, type LanguageModelV3Content, type LanguageModelV3StreamPart, type SharedV3ProviderMetadata, type SharedV3Warning, } from "@ai-sdk/provid

### `packages/llm/DESIGN.md` — score 5
Reason: matched: calls, failed, opencode, tool
Preview: # AI Library Design > Discussion draft. This document describes the intended replacement for the > current private `@opencode-ai/llm` API. Names and exact TypeScript signatures > are illustrative until implementation, but the domain boundar

### `packages/opencode/src/session/prompt/beast.txt` — score 5
Reason: matched: calls, handle, opencode, tool
Preview: You are opencode, an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Your thinking should be thorough and so it's fine if it's very long. However, avoid unneces

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 5
Reason: matched: calls, handle, opencode, tool
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `packages/opencode/src/session/prompt/default.txt` — score 5
Reason: matched: calls, failed, opencode, tool
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/kimi.txt` — score 5
Reason: matched: calls, failed, opencode, tool
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/test/acp/event.test.ts` — score 5
Reason: matched: calls, failed, handle, opencode, tool
Preview: import { describe, expect, it } from "bun:test" import type { AgentSideConnection } from "@agentclientprotocol/sdk" import { LayerNode } from "@opencode-ai/core/effect/layer-node" import type { Event, Message, OpencodeClient, Part, SessionM

### `perf/test-suite.md` — score 5
Reason: matched: calls, failed, opencode, tool
Preview: # Test Suite Speed ## Goal Speed up the `packages/opencode` test suite without reducing coverage or hiding failures. ## Benchmark Command Run from `packages/opencode`: ```sh bun run bench:test ``` The full-suite benchmark defaults to one me

### `specs/storage/remove-opencode-db.md` — score 5
Reason: matched: calls, handle, opencode, tool
Preview: # Remove `packages/opencode/src/storage/db.ts` ## Goal Remove all production usages of the legacy `packages/opencode/src/storage/db.ts` module. This means eliminating imports from `@/storage/db` or `./storage/db`, including: - `Database.use

### `specs/v2/schema-changelog.md` — score 5
Reason: matched: calls, failed, opencode, tool
Preview: # V2 Schema Changelog ## 2026-06-26: Add Finite Session History - Add `GET /api/session/:sessionID/history` and generated Promise, Effect, and legacy JavaScript client methods. - Page public durable Session events after an optional exclusiv

### `.github/workflows/docs-locale-sync.yml` — score 4
Reason: matched: calls, opencode, tool
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `CONTEXT.md` — score 4
Reason: matched: failed, opencode, tool
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `github/index.ts` — score 4
Reason: matched: failed, handle, opencode, tool
Preview: import { $ } from "bun" import path from "node:path" import { Octokit } from "@octokit/rest" import { graphql } from "@octokit/graphql" import * as core from "@actions/core" import * as github from "@actions/github" import type { Context as

### `packages/app/AGENTS.md` — score 4
Reason: matched: calls, opencode, tool
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/app/create-effect-simplification-spec.md` — score 4
Reason: matched: calls, handle, opencode
Preview: # CreateEffect Simplification Implementation Spec Reduce reactive misuse across `packages/app`. --- ## Context This work targets `packages/app/src`, which currently has 101 `createEffect` calls across 37 files. The biggest clusters are `pag

### `packages/codemode/README.md` — score 4
Reason: matched: calls, opencode, tool
Preview: # @opencode-ai/codemode Effect-native confined code execution over explicit, schema-described tools. CodeMode lets a model write a small JavaScript program that can call only the tools supplied by the host. The program can sequence calls, t

### `packages/codemode/codemode.md` — score 4
Reason: matched: calls, opencode, tool
Preview: # CodeMode Design and Status This is the living design and status document for `@opencode-ai/codemode` and its existing V2 OpenCode adapter. It records current behavior, intentional boundaries, durable rationale, and material remaining work

### `packages/codemode/src/codemode.ts` — score 4
Reason: matched: calls, failed, opencode, tool
Preview: import { Effect, Schema } from "effect" import { executeWithLimits } from "./interpreter/runtime.js" import { type HostTools, type Services, type ToolDescription, ToolRuntime } from "./tool-runtime.js" import type { Definition } from "./too

### `packages/codemode/src/tool-runtime.ts` — score 4
Reason: matched: calls, failed, opencode, tool
Preview: import { Cause, Effect, Schema } from "effect" import { ToolError, toolError } from "./tool-error.js" import { decodeInput as decodeToolInput, decodeOutput as decodeToolOutput, identifierSegment, inputProperties, inputTypeScript, outputType

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.

### Scout: Compare documentation and configuration with the implementation.
- `packages/codemode/README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/anthropic.txt`
- `packages/core/src/github-copilot/chat/openai-compatible-chat-language-model.ts`
- `packages/llm/DESIGN.md`
- `packages/opencode/src/session/prompt/beast.txt`
- `packages/opencode/src/session/prompt/copilot-gpt-5.txt`
- `packages/opencode/src/session/prompt/default.txt`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
