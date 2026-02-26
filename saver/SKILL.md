---
name: saver

description: Saves session state, technical findings, and error solutions to the logs/ directory to maintain project continuity. Use when ending a work session, after resolving complex technical problems, or completing key milestones. Creates logs/CURRENT_SESSION.md for live state and immutable logs/history/YYMMDD_HHMM_findings.md or logs/history/YYMMDD_HHMM_problems.md for historical records.

---

# Saver Skill (Universal Log System)

This skill persists the agent's short-term memory in Markdown files within the `logs/` folder. Its agnostic design allows documenting both the evolution of source code and the maturation of a knowledge graph (Logseq).

## File Structure

We use a flat, event- and time-based structure, adaptable to any workflow:

1. **`logs/CURRENT_SESSION.md`**: The "live" and mutable state. Represents the current snapshot of project.

2. **`logs/history/YYMMDD_HHMM_findings.md`**: Success milestones. (Ex: "Optimized query", "Refactored component", "Defined architecture").

3. **`logs/history/YYMMDD_HHMM_problems.md`**: Blocker and troubleshooting records. (Ex: "Build error", "Conflict in config.edn").

4. **`logs/plans/YYMMDD_HHMM_plan_[slug].md`**: Work plans with lifecycle tracking. (Ex: "categorizacion-correos", "migracion-db").

## When to Use

Execute this skill when:

1. You are about to end a work session.

2. You have resolved a complex technical problem (ex: a recursion bug or an advanced Logseq query that wasn't working).

3. You have completed a key milestone (ex: initial configuration, database migration, folder restructuring).

4. When user requests to create or save a work plan.

5. When the user requests corrections or error fixes that must be preserved as learnings.

## Execution Flow

Follow these steps strictly using the `bash` and `write` tools:

### Step 1: Prepare Directories

Ensure that structure exists. If not, create it:

```bash
mkdir -p logs/history logs/plans
```

### Step 2: Get Timestamp

Get the current date for historical versioning:

```bash
date +"%y%m%d_%H%M"
```

### Step 3: Save Current State (CURRENT_SESSION.md)

Overwrite logs/CURRENT_SESSION.md. This is the entry point for the next agent.

```markdown
# Session State: [Project Name]

**Last Updated**: [DATE_AND_TIME]

## Session Objective

[Brief description: Ex: "Refactor authentication module" or "Configure Logseq templates"]

## Current State

- [x] [Completed task A]

- [x] [Completed task B]

- [ ] [Pending/Blocked task]

## Critical Technical Context

[Vital information for the next agent. Ex: "Server runs on port 3000", "Don't touch custom.css for now", "API returns 404 on /login"]

## Next Steps

1. [Immediate concrete action]
```

### Step 4: Generate History (Only if applicable)

If events worth remembering occurred, create immutable files in logs/history/ using the timestamp from Step 2.

#### A. If there were Findings/Successes (..._findings.md)

Use it to document how something you just implemented works.
**Path:** logs/history/[TIMESTAMP]_findings.md

```markdown
# Technical Finding / Milestone

**Context**: [Ex: Database Configuration / Advanced Logseq Queries]

## The Discovery

[Technical explanation. Ex: "For the query to work, you must use syntax X" or "The React hook needed dependency Y"]

## Key Files Affected

- `src/...` or `logseq/...`
```

#### B. If there were Resolved Problems or Corrections (..._problems.md)

Use it to prevent the future agent from making same error and to capture user-requested corrections and learnings.
**Path:** logs/history/[TIMESTAMP]_problems.md

```markdown
# Problem Record (Troubleshooting)

**Severity**: [Low/Medium/High]

## The Problem

[Description of error, stack trace, or unexpected behavior of graph]

## User-Requested Corrections

[List the exact corrections the user asked for]

## The Solution / Workaround

[Exact steps that solved problem]

## Learnings to Preserve

[Concrete lessons or rules to apply in future sessions]
```

#### C. If a Plan was created or updated (..._plan_*.md)

Use to document multi-phase work plans with lifecycle tracking.
**Path:** logs/plans/[TIMESTAMP]_plan_[slug].md

```markdown
# Plan: [Título Descriptivo]

**Created**: YYYY-MM-DD HH:MM
**Updated**: YYYY-MM-DD HH:MM
**Status**: draft | approved | in_progress | completed | cancelled
**Slug**: [slug-corto]

## Objetivo

[Descripción concisa del objetivo]

## Fases

### Fase 1: [Nombre]

| # | Archivo | Acción | Notas |
|---|---------|--------|-------|
| 1.1 | path/file.md | Crear/Modificar | Descripción |

## Log de Ejecución

- [ ] Fase 1 iniciada
- [ ] Fase 1 completada
```

### Step 5: Confirmation

Inform the user:

"Context saved in CURRENT_SESSION.md. If applicable: Historical findings/problems records were generated."

---

### Adjustment in Integration (`AGENTS.md`)

For this generalization to work, update your `.opencode/AGENTS.md`. The key change here is to instruct the agent to look for **patterns** in the logs, regardless of whether it's code or text.

```markdown
# Universal Memory Protocol

## 1. Startup (Boot Sequence)

Your first action upon starting any task is to verify project memory:

1.  Check if `logs/CURRENT_SESSION.md` exists.

2.  If it exists, use `read` to load it.

3.  If the task involves continuing complex technical work, review the last files in `logs/history/` to see if there were recent "problems" to avoid.

## 2. Persistence

Use the `saver` skill upon finishing important milestones.

- If you're in a code project: Document architecture or dependency changes.

- If you're in Logseq/Obsidian: Document query, template, or data structure changes.

### Why this works for both worlds?

1. **Abstraction of "Affected Files":** In Step 4A, when asking for "Key Files", this applies equally to src/components/Button.tsx (React) as to logseq/config.edn (Logseq) [1].
2. **Finding vs Problem Dichotomy:** This separation [2, 3] is universal in engineering. In Logseq, a "problem" is usually a query that doesn't render or a sync conflict; in traditional code, it's a compilation error. The structure handles both without changing the format.
3. **"Live" State:** The CURRENT_SESSION.md [2, 4] acts as a "temporary README" that's useful both for knowing which git branch you're working on and for knowing which section of the graph you were editing.
