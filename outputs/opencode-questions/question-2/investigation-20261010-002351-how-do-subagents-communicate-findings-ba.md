# Repository Investigation Report

**Question:** How do subagents communicate findings back to the main agent?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 46248 tokens
- Estimated reduction: 99.6%

## Evidence selected

### `packages/opencode/src/session/prompt/gpt-astra.txt` — score 5
Reason: matched: agent, back, main, subagents
Preview: You are an AI agent powered by OpenCode, a coding agent harness. Help the user accomplish their goals using the tools you have available. # Harness - Responses are rendered as GitHub-flavored Markdown. - `<system-reminder>` blocks are harne

### `packages/opencode/src/session/prompt/meta.txt` — score 5
Reason: matched: agent, communicate, findings, subagents
Preview: You are OpenCode, a coding agent that helps users with software engineering tasks. You are powered by {{MODEL_NAME}}, a large language model trained by Meta MSL. Use the instructions below and the tools available to assist the user. # Commu

### `packages/opencode/src/session/prompt/beast.txt` — score 4
Reason: matched: agent, back, communicate
Preview: You are opencode, an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Your thinking should be thorough and so it's fine if it's very long. However, avoid unneces

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 4
Reason: matched: agent, back, communicate
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `specs/tui-package.md` — score 4
Reason: matched: agent, back, main
Preview: # TUI Package Extraction ## Goal Move the canonical OpenCode terminal application from `packages/opencode/src/cli/cmd/tui` into a self-contained workspace package while the legacy CLI and the new CLI continue to use the same implementation.

### `.github/workflows/docs-locale-sync.yml` — score 3
Reason: matched: agent, subagents
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.opencode/command/ai-deps.md` — score 3
Reason: matched: findings, subagents
Preview: --- description: "Bump AI sdk dependencies minor / patch versions only" --- Please read @package.json and @packages/opencode/package.json. Your job is to look into AI SDK dependencies, figure out if they have versions that can be upgraded (

### `AGENTS.md` — score 3
Reason: matched: agent, main
Preview: - To regenerate the legacy JavaScript SDK, run `./packages/sdk/js/script/build.ts`. - After changing the public Protocol or Server `HttpApi`, run `bun run generate` from `packages/client`. Do not edit `src/generated` or `src/generated-effec

### `SECURITY.md` — score 3
Reason: matched: agent, findings
Preview: # Security ## IMPORTANT We do not accept AI generated security reports. We receive a large number of these and we absolutely do not have the resources to review them all. If you submit one that will be an automatic ban from the project. ## 

### `github/action.yml` — score 3
Reason: matched: agent, back
Preview: name: "opencode GitHub Action" description: "Run opencode in GitHub Actions workflows" branding: icon: "code" color: "orange" inputs: model: description: "Model to use" required: true agent: description: "Agent to use. Must be a primary age

### `packages/app/src/i18n/en.ts` — score 3
Reason: matched: agent, back, main
Preview: import { DESKTOP_NATIVE_ENGLISH } from "./desktop-native" export const dict = { ...DESKTOP_NATIVE_ENGLISH, "command.category.suggested": "Suggested", "command.category.view": "View", "command.category.project": "Project", "command.category.

### `packages/app/src/i18n/lv.ts` — score 3
Reason: matched: agent, back, main
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Fails", "desktop.menu.edit": "Rediģēt", "desktop.menu.view": "Skats", "desktop.menu.go": "Iet", "desktop.menu.window": "Logs", "desktop.menu.help": "Palīdzība", "de

### `packages/codemode/codemode.md` — score 3
Reason: matched: agent, findings
Preview: # CodeMode Design and Status This is the living design and status document for `@opencode-ai/codemode` and its existing V2 OpenCode adapter. It records current behavior, intentional boundaries, durable rationale, and material remaining work

### `packages/core/src/plugin/agent.ts` — score 3
Reason: matched: agent, findings, main
Preview: export * as AgentPlugin from "./agent" import path from "path" import { define } from "./internal" import { Effect } from "effect" import { AgentV2 } from "../agent" import { Global } from "../global" import { Location } from "../location" 

### `packages/core/src/plugin/command/review.txt` — score 3
Reason: matched: agent, communicate
Preview: You are a code reviewer. Your job is to review code changes and provide actionable feedback. --- Input: $ARGUMENTS --- ## Determining What to Review Based on the input provided, determine which type of review to perform: 1. **No arguments (

### `packages/core/src/plugin/skill/customize-opencode.md` — score 3
Reason: matched: agent, main
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/core/src/v1/config/config.ts` — score 3
Reason: matched: agent, back, subagents
Preview: export * as ConfigV1 from "./config" import { Schema } from "effect" import { NonNegativeInt, PositiveInt, type DeepMutable } from "../../schema" import { ConfigExperimental } from "../../config/experimental" import { ConfigReference } from

### `packages/opencode/specs/effect/facades.md` — score 3
Reason: matched: agent, back
Preview: # Facade removal checklist Concrete inventory of the remaining `makeRuntime(...)`-backed facades in `packages/opencode`. Current status on this branch: - `src/` has 5 `makeRuntime(...)` call sites total. - 2 are intentionally excluded from 

### `packages/opencode/specs/tui-plugins.md` — score 3
Reason: matched: back, main
Preview: # TUI plugins Technical reference for the current TUI plugin system. ## Overview - TUI plugin config lives in `tui.json`. - Author package entrypoint is `@opencode-ai/plugin/tui`. - Internal plugins load inside the CLI app the same way exte

### `packages/opencode/src/agent/prompt/explore.txt` — score 3
Reason: matched: agent, findings
Preview: You are a file search specialist. You excel at thoroughly navigating and exploring codebases. Your strengths: - Rapidly finding files using glob patterns - Searching code and text with powerful regex patterns - Reading and analyzing file co

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `.opencode/command/ai-deps.md`
- `packages/core/src/plugin/agent.ts`
- `packages/core/src/plugin/command/review.txt`
- `packages/opencode/src/agent/prompt/explore.txt`

### Scout: Compare documentation and configuration with the implementation.
- `packages/core/src/v1/config/config.ts`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/gpt-astra.txt`
- `packages/opencode/src/session/prompt/meta.txt`
- `packages/opencode/src/session/prompt/beast.txt`
- `packages/opencode/src/session/prompt/copilot-gpt-5.txt`
- `specs/tui-package.md`
- `.github/workflows/docs-locale-sync.yml`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
