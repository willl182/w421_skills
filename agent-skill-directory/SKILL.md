---
name: agent-skill-directory
description: Directory map for installing Codex, OpenCode, Gemini CLI, Claude Code, and Antigravity skills. Use when deciding where to place or sync a skill folder at workspace, home, or system scope so every agent detects it.
---

# Agent Skill Directory

## Overview

Use this skill whenever you need to copy or link a skill folder so that multiple agents (Codex, OpenCode, Gemini CLI, Claude Code, Antigravity) can load it. The guidance is distilled from `skill_directory.md` and focuses on picking the right scope, duplicating folders safely, and keeping every copy in sync.

## Quick Start

1. Identify the agents that must see the skill.
2. Choose the deployment scope.
3. Mirror the same skill folder into all required paths.
4. Keep copies synchronized after each update.

Load `references/directory-map.md` for the full path matrix and per-agent behavior.

## Workspace Deployment

Use these paths relative to the repository root:

- `.agents/skills/<skill>/` -> Codex, Gemini CLI, OpenCode default shared path.
- `.agent/skills/<skill>/` -> Antigravity-only path (singular directory name).
- `.claude/skills/<skill>/` -> Claude Code workspace path; OpenCode also reads it.
- `.opencode/skills/<skill>/` -> OpenCode native workspace path.
- `.gemini/skills/<skill>/` -> Gemini CLI native workspace path.

## Home Deployment

Use when skills should be available across all projects for one user:

- `~/.agents/skills/<skill>/` -> Codex, Gemini CLI, OpenCode (best default).
- `~/.claude/skills/<skill>/` -> Claude Code and OpenCode.
- `~/.gemini/skills/<skill>/` -> Gemini CLI.
- `~/.gemini/antigravity/skills/<skill>/` -> Antigravity global path.
- `~/.config/opencode/skills/<skill>/` -> OpenCode global path.

## System and Plugin Deployment

- `/etc/codex/skills/<skill>/` -> machine-wide Codex skills.
- `<plugin>/skills/<skill>/` -> skills bundled by Claude Code plugins.

Treat these as managed snapshots. Update the source copy first, then redeploy.

## Sync Workflow

1. Keep the canonical skill in version control under `.agents/skills/`.
2. Copy or symlink to additional agent-specific paths as required.
3. Re-run validation after edits and before propagation.

## Reference

- Read `references/directory-map.md` before choosing target directories.
