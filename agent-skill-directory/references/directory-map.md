# Directory Map for Agent Skills

This file condenses the locations listed in skill_directory.md. Paths are workspace-relative unless noted.

## Workspace / Project Scope
| Path | Agents | Notes |
| --- | --- | --- |
| .agents/skills/<skill>/ | Codex, Gemini CLI, OpenCode | Default shared directory; Codex and Gemini CLI walk up from current working dir.
| .agent/skills/<skill>/ | Antigravity | Singular directory name; must exist in each workspace where Antigravity runs.
| .claude/skills/<skill>/ | Claude Code, OpenCode | Claude Code recursively scans nested subfolders (e.g., apps/frontend/.claude/skills/).
| .opencode/skills/<skill>/ | OpenCode | Native OpenCode path; still honors .agents/skills but keep this when OpenCode-only team members export workspace snapshots.
| .gemini/skills/<skill>/ | Gemini CLI | Exclusive Gemini CLI directory; recommended when shipping artifacts to Gemini-only runners.

## Home / Global Scope
| Path | Agents | Notes |
| ~/.agents/skills/<skill>/ | Codex, Gemini CLI, OpenCode | Widest coverage from a single copy; good default when you control the workstation.
| ~/.claude/skills/<skill>/ | Claude Code, OpenCode | Needed for Claude Code desktop; OpenCode also reads it.
| ~/.gemini/skills/<skill>/ | Gemini CLI | Use together with workspace-level .gemini when CLI configs are user scoped.
| ~/.gemini/antigravity/skills/<skill>/ | Antigravity | Only way to expose skills globally to Antigravity.
| ~/.config/opencode/skills/<skill>/ | OpenCode | CLI-specific path for OpenCode when not inside a repo.

## System & Extension Scope
| Path | Agents | Notes |
| /etc/codex/skills/<skill>/ | Codex | Shared machine-wide skills for codexd or CI boxes.
| <plugin>/skills/<skill>/ | Claude Code | Skills bundled with Claude Code extensions or plugins.

## Agent Discovery Behaviors
- Codex searches .agents/skills/, ~/.agents/skills/, then /etc/codex/skills/ while walking up directories.
- Gemini CLI checks .gemini/skills/ and ~/.gemini/skills/ plus the .agents mirrors for compatibility.
- OpenCode reads .opencode/skills/, ~/.config/opencode/skills/, and piggybacks on .agents/skills/ plus Claude directories.
- Claude Code restricts discovery to .claude/skills/ (workspace or nested) and ~/.claude/skills/ unless a plugin bundles more.
- Antigravity expects .agent/skills/ in workspaces and ~/.gemini/antigravity/skills/ globally.

## Placement Strategy Tips
1. Need broadest coverage on a shared machine: copy skills into both ~/.agents/skills/ and ~/.claude/skills/; symlink ~/.gemini/antigravity/skills/ when Antigravity is in scope.
2. Project-only rollout: add the skill under .agents/skills/ plus whichever agent-specific folders your teammates actually use.
3. Keep each skill folder identical across locations; version-control the workspace copy and document how to sync the rest.
