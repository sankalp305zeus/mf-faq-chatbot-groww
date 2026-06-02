# Project Context

<!-- AI: read this file first. It is the authoritative project identity. -->

## Identity
- **Name:** MF FAQ Chatbot
- **Slug:** mf-faq-chatbot-groww
- **One-liner:** Facts-only FAQ assistant for mutual fund scheme questions on Groww
- **Product:** Groww
- **AMC:** HDFC Mutual Fund
- **Type:** product
- **Stage:** prototype

## Problem
Investors on Groww ask repetitive questions about HDFC MF schemes (NAV, returns, risk, lock-in, exit load). Support teams spend time answering questions that have clear, documented answers.

## Solution
A chatbot that answers scheme-specific FAQs using only verified factual data. It does not give investment advice. It does not hallucinate or guess.

## Users
Retail mutual fund investors on Groww. They want quick, accurate answers about specific schemes — not generic financial advice.

## Scope
- **In scope:** Scheme facts (NAV, returns, category, risk, lock-in, exit load, fund manager)
- **Out of scope:** Investment advice, portfolio recommendations, real-time pricing

## Architecture
- Input: user question (natural language)
- Data source: curated FAQ dataset (sample-qa/) + scheme data (data/)
- Output: plain-text factual answer with source reference
- No live API calls in prototype phase

## Constraints
- Facts only — no opinions, predictions, or advice
- Answers must cite the data source
- HDFC MF schemes only (v1)
- No user data stored

## Assumptions (unvalidated)
<!-- AI: treat everything here as uncertain, not confirmed fact. -->
- Users prefer short answers over detailed explanations
- Most questions fall into 5-8 repeatable categories
- A curated FAQ dataset is sufficient for prototype accuracy
