---
name: continue

description: Restores project context by reading the active session log and recent technical history. Use when starting a new session, when the user asks "where were we?", or "continue". Automatically reads logs/CURRENT_SESSION.md and recent logs/history/ files to restore project state and detect any outstanding issues or blockers.

---

# Continue Skill (Universal Context Restoration)

This skill recovers project memory by reading the `logs/` directory. It connects the current session with the "live" state of the work and analyzes whether the previous session ended in success (finding) or a blocker (problem) [1, 2].

## Purpose

**Problem:** When restarting the agent, operational memory is lost about which build error was pending, which Logseq query failed, or which refactoring was left incomplete [3].

**Solution:** Read `logs/CURRENT_SESSION.md` for immediate state and consult `logs/history/` for recent technical context.

## When to Use

1. At the start of any interaction (Auto-start recommended in `AGENTS.md`).

2. When the user says "Continue", "Summary", or "What's next?".

3. If you need to remember the last technical solution applied to the project configuration (whether `config.edn`, `package.json`, or `docker-compose.yml`) [3].

## Execution Flow

Follow these steps strictly using the `bash` and `read` tools:

### Step 1: Verify Logs Existence

Verify that project logs exist.

```bash
ls -F logs/
```

*If logs/ doesn't exist, assume it's a new project and suggest starting configuration.*

### Step 2: Read "Live" State

Read the mutable file we left in the previous session. **Tool:** read on logs/CURRENT_SESSION.md. **Goal:** Extract the "Current Objective" and "Next Steps".

### Step 3: Reconnaissance (Recent Context)

Search for recent technical intelligence by checking last 2 generated files in history and for active plans [4, 5].

```bash
ls -t logs/history/ | head -n 2
ls -t logs/plans/ 2>/dev/null | head -n 2 || echo "No plans found"
```

If filename suggests immediate relevance (has a recent date), **READ IT** using read.

- **If you see ..._problems.md:** It is CRITICAL to read it. It means there was an error (bug, broken query, crash) that we must resolve before proceeding [6, 7].
- **If you see ..._findings.md:** Read it to understand what new capability or configuration was recently enabled [2, 8].
- **If you see ..._plan_*.md:** Read it to understand active work plans and their status.

### Step 4: Adaptive Executive Summary

Generate a structured response based on project type detected in the logs:

- **Project State:** Summary of CURRENT_SESSION.md.
- **Technical Context:**
  - *If it's code:* Mention affected files or pending build errors.
  - *If it's Logseq:* Mention query status, templates, or graph integrity (config.edn).
- **Active Plans:** If there are plans in `approved` or `in_progress` status, summarize and propose continuing execution.
- **Alert (If applicable):** *"Note: The last session recorded a problem in [File]. I suggest starting there."*
- **Proposal:** Logical next step.

## Example Generic Response

"I've restored the context. **Current State:** We were working on [Objective]. **Recent Context:** I detected a problem record (..._problems.md) related to [Component/Query]. **Plan:** Review the solution proposed in the log and continue with task B."

---

### Integration in `AGENTS.md`

To close the cycle with `2_saver.md`, update your `.opencode/AGENTS.md` (or `~/.config/opencode/AGENTS.md`) with this continuity protocol. This ensures the agent uses the skill automatically [9, 10].

```markdown
# Continuity Protocol (Memory)

## 1. Session Startup (Boot Sequence)

Your first action upon receiving ANY task should be to verify project memory:

1.  Check if `logs/CURRENT_SESSION.md` exists.

2.  If it exists, invoke the `continue` skill (or use `read` manually) IMMEDIATELY. Do not wait for user instruction.

3.  Your goal is to "load the mental graph" of the project before writing code or suggesting changes.

## 2. Project Adaptability

- If upon reading logs you detect Logseq files (`config.edn`, `pages/`), assume the role of **Knowledge Manager**.

- If you detect source code (`src/`, `package.json`, `pyproject.toml`), assume the role of **Software Engineer**.

- If the `continue` skill reports a recent `_problems.md`, your absolute priority is to verify if that problem still exists.
