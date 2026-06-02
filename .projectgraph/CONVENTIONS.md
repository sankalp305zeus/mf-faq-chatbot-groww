# Conventions

<!-- Rules only. Source of truth for AI behaviour on this project. -->

## Content rules
- Answers must be facts only — no opinions, predictions, or investment advice
- Every answer must cite its data source (file name or field name)
- Do not use hedging language like "it depends" without explaining what it depends on

## Data rules
- All scheme data must come from verified sources (HDFC MF website, AMFI, Groww scheme page)
- No estimated or inferred data — mark any gap as [DATA MISSING]
- Dataset files live in data/ — do not embed data inline in code

## Output format
- Answers: 1–3 sentences max
- If a question is out of scope, say: "This chatbot answers factual questions about HDFC MF schemes only."
- Never say "I think" or "I believe"

## Process
- New scheme categories require a log/ entry before adding to scope
- Q&A pairs in sample-qa/ must be reviewed before using as training data

## AI must never do on this project
- Give investment advice or recommendations
- Answer questions about non-HDFC MF schemes (v1)
- Fabricate scheme data — return [DATA MISSING] instead
- Store or repeat any user-provided personal information
