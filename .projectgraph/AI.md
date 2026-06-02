# AI Tool Integration

<!-- Copy the block for your tool into its native config. -->
<!-- CONVENTIONS.md is the rule source of truth — do not duplicate rules here. -->

## Reading order

| When | Files to load |
|---|---|
| Every session | `CONTEXT.md` + `CONVENTIONS.md` |
| Complex tasks | + `STATE.md` + `RESEARCH.md` (Active only) |
| Arch / data decisions | + last 3 files in `log/` |
| Never auto-load | `CAPTURE.md` — unprocessed inbox |

---

## Claude — claude.ai Projects

Paste into **Project Instructions**:

```
Before every response, read .projectgraph/CONTEXT.md and .projectgraph/CONVENTIONS.md.
This is a facts-only mutual fund FAQ chatbot for HDFC MF schemes on Groww.
Never give investment advice. Never fabricate scheme data — return [DATA MISSING] instead.
Treat anything under CONTEXT.md "Assumptions" as unvalidated.
Never use .projectgraph/CAPTURE.md as context.
```

---

## Claude Code

Add to `CLAUDE.md` at project root:

```
@file .projectgraph/CONTEXT.md
@file .projectgraph/CONVENTIONS.md

Follow all conventions in CONVENTIONS.md exactly.
For data or architecture decisions, check .projectgraph/log/ before proposing changes.
Treat CONTEXT.md "Assumptions" as unvalidated.
```

---

## Cursor

`.cursor/rules/projectgraph.mdc` is already configured in this repo. No action needed.

---

## Antigravity

`.antigravity/rules/projectgraph.md` is already configured in this repo. No action needed.

---

## ChatGPT

**Option A — Custom Instructions:**
```
I am building a facts-only FAQ chatbot for HDFC Mutual Fund schemes on Groww.
When I share CONTEXT.md, treat it as authoritative. Never give investment advice.
Treat "Assumptions" sections as unvalidated beliefs, not confirmed facts.
```

**Option B — Per session:** Upload `CONTEXT.md` + `CONVENTIONS.md` at session start.

---

## Gemini

Load core files at session start, then open with:
```
I've attached my project context files. Read them before responding.
This is a facts-only MF FAQ chatbot. Never give investment advice.
Treat "Assumptions" as unvalidated.
```
