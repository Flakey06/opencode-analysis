# Repository Investigation Report

**Question:** How does OpenCode select repository context?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 48239 tokens
- Estimated reduction: 99.5%

## Evidence selected

### `.github/workflows/duplicate-issues.yml` — score 5
Reason: matched: context, opencode, repository, select
Preview: name: duplicate-issues on: issues: types: [opened, edited] jobs: check-duplicates: if: github.event.action == 'opened' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: 

### `.github/workflows/pr-standards.yml` — score 5
Reason: matched: context, opencode, repository, select
Preview: name: pr-standards on: pull_request_target: types: [opened, edited, synchronize] jobs: check-standards: runs-on: ubuntu-latest permissions: contents: read pull-requests: write steps: - name: Check PR standards uses: actions/github-script@f2

### `github/README.md` — score 5
Reason: matched: context, opencode, repository, select
Preview: # opencode GitHub Action A GitHub Action that integrates [opencode](https://opencode.ai) directly into your GitHub workflow. Mention `/opencode` in your comment, and opencode will execute tasks within your GitHub Actions runner. ## Features

### `.github/workflows/pr-management.yml` — score 4
Reason: matched: context, opencode, repository
Preview: name: pr-management on: pull_request_target: types: [opened] jobs: check-duplicates: runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read pull-requests: write steps: - name: Checkout repository uses: actions/checkout@34e114876b

### `.github/workflows/review.yml` — score 4
Reason: matched: context, opencode, repository
Preview: name: review on: issue_comment: types: [created] jobs: check-guidelines: if: | github.event.issue.pull_request && startsWith(github.event.comment.body, '/review') && contains(fromJson('["OWNER","MEMBER"]'), github.event.comment.author_assoc

### `CONTEXT.md` — score 4
Reason: matched: context, opencode, select
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `CONTRIBUTING.md` — score 4
Reason: matched: context, opencode, repository
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/app/AGENTS.md` — score 4
Reason: matched: context, opencode, select
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/app/V1_API_MIGRATION.md` — score 4
Reason: matched: context, opencode, repository
Preview: # V1 API Migration Checklist The app is currently hybrid. In this document, V1 refers to the legacy unprefixed server APIs used by `@opencode-ai/sdk/v2`, despite the SDK package name. ## Events - [x] Replace `GET /global/event` with `GET /a

### `packages/app/src/components/prompt-input-v2.tsx` — score 4
Reason: matched: context, opencode, repository, select
Preview: import { ImagePreview } from "@opencode-ai/ui/image-preview" import { useDialog } from "@opencode-ai/ui/context/dialog" import { ProviderIcon } from "@opencode-ai/ui/provider-icon" import { ButtonV2 } from "@opencode-ai/ui/v2/button-v2" imp

### `packages/core/src/plugin/command/initialize.txt` — score 4
Reason: matched: context, opencode, repository
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: context, opencode, repository
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/opencode/src/cli/cmd/github.handler.ts` — score 4
Reason: matched: context, opencode, repository, select
Preview: import path from "path" import { exec } from "child_process" import { Filesystem } from "@/util/filesystem" import * as prompts from "@clack/prompts" import { map, pipe, sortBy, values } from "remeda" import { Octokit } from "@octokit/rest"

### `packages/opencode/src/command/template/initialize.txt` — score 4
Reason: matched: context, opencode, repository
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/opencode/src/project/project.ts` — score 4
Reason: matched: context, opencode, repository, select
Preview: import { LayerNode } from "@opencode-ai/core/effect/layer-node" import { and, eq, sql } from "drizzle-orm" import { Database } from "@opencode-ai/core/database/database" import { ProjectDirectoryTable, ProjectTable } from "@opencode-ai/core

### `packages/opencode/src/session/prompt/default.txt` — score 4
Reason: matched: context, opencode, repository
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/trinity.txt` — score 4
Reason: matched: context, opencode, repository
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `packages/opencode/src/tool/task.txt` — score 4
Reason: matched: context, opencode, select
Preview: Launch a new agent to handle complex, multistep tasks autonomously. When using the Task tool, you must specify a subagent_type parameter to select which agent type to use. When NOT to use the Task tool: - If you want to read a specific file

### `packages/opencode/test/AGENTS.md` — score 4
Reason: matched: context, opencode, repository
Preview: # Test Fixtures Guide ## Temporary Directory Fixture The `tmpdir` function in `fixture/fixture.ts` creates temporary directories for tests with automatic cleanup. ### Basic Usage ```typescript import { tmpdir } from "./fixture/fixture" test

### `packages/opencode/test/tool/fixtures/models-api.json` — score 4
Reason: matched: context, opencode, repository
Preview: { "requesty": { "id": "requesty", "env": ["REQUESTY_API_KEY"], "npm": "@ai-sdk/openai-compatible", "api": "https://router.requesty.ai/v1", "name": "Requesty", "doc": "https://requesty.ai/solution/llm-routing/models", "models": { "xai/grok-4

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/core/src/plugin/command/initialize.txt`
- `packages/opencode/src/command/template/initialize.txt`
- `packages/opencode/src/tool/task.txt`
- `packages/opencode/test/tool/fixtures/models-api.json`

### Scout: Compare documentation and configuration with the implementation.
- `github/README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `.github/workflows/duplicate-issues.yml`
- `.github/workflows/pr-standards.yml`
- `.github/workflows/pr-management.yml`
- `.github/workflows/review.yml`
- `CONTEXT.md`
- `CONTRIBUTING.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
