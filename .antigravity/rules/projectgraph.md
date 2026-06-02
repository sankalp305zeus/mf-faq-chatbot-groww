# ProjectGraph OS — Antigravity Rules
# MF FAQ Chatbot | Groww | HDFC Mutual Fund

<!-- Antigravity reads this file automatically from .antigravity/rules/ -->

## Files to load

**Every session:**
- `.projectgraph/CONTEXT.md`
- `.projectgraph/CONVENTIONS.md`

**Complex tasks:**
- `.projectgraph/STATE.md`
- `.projectgraph/RESEARCH.md` (Active section only)

**Architecture or data decisions:**
- `.projectgraph/log/` — 3 most recent files

**Never load:**
- `.projectgraph/CAPTURE.md` — unprocessed inbox, not reliable context

## Behaviour rules

- Follow all conventions in `CONVENTIONS.md` exactly.
- This is a facts-only chatbot — never give investment advice or recommendations.
- Return `[DATA MISSING]` for any scheme data not found in `data/` or `sample-qa/`.
- Treat anything under `CONTEXT.md` "Assumptions" as unvalidated — say so when relevant.
- Before proposing new scheme categories or data formats, check `log/` for prior decisions.
- If `STATE.md` shows any file unreviewed >30 days, flag it.
- When `RESEARCH.md` entries have `Status: stale`, treat them with skepticism and say so.
