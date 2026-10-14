# Repository Investigation Report

**Question:** How does OpenCode search and select files?

## Context comparison

- Candidate files: 3950
- Focused files: 20
- Broad estimate: 10314702 tokens
- Focused estimate: 61676 tokens
- Estimated reduction: 99.4%

## Evidence selected

### `packages/opencode/src/tool/task.txt` — score 5
Reason: matched: files, opencode, search, select
Preview: Launch a new agent to handle complex, multistep tasks autonomously. When using the Task tool, you must specify a subagent_type parameter to select which agent type to use. When NOT to use the Task tool: - If you want to read a specific file

### `.github/workflows/docs-locale-sync.yml` — score 4
Reason: matched: files, opencode, search
Preview: name: docs-locale-sync on: push: branches: - dev paths: - packages/web/src/content/docs/*.mdx jobs: sync-locales: if: false #if: github.actor != 'opencode-agent[bot]' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: write steps:

### `.github/workflows/duplicate-issues.yml` — score 4
Reason: matched: opencode, search, select
Preview: name: duplicate-issues on: issues: types: [opened, edited] jobs: check-duplicates: if: github.event.action == 'opened' runs-on: blacksmith-4vcpu-ubuntu-2404 permissions: contents: read issues: write steps: - name: Checkout repository uses: 

### `.opencode/skills/effect/SKILL.md` — score 4
Reason: matched: files, opencode, search
Preview: --- name: effect description: Work with Effect v4 / effect-smol TypeScript code in this repo --- # Effect This codebase uses Effect for typed, composable TypeScript services, schemas, and workflows. ## Source Of Truth Use the current Effect

### `CONTEXT.md` — score 4
Reason: matched: files, opencode, select
Preview: # OpenCode Session Runtime OpenCode sessions preserve durable conversational history while assembling the runtime context an agent needs to act correctly in its current environment. ## Language **System Context**: The structured collection 

### `github/README.md` — score 4
Reason: matched: files, opencode, select
Preview: # opencode GitHub Action A GitHub Action that integrates [opencode](https://opencode.ai) directly into your GitHub workflow. Mention `/opencode` in your comment, and opencode will execute tasks within your GitHub Actions runner. ## Features

### `packages/app/src/components/command-palette.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: import { getFilename } from "@opencode-ai/core/util/path" import type { Project } from "@opencode-ai/sdk/v2/client" import type { SessionInfo } from "@opencode-ai/client/promise" import { useDialog } from "@opencode-ai/ui/context/dialog" im

### `packages/app/src/components/dialog-command-palette-v2.tsx` — score 4
Reason: matched: files, opencode, search, select
Preview: import { getDirectory, getFilename } from "@opencode-ai/core/util/path" import { FileIcon } from "@opencode-ai/ui/file-icon" import { ScrollView } from "@opencode-ai/ui/scroll-view" import { Dialog, DialogBody } from "@opencode-ai/ui/v2/dia

### `packages/app/src/components/dialog-select-file.tsx` — score 4
Reason: matched: files, opencode, search, select
Preview: import { Dialog } from "@opencode-ai/ui/dialog" import { FileIcon } from "@opencode-ai/ui/file-icon" import { Icon } from "@opencode-ai/ui/icon" import { Keybind } from "@opencode-ai/ui/keybind" import { List } from "@opencode-ai/ui/list" i

### `packages/app/src/i18n/am.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "ፋይል", "desktop.menu.edit": "አርትዕ", "desktop.menu.view": "እይታ", "desktop.menu.go": "ሂድ", "desktop.menu.window": "መስኮት", "desktop.menu.help": "እገዛ", "desktop.menu.che

### `packages/app/src/i18n/ar.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "ملف", "desktop.menu.edit": "تحرير", "desktop.menu.view": "عرض", "desktop.menu.go": "انتقال", "desktop.menu.window": "نافذة", "desktop.menu.help": "مساعدة", "desktop

### `packages/app/src/i18n/az.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Fayl", "desktop.menu.edit": "Redaktə", "desktop.menu.view": "Görünüş", "desktop.menu.go": "Keçid", "desktop.menu.window": "Pəncərə", "desktop.menu.help": "Kömək", "

### `packages/app/src/i18n/bg.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Файл", "desktop.menu.edit": "Редактиране", "desktop.menu.view": "Преглед", "desktop.menu.go": "върви", "desktop.menu.window": "прозорец", "desktop.menu.help": "Помо

### `packages/app/src/i18n/bn.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict: Record<string, string> = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "ফাইল", "desktop.menu.edit": "সম্পাদনা করুন", "desktop.menu.view": "দেখুন", "desktop.menu.go": "যাও", "desktop.menu.window": "জানালা", "deskt

### `packages/app/src/i18n/br.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Arquivo", "desktop.menu.edit": "Editar", "desktop.menu.view": "Visualizar", "desktop.menu.go": "Ir", "desktop.menu.window": "Janela", "desktop.menu.help": "Ajuda", 

### `packages/app/src/i18n/bs.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Datoteka", "desktop.menu.edit": "Uredi", "desktop.menu.view": "Prikaz", "desktop.menu.go": "Idi", "desktop.menu.window": "Prozor", "desktop.menu.help": "Pomoć", "de

### `packages/app/src/i18n/ca.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Fitxer", "desktop.menu.edit": "Edita", "desktop.menu.view": "Veure", "desktop.menu.go": "Vés", "desktop.menu.window": "Finestra", "desktop.menu.help": "Ajuda", "des

### `packages/app/src/i18n/cs.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "desktop.menu.app": "OpenCode", "desktop.menu.file": "Soubor", "desktop.menu.edit": "Upravit", "desktop.menu.view": "Zobrazit", "desktop.menu.go": "Jdi", "desktop.menu.window": "okno", "desktop.menu.help": "Pomoc", "de

### `packages/app/src/i18n/da.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: export const dict = { "command.category.suggested": "Foreslået", "command.category.view": "Vis", "command.category.project": "Projekt", "command.category.provider": "Udbyder", "command.category.server": "Server", "command.category.session":

### `packages/app/src/i18n/de.ts` — score 4
Reason: matched: files, opencode, search, select
Preview: import { dict as en } from "./en" type Keys = keyof typeof en export const dict = { "command.category.suggested": "Vorgeschlagen", "command.category.view": "Ansicht", "command.category.project": "Projekt", "command.category.provider": "Anbi

## Focused roles

### Explore: Trace implementation, agents, tools, commands, and permissions.
- `packages/opencode/src/tool/task.txt`

### Scout: Compare documentation and configuration with the implementation.
- `github/README.md`

### Review: Inspect tests, integrations, APIs, and supporting modules.
- `.github/workflows/docs-locale-sync.yml`
- `.github/workflows/duplicate-issues.yml`
- `.opencode/skills/effect/SKILL.md`
- `CONTEXT.md`
- `packages/app/src/components/command-palette.ts`
- `packages/app/src/components/dialog-command-palette-v2.tsx`

## Boundary of this prototype

This tool selects and explains evidence; it does not call a model or claim to answer the question. The next stage is to give each role its assigned files and compare the resulting findings.
