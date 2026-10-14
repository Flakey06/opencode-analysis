# Repository Investigation Report

**Question:** How are agent actions shown to the user?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 44248 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `README.md` — score 5
Reason: matched: actions, agent, are, user
Preview: <p align="center"> <a href="https://opencode.ai"> <picture> <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)"> <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" med

### `SECURITY.md` — score 5
Reason: matched: actions, agent, are, user
Preview: # Security ## IMPORTANT We do not accept AI generated security reports. We receive a large number of these and we absolutely do not have the resources to review them all. If you submit one that will be an automatic ban from the project. ## 

### `packages/core/src/plugin/skill/customize-opencode.md` — score 5
Reason: matched: actions, agent, are, user
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/opencode/src/session/prompt/anthropic.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/session/prompt/codex.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. ## Editing constraints - 

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `packages/opencode/src/session/prompt/gemini.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/opencode/src/session/prompt/kimi.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/plan-mode.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: <system-reminder> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs 

### `packages/opencode/src/session/prompt/plan-reminder-anthropic.txt` — score 5
Reason: matched: actions, agent, are, user
Preview: <system-reminder> # Plan Mode - System Reminder Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tool

### `specs/v2/session.md` — score 5
Reason: matched: agent, are, shown, user
Preview: # Session API ## Current V2 Core Slice The Effect-native core facade treats prompt recording and execution as separate responsibilities: ```text sessions.create({ id?, location, ... }) -> omitted ID generates one internal Session ID -> supp

### `.github/workflows/docs-locale-sync.yml` — score 4
Reason: matched: actions, agent, are
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.github/workflows/docs-update.yml` — score 4
Reason: matched: actions, agent, are
Preview: name: docs-update on: schedule: - cron: "0 */12 * * *" workflow_dispatch: env: LOOKBACK_HOURS: 4 jobs: update-docs: if: github.repository == 'sst/opencode' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: id-token: write contents: write p

### `.github/workflows/duplicate-issues.yml` — score 4
Reason: matched: actions, are, user
Preview: name: duplicate-issues on: issues: types: [opened, edited] jobs: check-duplicates: if: github.event.action == 'opened' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: 

### `.github/workflows/pr-standards.yml` — score 4
Reason: matched: actions, are, user
Preview: name: pr-standards on: pull_request_target: types: [opened, edited, synchronize] jobs: check-standards: runs-on: ubuntu-latest permissions: contents: read pull-requests: write steps: - name: Check PR standards uses: actions/github-script@f2

### `.github/workflows/triage.yml` — score 4
Reason: matched: actions, agent, user
Preview: name: triage on: issues: types: [opened] jobs: triage: runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5 # v4.3

### `.opencode/command/commit.md` — score 4
Reason: matched: agent, are, user
Preview: --- description: git commit and push model: opencode/kimi-k2.5 subtask: true --- commit and push make sure it includes a prefix like docs: tui: core: ci: ignore: wip: For anything in the packages/web use the docs: prefix. prefer to explain 

### `AGENTS.md` — score 4
Reason: matched: agent, are, user
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `CONTEXT.md` — score 4
Reason: matched: agent, are, user
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `packages/app/create-effect-simplification-spec.md` — score 4
Reason: matched: actions, are, user
Preview: # CreateEffect Simplification Implementation Spec Reduce reactive misuse across `packages/app`. --- ## Context This work targets `packages/app/src`, which currently has 101 `createEffect` calls across 37 files. The biggest clusters are `pag

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `.opencode/command/commit.md`

### Scout: Compare documentation and configuration with the implementation.
- `README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `SECURITY.md`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `packages/opencode/src/session/prompt/anthropic.txt`
- `packages/opencode/src/session/prompt/codex.txt`
- `packages/opencode/src/session/prompt/copilot-gpt-5.txt`
- `packages/opencode/src/session/prompt/gemini.txt`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
