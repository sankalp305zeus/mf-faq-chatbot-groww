# Sample Q&A — MF FAQ Chatbot

**Project:** MF FAQ Chatbot — Groww Trial
**Version:** v1
**Last updated:** 2026-06-02
**Rules source:** `prototype/faq-rules.md`
**Data source:** `data/source-list.md`

Format: Question / Answer / Source — following faq-rules.md §3 exactly.
Refusals follow faq-rules.md §5 — no source citation added.

---

## Factual Questions

---

**Q1 — Minimum SIP**

**Question:** What is the minimum SIP amount for HDFC Flexi Cap Fund?

**Answer:** The minimum SIP amount for HDFC Flexi Cap Fund is ₹100 per instalment.

**Source:** https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/direct

---

**Q2 — Lock-in (ELSS)**

**Question:** Does HDFC ELSS Tax Saver have a lock-in? How long is it?

**Answer:** Yes. HDFC ELSS Tax Saver has a statutory lock-in period of 3 years from the date of allotment. Redemption is not permitted before the lock-in period ends.

**Source:** https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver/direct

---

**Q3 — Exit load**

**Question:** Is there any exit load on HDFC ELSS Tax Saver Fund?

**Answer:** No. The exit load on HDFC ELSS Tax Saver Fund is NIL.

**Source:** https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver/direct

---

**Q4 — Scheme name alias (edge case)**

**Question:** I want to invest in HDFC Top 100 Fund. Can you give me the details?

**Answer:** HDFC Top 100 Fund was renamed to HDFC Large Cap Fund effective January 1, 2025. The HDFC Large Cap Fund (Direct Plan) has a minimum SIP of ₹100, an exit load of 1.00% if redeemed within 1 year, a TER of 0.98%, and a benchmark of NIFTY 100 Total Return Index.

**Source:** https://www.hdfcfund.com/explore/mutual-funds/hdfc-large-cap-fund/direct · Addendum: https://files.hdfcfund.com/s3fs-public/2024-12/1280%20-%20Addendum%20-%20Change%20in%20name%20of%20HDFC%20Top%20100%20Fund%20w.e..f.%20Jan%2001,%202025.pdf

---

**Q5 — Expense ratio**

**Question:** What is the expense ratio of HDFC Index Fund Sensex — Direct Plan?

**Answer:** The Total Expense Ratio (TER) for the HDFC BSE Sensex Index Fund Direct Plan is 0.21% per annum.

**Source:** https://www.hdfcfund.com/explore/mutual-funds/hdfc-bse-sensex-index-fund/direct

---

**Q6 — Account statement download**

**Question:** Where can I download my HDFC Mutual Fund account statement?

**Answer:** You can download your account statement directly from the HDFC MF website. You can choose a PAN-based statement (all folios) or a folio-based statement, and select your preferred date range.

**Source:** https://www.hdfcfund.com/services/consolidated-account-statement

---

**Q7 — Capital gains statement**

**Question:** Where do I get my capital gains statement from HDFC MF for income tax filing?

**Answer:** You can request your capital gains statement online through the HDFC MF investor services page. Statements are available free of cost and can also be downloaded via CAMS or KFintech using your PAN and registered email ID.

**Source:** https://www.hdfcfund.com/information/request-statement

---

## Refusal Questions

---

**R1 — Investment advice**

**Question:** Should I invest in HDFC Top 100 Fund or HDFC Flexi Cap Fund? Which is better for me?

**Answer:** This chatbot provides factual information only and does not give investment advice.

**Source:** *(not applicable — refusal)*

---

**R2 — Return prediction**

**Question:** Will HDFC Flexi Cap Fund give good returns in the next 3 years?

**Answer:** This chatbot does not predict future returns. Past performance is not a guarantee of future results.

**Source:** *(not applicable — refusal)*

---

**R3 — Out-of-scope scheme**

**Question:** What is the NAV of Mirae Asset Large Cap Fund?

**Answer:** This chatbot answers factual questions about HDFC MF schemes only.

**Source:** *(not applicable — refusal)*

---

## Data gaps noted during Q&A creation

| Gap | Detail | Impact |
|---|---|---|
| Returns (1Y / 3Y / 5Y) | Exact return figures were not captured in source-list.md during research. Scheme pages show returns but values change daily — not safe to hardcode. | Cannot write factual Q&A for returns category without a live data pull or a dated snapshot. |
| Fund manager — HDFC Large Cap Fund | Fund manager name (Rahul Baijal) was found during URL verification but not recorded in source-list.md. | Minor gap — add a fund manager row to source-list.md or data file. |
| Minimum lump sum | Not captured for any scheme in source-list.md. | Cannot answer "What is the minimum one-time investment?" without checking scheme pages directly. |
| ELSS KIM PDF direct URL | KIM hub page lists it but no direct PDF URL was found during research. | Low impact — hub page URL is sufficient for citation. |
