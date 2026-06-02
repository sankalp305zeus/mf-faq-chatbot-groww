# MF FAQ Chatbot — Groww Trial

A facts-only FAQ assistant for HDFC Mutual Fund scheme questions, built on the [ProjectGraph-OS](https://github.com/sankalp305zeus/ProjectGraph-OS) framework.

This is a real-world trial project validating ProjectGraph-OS in a live PM + AI workflow.

---

## Problem

Investors on Groww ask the same factual questions repeatedly — NAV, exit load, lock-in period, expense ratio, fund manager. These questions have clear, documented answers. This chatbot finds and returns them without hallucinating or giving advice.

---

## Target user

Retail mutual fund investors on Groww who want a quick, accurate answer about a specific HDFC MF scheme — not a recommendation, not a prediction, just a fact.

---

## Scope

**Platform:** Groww
**AMC:** HDFC Mutual Fund
**Schemes (v1):**
1. HDFC Large Cap Fund *(formerly HDFC Top 100 Fund — renamed Jan 1, 2025)*
2. HDFC Flexi Cap Fund
3. HDFC ELSS Tax Saver Fund
4. HDFC Index Fund — S&P BSE Sensex

**In scope:** NAV, returns, benchmark, expense ratio, exit load, minimum SIP, lock-in, riskometer, fund manager, account statement download, capital gains statement

**Out of scope:** Investment advice, portfolio recommendations, real-time pricing, non-HDFC schemes, schemes not listed above (v1)

---

## Data source policy

- Official public sources only: **hdfcfund.com**, **amfiindia.com**, **sebi.gov.in**
- No blogs, no third-party finance sites, no estimated data
- Every answer cites its source file or URL
- Missing data is returned as `[DATA MISSING]` — never inferred

See [`data/source-list.md`](data/source-list.md) for all verified URLs.

---

## Folder structure

```
mf-faq-chatbot-groww/
├── .projectgraph/
│   ├── CONTEXT.md        # Project identity — AI reads first
│   ├── STATE.md          # Current status and open questions
│   ├── RESEARCH.md       # Findings from source research
│   ├── CONVENTIONS.md    # Rules for AI and humans
│   ├── CAPTURE.md        # Raw inbox — normalize weekly
│   ├── AI.md             # Per-tool setup (Claude, Cursor, ChatGPT, Gemini, Antigravity)
│   └── log/              # One file per decision
├── .cursor/
│   └── rules/
│       └── projectgraph.mdc
├── .antigravity/
│   └── rules/
│       └── projectgraph.md
├── data/
│   └── source-list.md    # Verified official source URLs
├── prototype/            # Chatbot prototype files
├── sample-qa/            # Seed Q&A pairs for testing
├── .gitignore
└── README.md
```

---

## Success criteria

| Criteria | Target |
|---|---|
| Factual accuracy | Answer matches official source exactly |
| Hallucination rate | Zero — [DATA MISSING] if not found |
| Question coverage | 20+ FAQ pairs across 4 schemes |
| Source citation | Every answer cites a URL or file |
| Out-of-scope handling | Consistent refusal message, no guessing |

---

## Disclaimer

This chatbot provides factual information about mutual fund schemes only. It does not provide investment advice, financial recommendations, or predictions of any kind. Always consult a SEBI-registered investment advisor before making investment decisions. Mutual fund investments are subject to market risks.

---

## Built on ProjectGraph-OS

This project uses [ProjectGraph-OS](https://github.com/sankalp305zeus/ProjectGraph-OS) — a structured AI context system for PM and project workflows. All `.projectgraph/`, `.cursor/`, and `.antigravity/` files follow ProjectGraph-OS conventions.

| File | When to update | Committed |
|---|---|---|
| CONTEXT.md | Rarely — identity changes | Yes |
| STATE.md | Each session | Solo: yes. Team: no (gitignored) |
| RESEARCH.md | Per finding | Yes |
| CONVENTIONS.md | Per new rule | Yes |
| CAPTURE.md | Continuously | No (gitignored) |
| AI.md | Per tool change | Yes |
| log/*.md | Per decision | Yes |
