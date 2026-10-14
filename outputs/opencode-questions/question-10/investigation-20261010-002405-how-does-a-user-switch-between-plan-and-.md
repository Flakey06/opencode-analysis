# Repository Investigation Report

**Question:** How does a user switch between Plan and Build modes?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 50555 tokens
- Estimated reduction: 99.5%

## Evidence selected

### `README.md` — score 6
Reason: matched: between, build, plan, switch, user
Preview: <p align="center"> <a href="https://opencode.ai"> <picture> <source srcset="packages/console/app/src/asset/logo-ornate-dark.svg" media="(prefers-color-scheme: dark)"> <source srcset="packages/console/app/src/asset/logo-ornate-light.svg" med

### `packages/opencode/src/session/prompt/meta.txt` — score 6
Reason: matched: between, build, plan, switch, user
Preview: You are OpenCode, a coding agent that helps users with software engineering tasks. You are powered by {{MODEL_NAME}}, a large language model trained by Meta MSL. Use the instructions below and the tools available to assist the user. # Commu

### `packages/opencode/src/session/prompt/anthropic.txt` — score 5
Reason: matched: between, build, plan, user
Preview: You are OpenCode, the best coding agent on the planet. You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user. IMPORTANT: You must NEVER

### `packages/opencode/src/tool/plan-exit.txt` — score 5
Reason: matched: build, plan, switch, user
Preview: Use this tool when you have completed the planning phase and are ready to exit plan agent. This tool will ask the user if they want to switch to build agent to start implementing the plan. Call this tool: - After you have written a complete

### `packages/plugin/src/v2/effect/PLAN.md` — score 5
Reason: matched: between, build, plan, user
Preview: # V2 Plugin System Implementation Plan ## Status This document describes the agreed target design for the V2 plugin system. It is an implementation plan, not documentation for the current API. ## Goals - Internal and external plugins use th

### `packages/tui/src/feature-plugins/home/tips-view.tsx` — score 5
Reason: matched: between, build, modes, plan, switch
Preview: import type { TuiPluginApi } from "@opencode-ai/plugin/tui" import { createMemo, For, type Accessor } from "solid-js" import { DEFAULT_THEMES, useTheme } from "../../context/theme" import { useCommandShortcut } from "../../keymap" const the

### `packages/core/src/plugin/skill/customize-opencode.md` — score 4
Reason: matched: build, plan, user
Preview: <!-- Built-in skill. Name and description are registered in code at packages/core/src/plugin/skill.ts and CUSTOMIZE_OPENCODE_SKILL_DESCRIPTION). The body below becomes the skill's content. --> # Customizing opencode opencode validates its o

### `packages/core/test/session-create.test.ts` — score 4
Reason: matched: build, plan, switch, user
Preview: import { describe, expect } from "bun:test" import path from "path" import { Effect, Layer, Stream } from "effect" import { AgentV2 } from "@opencode-ai/core/agent" import { asc, eq } from "drizzle-orm" import { Database } from "@opencode-a

### `packages/llm/DESIGN.md` — score 4
Reason: matched: between, switch, user
Preview: # AI Library Design > Discussion draft. This document describes the intended replacement for the > current private `@opencode-ai/llm` API. Names and exact TypeScript signatures > are illustrative until implementation, but the domain boundar

### `packages/opencode/specs/effect/error-boundaries-plan.md` — score 4
Reason: matched: build, plan, user
Preview: # Error Boundaries Plan Plan for removing `NamedError` as connective tissue while keeping public wire contracts stable. ## Desired Shape ```text Domain/service error Schema.TaggedErrorClass - catchable with catchTag / catchTags - appears in

### `packages/opencode/src/session/prompt/copilot-gpt-5.txt` — score 4
Reason: matched: build, plan, user
Preview: You are an expert AI programming assistant Your name is opencode Keep your answers short and impersonal. <gptAgentInstructions> You are a highly sophisticated coding agent with expert-level knowledge across programming languages and framewo

### `packages/opencode/src/session/prompt/gemini.txt` — score 4
Reason: matched: build, plan, user
Preview: You are opencode, an interactive CLI agent specializing in software engineering tasks. Your primary goal is to help users safely and efficiently, adhering strictly to the following instructions and utilizing your available tools. # Core Man

### `packages/opencode/src/session/prompt/gpt.txt` — score 4
Reason: matched: build, plan, user
Preview: You are OpenCode, You and the user share the same workspace and collaborate to achieve the user's goals. You are a deeply pragmatic, effective software engineer. You take engineering quality seriously, and collaboration comes through as dir

### `packages/opencode/src/session/prompt/kimi.txt` — score 4
Reason: matched: build, plan, user
Preview: You are OpenCode, an interactive general AI agent running on a user's computer. Your primary goal is to help users with software engineering tasks by taking action — use the tools available to you to make real changes on the user's system. 

### `packages/opencode/src/session/prompt/plan-mode.txt` — score 4
Reason: matched: build, plan, user
Preview: <system-reminder> Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tools (including changing configs 

### `packages/opencode/src/session/prompt/plan-reminder-anthropic.txt` — score 4
Reason: matched: build, plan, user
Preview: <system-reminder> # Plan Mode - System Reminder Plan mode is active. The user indicated that they do not want you to execute yet -- you MUST NOT make any edits (with the exception of the plan file mentioned below), run any non-readonly tool

### `packages/opencode/src/tool/plan-enter.txt` — score 4
Reason: matched: plan, switch, user
Preview: Use this tool to suggest switching to plan agent when the user's request would benefit from planning before implementation. If they explicitly mention wanting to create a plan ALWAYS call this tool first. This tool will ask the user if they

### `packages/opencode/src/tool/plan.ts` — score 4
Reason: matched: build, plan, switch, user
Preview: import path from "path" import { SessionV1 } from "@opencode-ai/core/v1/session" import { Effect, Schema } from "effect" import * as Tool from "./tool" import { Question } from "../question" import { Session } from "@/session/session" impor

### `packages/opencode/test/cli/run/session-replay.test.ts` — score 4
Reason: matched: between, build, plan, user
Preview: import { describe, expect, test } from "bun:test" import { replayLocalRows, replaySession } from "@/cli/cmd/run/session-replay" import type { SessionMessages } from "@/cli/cmd/run/session.shared" import type { RunProvider } from "@/cli/cmd/

### `packages/session-ui/src/components/timeline-playground.stories.tsx` — score 4
Reason: matched: between, build, plan, user
Preview: // @ts-nocheck import { createSignal, createMemo, createEffect, on, For, Show, batch } from "solid-js" import { createStore, produce } from "solid-js/store" import type { Message, UserMessage, AssistantMessage, Part, TextPart, ReasoningPart

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/opencode/src/tool/plan-exit.txt`
- `packages/opencode/src/tool/plan-enter.txt`
- `packages/opencode/src/tool/plan.ts`

### Scout: Compare documentation and configuration with the implementation.
- `README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `packages/opencode/src/session/prompt/meta.txt`
- `packages/opencode/src/session/prompt/anthropic.txt`
- `packages/plugin/src/v2/effect/PLAN.md`
- `packages/tui/src/feature-plugins/home/tips-view.tsx`
- `packages/core/src/plugin/skill/customize-opencode.md`
- `packages/core/test/session-create.test.ts`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
