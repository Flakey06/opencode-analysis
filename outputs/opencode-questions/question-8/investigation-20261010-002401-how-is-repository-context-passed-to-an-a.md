# Repository Investigation Report

**Question:** How is repository context passed to an agent?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 40321 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `packages/app/V1_API_MIGRATION.md` — score 4
Reason: matched: agent, context, repository
Preview: # V1 API Migration Checklist The app is currently hybrid. In this document, V1 refers to the legacy unprefixed server APIs used by `@opencode-ai/sdk/v2`, despite the SDK package name. ## Events - [x] Replace `GET /global/event` with `GET /a

### `packages/core/src/plugin/command/initialize.txt` — score 4
Reason: matched: agent, context, repository
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: agent, context, repository
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/opencode/src/command/template/initialize.txt` — score 4
Reason: matched: agent, context, repository
Preview: Create or update `AGENTS.md` for this repository. The goal is a compact instruction file that helps future OpenCode sessions avoid mistakes and ramp up quickly. Every line should answer: "Would an agent likely miss this without help?" If no

### `packages/opencode/src/session/prompt/gemini.txt` — score 4
Reason: matched: agent, context, passed
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/plugin/src/v2/effect/PLAN.md` — score 4
Reason: matched: agent, context, repository
Preview: # V2 Plugin System Implementation Plan ## Status This document describes the agreed target design for the V2 plugin system. It is an implementation plan, not documentation for the current API. ## Goals - Internal and external plugins use th

### `perf/test-suite.md` — score 4
Reason: matched: agent, passed, repository
Preview: # Test Suite Speed ## Goal Speed up the `packages/opencode` test suite without reducing coverage or hiding failures. ## Benchmark Command Run from `packages/opencode`: ```sh bun run bench:test ``` The full-suite benchmark defaults to one me

### `specs/v2/config.md` — score 4
Reason: matched: agent, context, repository
Preview: # V2 Config Review This document breaks the legacy configuration schema into small review groups. Work through one group at a time and decide whether each field should be ported as-is, removed, or redesigned for v2. ## Status Labels - `pend

### `specs/v2/tools.md` — score 4
Reason: matched: agent, context, passed
Preview: # V2 Tools ## Design V2 has one opaque type for locally executable tools: ```ts type Definition<Input, Output> type AnyTool = Definition<any, any> const make: < Input extends Schema.Codec<any, any, never, never>, Output extends Schema.Codec

### `.github/workflows/docs-locale-sync.yml` — score 3
Reason: matched: agent, repository
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.github/workflows/docs-update.yml` — score 3
Reason: matched: agent, repository
Preview: name: docs-update on: schedule: - cron: "0 */12 * * *" workflow_dispatch: env: LOOKBACK_HOURS: 4 jobs: update-docs: if: github.repository == 'sst/opencode' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: id-token: write contents: write p

### `.github/workflows/duplicate-issues.yml` — score 3
Reason: matched: context, repository
Preview: name: duplicate-issues on: issues: types: [opened, edited] jobs: check-duplicates: if: github.event.action == 'opened' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: 

### `.github/workflows/nix-eval.yml` — score 3
Reason: matched: passed, repository
Preview: name: nix-eval on: push: branches: [dev] pull_request: branches: [dev] workflow_dispatch: concurrency: group: ${{ github.workflow }}-${{ github.ref }} cancel-in-progress: true permissions: contents: read jobs: nix-eval: runs-on: blacksmith-

### `.github/workflows/pr-management.yml` — score 3
Reason: matched: context, repository
Preview: name: pr-management on: pull_request_target: types: [opened] jobs: check-duplicates: runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read pull-requests: write steps: - name: Checkout repository uses: actions/checkout@34e114876b

### `.github/workflows/pr-standards.yml` — score 3
Reason: matched: context, repository
Preview: name: pr-standards on: pull_request_target: types: [opened, edited, synchronize] jobs: check-standards: runs-on: ubuntu-latest permissions: contents: read pull-requests: write steps: - name: Check PR standards uses: actions/github-script@f2

### `.github/workflows/review.yml` — score 3
Reason: matched: context, repository
Preview: name: review on: issue_comment: types: [created] jobs: check-guidelines: if: | github.event.issue.pull_request && startsWith(github.event.comment.body, '/review') && contains(fromJson('["OWNER","MEMBER"]'), github.event.comment.author_assoc

### `.github/workflows/triage.yml` — score 3
Reason: matched: agent, repository
Preview: name: triage on: issues: types: [opened] jobs: triage: runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5 # v4.3

### `.opencode/agent/triage.md` — score 3
Reason: matched: agent, context
Preview: --- mode: primary hidden: true model: opencode/gpt-6-luna color: "#44BA81" tools: "*": false "github-triage": true --- You are a triage agent responsible for triaging github issues. Use your github-triage tool to triage issues. This file is

### `.opencode/command/learn.md` — score 3
Reason: matched: agent, context
Preview: --- description: Extract non-obvious learnings from session to AGENTS.md files to build codebase understanding --- Analyze this session and extract non-obvious learnings to add to AGENTS.md files. AGENTS.md files can exist at any directory 

### `AGENTS.md` — score 3
Reason: matched: agent, context
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/core/src/plugin/command/initialize.txt`
- `packages/opencode/src/command/template/initialize.txt`
- `.opencode/agent/triage.md`
- `.opencode/command/learn.md`

### Scout: Compare documentation and configuration with the implementation.
- `specs/v2/config.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/app/V1_API_MIGRATION.md`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `packages/opencode/src/session/prompt/gemini.txt`
- `packages/plugin/src/v2/effect/PLAN.md`
- `perf/test-suite.md`
- `specs/v2/tools.md`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
