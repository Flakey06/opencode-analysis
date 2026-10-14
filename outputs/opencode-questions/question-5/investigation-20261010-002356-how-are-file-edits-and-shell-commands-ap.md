# Repository Investigation Report

**Question:** How are file edits and shell commands approved?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 40368 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `packages/opencode/src/session/prompt/codex.txt` — score 7
Reason: matched: approved, are, commands, edits, file, shell
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. ## Editing constraints - 

### `packages/opencode/src/session/prompt/gpt.txt` — score 7
Reason: matched: approved, are, commands, edits, file, shell
Preview: You are OpenCode, You and the user share the same workspace and collaborate to achieve the user's goals. You are a deeply pragmatic, effective software engineer. You take engineering quality seriously, and collaboration comes through as dir

### `packages/core/src/plugin/skill/customize-opencode.md` — score 6
Reason: matched: are, commands, edits, file, shell
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/opencode/src/session/prompt/gemini.txt` — score 6
Reason: matched: approved, are, commands, file, shell
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/opencode/src/session/prompt/gpt-astra.txt` — score 6
Reason: matched: are, commands, edits, file, shell
Preview: You are an AI agent powered by OpenCode, a coding agent harness. Help the user accomplish their goals using the tools you have available. # Harness - Responses are rendered as GitHub-flavored Markdown. - `<system-reminder>` blocks are harne

### `.github/workflows/docs-locale-sync.yml` — score 5
Reason: matched: are, edits, file, shell
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `README.md` — score 5
Reason: matched: are, commands, edits, file
Preview: <p align="center"> <a href="https://opencode.ai"> <picture> <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)"> <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" med

### `SECURITY.md` — score 5
Reason: matched: are, commands, file, shell
Preview: # Security ## IMPORTANT We do not accept AI generated security reports. We receive a large number of these and we absolutely do not have the resources to review them all. If you submit one that will be an automatic ban from the project. ## 

### `packages/app/V1_API_MIGRATION.md` — score 5
Reason: matched: are, commands, file, shell
Preview: # V1 API Migration Checklist The app is currently hybrid. In this document, V1 refers to the legacy unprefixed server APIs used by `@opencode-ai/sdk/v2`, despite the SDK package name. ## Events - [x] Replace `GET /global/event` with `GET /a

### `packages/opencode/specs/tui-plugins.md` — score 5
Reason: matched: are, commands, edits, file
Preview: # TUI plugins Technical reference for the current TUI plugin system. ## Overview - TUI plugin config lives in `tui.json`. - Author package entrypoint is `@opencode-ai/plugin/tui`. - Internal plugins load inside the CLI app the same way exte

### `packages/opencode/src/session/prompt/anthropic.txt` — score 5
Reason: matched: are, commands, file, shell
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/session/prompt/build-switch.txt` — score 5
Reason: matched: are, commands, file, shell
Preview: <system-reminder> Your operational mode has changed from plan to build. You are no longer in read-only mode. You are permitted to make file changes, run shell commands, and utilize your arsenal of tools as needed. </system-reminder>

### `packages/opencode/src/session/prompt/kimi.txt` — score 5
Reason: matched: are, commands, file, shell
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/meta.txt` — score 5
Reason: matched: are, commands, file, shell
Preview: You are OpenCode, a coding agent that helps users with software engineering tasks. You are powered by {{MODEL_NAME}}, a large language model trained by Meta MSL. Use the instructions below and the tools available to assist the user. # Commu

### `packages/opencode/src/session/prompt/plan.txt` — score 5
Reason: matched: are, commands, edits, file
Preview: <system-reminder> # Plan Mode - System Reminder CRITICAL: Plan mode ACTIVE - you are in READ-ONLY phase. STRICTLY FORBIDDEN: ANY file edits, modifications, or system changes. Do NOT use sed, tee, echo, cat, or ANY other bash command to mani

### `script/translate-app.md` — score 5
Reason: matched: are, commands, file, shell
Preview: Translate the product app locale `$1` from the English source dictionaries. English is the read-only source of truth. Its copy is intentional and must never be modified, rewritten, or "improved." The translation request below contains the l

### `specs/v2/config.md` — score 5
Reason: matched: are, commands, file, shell
Preview: # V2 Config Review This document breaks the legacy configuration schema into small review groups. Work through one group at a time and decide whether each field should be ported as-is, removed, or redesigned for v2. ## Status Labels - `pend

### `specs/v2/schema-changelog.md` — score 5
Reason: matched: approved, are, file, shell
Preview: # V2 Schema Changelog ## 2026-06-26: Add Finite Session History - Add `GET /api/session/:sessionID/history` and generated Promise, Effect, and legacy JavaScript client methods. - Page public durable Session events after an optional exclusiv

### `specs/v2/todo.md` — score 5
Reason: matched: are, commands, file, shell
Preview: # TODO ok we need to work towards a launch of v2 so we can get out of this rebuild phase ## Post-Hono cleanup - Kit The opencode server has moved to the Effect HttpApi backend. Remaining work is mostly cleanup: delete compatibility shims, s

### `.opencode/agent/triage.md` — score 4
Reason: matched: are, file, shell
Preview: --- mode: primary hidden: true model: opencode/gpt-6-luna color: "#44BA81" tools: "*": false "github-triage": true --- You are a triage agent responsible for triaging github issues. Use your github-triage tool to triage issues. This file is

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `.opencode/agent/triage.md`

### Scout: Compare documentation and configuration with the implementation.
- `README.md`
- `specs/v2/config.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/codex.txt`
- `packages/opencode/src/session/prompt/gpt.txt`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `packages/opencode/src/session/prompt/gemini.txt`
- `packages/opencode/src/session/prompt/gpt-astra.txt`
- `.github/workflows/docs-locale-sync.yml`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
