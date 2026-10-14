# Repository Investigation Report

**Question:** Where are permissions enforced in the source code?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 55808 tokens
- Estimated reduction: 99.5%

## Evidence selected

### `packages/llm/AGENTS.md` — score 7
Reason: matched: are, code, enforced, permissions, source, where
Preview: # LLM Package Guide ## Effect - Prefer `HttpClient.HttpClient` / `HttpClientResponse.HttpClientResponse` over web `fetch` / `Response` at package boundaries. - Use `Stream.Stream` for streaming data flow. Avoid ad hoc async generators or ma

### `AGENTS.md` — score 6
Reason: matched: are, code, permissions, source, where
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `packages/core/src/plugin/skill/customize-opencode.md` — score 6
Reason: matched: are, code, permissions, source, where
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `specs/v2/catalog-config-plugin-lifecycle.md` — score 6
Reason: matched: are, code, permissions, source, where
Preview: # Catalog / Config / Plugin Lifecycle Options Status: current core has selected replayable Location-scoped Catalog transforms, aligned with option B. Reload/watch behavior and deferred external plugin activation remain design work; the opti

### `.github/workflows/docs-locale-sync.yml` — score 5
Reason: matched: are, code, permissions, source
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.github/workflows/pr-standards.yml` — score 5
Reason: matched: are, code, permissions, where
Preview: name: pr-standards on: pull_request_target: types: [opened, edited, synchronize] jobs: check-standards: runs-on: ubuntu-latest permissions: contents: read pull-requests: write steps: - name: Check PR standards uses: actions/github-script@f2

### `CONTRIBUTING.md` — score 5
Reason: matched: are, code, enforced, source
Preview: # Contributing to OpenCode We want to make it easy for you to contribute to OpenCode. Here are the most common type of changes that get merged: - Bug fixes - Additional LSPs / Formatters - Improvements to LLM performance - Support for new p

### `packages/app/AGENTS.md` — score 5
Reason: matched: are, code, source, where
Preview: ## Priorities - Prioritise, in this order: stability, simplicity, performance. - Before changing session or timeline code, record a production benchmark baseline and compare it after the change. ## Debugging - NEVER try to restart the app, 

### `packages/app/create-effect-simplification-spec.md` — score 5
Reason: matched: are, code, source, where
Preview: # CreateEffect Simplification Implementation Spec Reduce reactive misuse across `packages/app`. --- ## Context This work targets `packages/app/src`, which currently has 101 `createEffect` calls across 37 files. The biggest clusters are `pag

### `packages/console/app/src/routes/legal/terms-of-service/index.tsx` — score 5
Reason: matched: are, code, permissions, source, where
Preview: import "../../brand/index.css" import "./index.css" import { Title, Meta } from "@solidjs/meta" import { Header } from "~/component/header" import { Footer } from "~/component/footer" import { Legal } from "~/component/legal" import { Local

### `packages/opencode/specs/effect/todo.md` — score 5
Reason: matched: are, code, source, where
Preview: # Effect TODO Short roadmap for Effect cleanup in `packages/opencode`. Current patterns and examples live in [`guide.md`](./guide.md). Error boundary migration details live in [`error-boundaries-plan.md`](./error-boundaries-plan.md). Test m

### `packages/opencode/specs/openapi-translation-cleanup.md` — score 5
Reason: matched: are, code, source, where
Preview: # OpenAPI Translation Cleanup Plan ## Goal Trim `packages/opencode/src/server/routes/instance/httpapi/public.ts` until OpenAPI generation is mostly a direct projection of the `HttpApi` route declarations, without breaking the generated SDK 

### `packages/opencode/src/session/prompt/anthropic.txt` — score 5
Reason: matched: are, code, source, where
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/session/prompt/default.txt` — score 5
Reason: matched: are, code, source, where
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER generate or guess URLs for the user unless y

### `packages/opencode/src/session/prompt/gemini.txt` — score 5
Reason: matched: are, code, source, where
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/opencode/src/session/prompt/meta.txt` — score 5
Reason: matched: are, code, source, where
Preview: You are OpenCode, a coding agent that helps users with software engineering tasks. You are powered by {{MODEL_NAME}}, a large language model trained by Meta MSL. Use the instructions below and the tools available to assist the user. # Commu

### `packages/opencode/src/session/prompt/trinity.txt` — score 5
Reason: matched: are, code, source, where
Preview: You are opencode, an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. # Tone and style You should be concise, direct, and to the point. When

### `specs/tui-package.md` — score 5
Reason: matched: are, code, source, where
Preview: # TUI Package Extraction ## Goal Move the canonical OpenCode terminal application from `packages/opencode/src/cli/cmd/tui` into a self-contained workspace package while the legacy CLI and the new CLI continue to use the same implementation.

### `specs/v2/schema-changelog.md` — score 5
Reason: matched: are, enforced, permissions, source
Preview: # V2 Schema Changelog ## 2026-06-26: Add Finite Session History - Add `GET /api/session/:sessionID/history` and generated Promise, Effect, and legacy JavaScript client methods. - Page public durable Session events after an optional exclusiv

### `.github/workflows/docs-update.yml` — score 4
Reason: matched: are, permissions, where
Preview: name: docs-update on: schedule: - cron: "0 */12 * * *" workflow_dispatch: env: LOOKBACK_HOURS: 4 jobs: update-docs: if: github.repository == 'sst/opencode' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: id-token: write contents: write p

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.

### Scout: Compare documentation and configuration with the implementation.

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/llm/AGENTS.md`
- `AGENTS.md`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `specs/v2/catalog-config-plugin-lifecycle.md`
- `.github/workflows/docs-locale-sync.yml`
- `.github/workflows/pr-standards.yml`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
