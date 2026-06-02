# Project Context

<!-- AI: read this file first. It is the authoritative project identity. -->
<!-- This project runs on ProjectGraph-OS. All operational rules apply. -->

## Identity
- **Name:** MF FAQ Chatbot — Groww Trial
- **Slug:** mf-faq-chatbot-groww
- **One-liner:** Facts-only FAQ assistant for HDFC MF scheme questions on Groww
- **Product:** Groww
- **AMC:** HDFC Mutual Fund
- **Type:** product + framework validation
- **Stage:** prototype

## Objective
Build a working FAQ chatbot that answers factual questions about HDFC Mutual Fund schemes using only verified official data. Simultaneously validate that ProjectGraph-OS can structure a real PM + AI workflow end-to-end.

## Problem
Investors on Groww ask the same factual questions repeatedly about HDFC MF schemes. These questions have clear, documented answers. The chatbot finds and returns them — no advice, no guessing.

## Current scope

**Platform:** Groww
**AMC:** HDFC Mutual Fund
**Schemes (v1):**
1. HDFC Large Cap Fund *(formerly HDFC Top 100 Fund — renamed Jan 1, 2025)*
2. HDFC Flexi Cap Fund
3. HDFC ELSS Tax Saver Fund
4. HDFC Index Fund — S&P BSE Sensex

**Question categories covered:**
- NAV, returns (1Y / 3Y / 5Y / since inception)
- Benchmark index
- Expense ratio (TER)
- Exit load
- Minimum SIP and lump sum
- Lock-in period (ELSS)
- Riskometer / risk level
- Fund manager name
- Account statement download
- Capital gains statement

## Official source constraints
<!-- AI: only use sources from this list. No exceptions. -->
- **Allowed:** hdfcfund.com · amfiindia.com · sebi.gov.in
- **Not allowed:** Blogs, third-party finance sites, estimated or inferred data
- All verified URLs are in `data/source-list.md`
- Any data not found in official sources → return `[DATA MISSING]`

## Answer format rules
<!-- AI: follow these exactly for every FAQ response. -->
- Answer in 1–3 sentences maximum
- Always cite the source (URL or file name) at the end of the answer
- Never say "I think", "I believe", or "approximately"
- If the question is out of scope, respond: *"This chatbot answers factual questions about HDFC MF schemes only."*
- If data is missing from official sources, respond: *"[DATA MISSING] — this information was not found in the verified source list."*

## Out-of-scope rules
<!-- AI: these are hard stops. Never answer. -->
- Investment advice or recommendations of any kind
- Predictions about future returns or market performance
- Comparison with non-HDFC schemes
- Questions about schemes not in the v1 list above
- Any user personal data — do not store or repeat

## Architecture
- Input: user question (natural language)
- Data: `data/` (scheme facts) + `sample-qa/` (curated Q&A pairs)
- Output: plain-text factual answer with source citation
- No live API calls in prototype phase
- No user data stored

## Next milestones
| Milestone | Status |
|---|---|
| Source collection — verified URL list | ✅ Done (`data/source-list.md`) |
| FAQ rules — answer format and refusal logic | ✅ Done (CONVENTIONS.md + this file) |
| Sample Q&A — 20+ pairs across 4 schemes | 🔲 Next |
| Prototype UI — basic chatbot interface | 🔲 Upcoming |

## Assumptions (unvalidated)
<!-- AI: treat everything here as uncertain, not confirmed fact. -->
- Users prefer answers under 3 sentences
- Most questions fall into the 10 categories listed above
- A curated FAQ dataset of 20–30 pairs is sufficient for prototype testing
- Groww users are comfortable with plain-text responses (no rich formatting needed)
