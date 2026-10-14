# Repository Investigation Report

**Question:** How are tool permissions and approvals enforced?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 41864 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `specs/v2/schema-changelog.md` — score 6
Reason: matched: approvals, are, enforced, permissions, tool
Preview: # V2 Schema Changelog ## 2026-06-26: Add Finite Session History - Add `GET /api/session/:sessionID/history` and generated Promise, Effect, and legacy JavaScript client methods. - Page public durable Session events after an optional exclusiv

### `packages/llm/AGENTS.md` — score 5
Reason: matched: are, enforced, permissions, tool
Preview: # LLM Package Guide ## Effect - Prefer `HttpClient.HttpClient` / `HttpClientResponse.HttpClientResponse` over web `fetch` / `Response` at package boundaries. - Use `Stream.Stream` for streaming data flow. Avoid ad hoc async generators or ma

### `.github/workflows/docs-locale-sync.yml` — score 4
Reason: matched: are, permissions, tool
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `AGENTS.md` — score 4
Reason: matched: are, permissions, tool
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: are, permissions, tool
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/core/src/tool/AGENTS.md` — score 4
Reason: matched: are, permissions, tool
Preview: # Core Tool Architecture This folder owns Core's one local tool representation, process and Location registration, effective lookup, and settlement. ## Representations - `tool.ts` defines the opaque canonical `Tool.make({ description, input

### `packages/llm/README.md` — score 4
Reason: matched: are, enforced, tool
Preview: # @opencode-ai/llm Schema-first LLM core for opencode. One typed request, response, event, and tool language; provider quirks live in adapters, not in calling code. ```ts import { Effect } from "effect" import { LLM, LLMClient } from "@open

### `specs/v2/session.md` — score 4
Reason: matched: are, permissions, tool
Preview: # Session API ## Current V2 Core Slice The Effect-native core facade treats prompt recording and execution as separate responsibilities: ```text sessions.create({ id?, location, ... }) -> omitted ID generates one internal Session ID -> supp

### `.github/workflows/docs-update.yml` — score 3
Reason: matched: are, permissions
Preview: name: docs-update on: schedule: - cron: "0 */12 * * *" workflow_dispatch: env: LOOKBACK_HOURS: 4 jobs: update-docs: if: github.repository == 'sst/opencode' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: id-token: write contents: write p

### `.github/workflows/duplicate-issues.yml` — score 3
Reason: matched: are, permissions
Preview: name: duplicate-issues on: issues: types: [opened, edited] jobs: check-duplicates: if: github.event.action == 'opened' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: 

### `.github/workflows/pr-standards.yml` — score 3
Reason: matched: are, permissions
Preview: name: pr-standards on: pull_request_target: types: [opened, edited, synchronize] jobs: check-standards: runs-on: ubuntu-latest permissions: contents: read pull-requests: write steps: - name: Check PR standards uses: actions/github-script@f2

### `.github/workflows/review.yml` — score 3
Reason: matched: are, permissions
Preview: name: review on: issue_comment: types: [created] jobs: check-guidelines: if: | github.event.issue.pull_request && startsWith(github.event.comment.body, '/review') && contains(fromJson('["OWNER","MEMBER"]'), github.event.comment.author_assoc

### `.opencode/agent/duplicate-pr.md` — score 3
Reason: matched: are, tool
Preview: --- mode: primary hidden: true model: opencode/claude-haiku-4-5 color: "#E67E22" tools: "*": false "github-pr-search": true --- You are a duplicate PR detection agent. When a PR is opened, your job is to search for potentially duplicate or 

### `.opencode/agent/triage.md` — score 3
Reason: matched: are, tool
Preview: --- mode: primary hidden: true model: opencode/gpt-6-luna color: "#44BA81" tools: "*": false "github-triage": true --- You are a triage agent responsible for triaging github issues. Use your github-triage tool to triage issues. This file is

### `.opencode/command/learn.md` — score 3
Reason: matched: are, tool
Preview: --- description: Extract non-obvious learnings from session to AGENTS.md files to build codebase understanding --- Analyze this session and extract non-obvious learnings to add to AGENTS.md files. AGENTS.md files can exist at any directory 

### `CONTEXT.md` — score 3
Reason: matched: are, tool
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `CONTRIBUTING.md` — score 3
Reason: matched: are, enforced
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/app/AGENTS.md` — score 3
Reason: matched: are, tool
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/app/V1_API_MIGRATION.md` — score 3
Reason: matched: are, permissions
Preview: # V1 API Migration Checklist The app is currently hybrid. In this document, V1 refers to the legacy unprefixed server APIs used by `@opencode-ai/sdk/v2`, despite the SDK package name. ## Events - [x] Replace `GET /global/event` with `GET /a

### `packages/codemode/AGENTS.md` — score 3
Reason: matched: are, tool
Preview: # @opencode-ai/codemode - This local package owns confined execution over explicit schema-described tools. Applications own authorization, persistence, external authority, and tool-specific delivery semantics. - Do not add a speculative gen

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/core/src/tool/AGENTS.md`
- `.opencode/agent/duplicate-pr.md`
- `.opencode/agent/triage.md`
- `.opencode/command/learn.md`

### Scout: Compare documentation and configuration with the implementation.
- `packages/llm/README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `specs/v2/schema-changelog.md`
- `packages/llm/AGENTS.md`
- `.github/workflows/docs-locale-sync.yml`
- `AGENTS.md`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `specs/v2/session.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
