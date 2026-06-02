import streamlit as st

# ── FAQ data (logic unchanged from v1) ────────────────────────────────────────

FAQ = [
    {
        "keywords": ["minimum sip", "min sip", "sip amount", "sip for flexi cap", "flexi cap sip"],
        "answer": "The minimum SIP amount for HDFC Flexi Cap Fund is ₹100 per instalment.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/direct",
    },
    {
        "keywords": ["lock-in", "lock in", "elss lock", "elss tax saver lock", "how long lock"],
        "answer": "HDFC ELSS Tax Saver has a statutory lock-in period of 3 years from the date of allotment. Redemption is not permitted before the lock-in period ends.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver/direct",
    },
    {
        "keywords": ["exit load elss", "exit load tax saver", "elss exit"],
        "answer": "The exit load on HDFC ELSS Tax Saver Fund is NIL.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver/direct",
    },
    {
        "keywords": ["exit load flexi cap", "flexi cap exit"],
        "answer": "The exit load is 1.00% if units are redeemed or switched out within 1 year of allotment. There is no exit load after 1 year.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-flexi-cap-fund/direct",
    },
    {
        "keywords": ["top 100", "hdfc top 100"],
        "answer": "HDFC Top 100 Fund was renamed to HDFC Large Cap Fund effective January 1, 2025. The Direct Plan has a minimum SIP of ₹100, exit load of 1.00% if redeemed within 1 year, TER of 0.98%, and benchmark of NIFTY 100 Total Return Index.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-large-cap-fund/direct",
    },
    {
        "keywords": ["expense ratio sensex", "ter sensex", "ter index", "expense ratio index", "sensex expense"],
        "answer": "The Total Expense Ratio (TER) for the HDFC BSE Sensex Index Fund Direct Plan is 0.21% per annum.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-bse-sensex-index-fund/direct",
    },
    {
        "keywords": ["expense ratio elss", "ter elss", "ter tax saver"],
        "answer": "The Total Expense Ratio (TER) for HDFC ELSS Tax Saver Fund (Direct Plan) is 1.11% per annum.",
        "source": "https://www.hdfcfund.com/explore/mutual-funds/hdfc-elss-tax-saver/direct",
    },
    {
        "keywords": ["account statement", "download statement", "statement download"],
        "answer": "You can download your account statement directly from the HDFC MF website. Choose a PAN-based statement (all folios) or a folio-based statement, and select your preferred date range.",
        "source": "https://www.hdfcfund.com/services/consolidated-account-statement",
    },
    {
        "keywords": ["capital gains", "tax statement", "income tax statement", "gains statement"],
        "answer": "You can request your capital gains statement online through the HDFC MF investor services page. Statements are available free of cost and can also be downloaded via CAMS or KFintech using your PAN and registered email ID.",
        "source": "https://www.hdfcfund.com/information/request-statement",
    },
    {
        "keywords": ["nav", "current nav", "today nav", "latest nav"],
        "answer": "NAV changes daily. Check the latest NAV for any HDFC MF scheme on the AMFI NAV History page.",
        "source": "https://www.amfiindia.com/net-asset-value/nav-history",
    },
]

REFUSALS = [
    ("should i invest", "This chatbot provides factual information only and does not give investment advice."),
    ("better for me", "This chatbot provides factual information only and does not give investment advice."),
    ("which is better", "This chatbot provides factual information only and does not give investment advice."),
    ("recommend", "This chatbot provides factual information only and does not give investment advice."),
    ("future return", "This chatbot does not predict future returns. Past performance is not a guarantee of future results."),
    ("will it give", "This chatbot does not predict future returns. Past performance is not a guarantee of future results."),
    ("predict", "This chatbot does not predict future returns. Past performance is not a guarantee of future results."),
    ("next year return", "This chatbot does not predict future returns. Past performance is not a guarantee of future results."),
    ("mirae", "This chatbot answers factual questions about HDFC MF schemes only."),
    ("axis", "This chatbot answers factual questions about HDFC MF schemes only."),
    ("sbi", "This chatbot answers factual questions about HDFC MF schemes only."),
    ("icici", "This chatbot answers factual questions about HDFC MF schemes only."),
    ("kotak", "This chatbot answers factual questions about HDFC MF schemes only."),
    ("my portfolio", "This chatbot does not access or store personal account information."),
    ("my pan", "This chatbot does not access or store personal account information."),
    ("my folio", "This chatbot does not access or store personal account information."),
]


def get_response(question: str) -> dict:
    q = question.lower().strip()
    for trigger, refusal_text in REFUSALS:
        if trigger in q:
            return {"type": "refusal", "answer": refusal_text, "source": None}
    for faq in FAQ:
        if any(kw in q for kw in faq["keywords"]):
            return {"type": "answer", "answer": faq["answer"], "source": faq["source"]}
    return {
        "type": "missing",
        "answer": "[DATA MISSING] — This information was not found in the verified source list.",
        "source": "data/source-list.md",
    }


# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="MF FAQ Chatbot — Groww Trial",
    page_icon="💬",
    layout="centered",
)

# ── Groww theme CSS (from Stitch design spec) ─────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #0b1015 !important;
    color: #dee3ea !important;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; padding-bottom: 6rem !important; max-width: 800px !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1f2937; border-radius: 10px; }

/* ── App header ── */
.pg-header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(11,16,21,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(63,74,67,0.3);
    padding: 14px 0 10px 0;
    margin-bottom: 20px;
}
.pg-header h1 {
    font-size: 22px;
    font-weight: 700;
    color: #44edb7;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.01em;
}
.pg-header p {
    font-size: 12px;
    color: #85948c;
    margin: 2px 0 0 0;
    letter-spacing: 0.02em;
}
.pg-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    background: #171c21;
    border: 1px solid rgba(63,74,67,0.4);
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 500;
    color: #85948c;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-top: 10px;
}

/* ── Chip buttons ── */
.chip-row { display: flex; flex-wrap: wrap; gap: 8px; margin: 16px 0 24px 0; }
.chip {
    display: inline-block;
    padding: 7px 16px;
    border: 1px solid #3c4a43;
    border-radius: 9999px;
    background: transparent;
    color: #dee3ea;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: border-color 0.2s, color 0.2s;
    font-family: 'Inter', sans-serif;
}
.chip:hover { border-color: #44edb7; color: #44edb7; }

/* ── Chat bubbles ── */
.bubble-wrap-ai { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 20px; }
.bubble-avatar {
    width: 32px; height: 32px; border-radius: 50%;
    background: rgba(68,237,183,0.1);
    border: 1px solid rgba(68,237,183,0.25);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0;
}
.bubble-ai {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 16px;
    border-top-left-radius: 4px;
    padding: 14px 16px;
    max-width: 85%;
    font-size: 15px;
    line-height: 1.6;
    color: #dee3ea;
}
.bubble-wrap-user { display: flex; justify-content: flex-end; margin-bottom: 20px; }
.bubble-user {
    border: 1px solid #1f2937;
    border-radius: 16px;
    border-top-right-radius: 4px;
    padding: 12px 16px;
    max-width: 85%;
    font-size: 15px;
    line-height: 1.6;
    color: #dee3ea;
    background: transparent;
}

/* ── Source card ── */
.source-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;
    padding: 8px 12px;
    background: #171c21;
    border: 1px solid rgba(63,74,67,0.4);
    border-radius: 10px;
    font-size: 12px;
    color: #85948c;
    text-decoration: none;
}
.source-card:hover { border-color: #44edb7; color: #44edb7; }
.source-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: #44edb7; margin-right: 6px; font-weight: 600; }
.source-url { word-break: break-all; }

/* ── Refusal / missing bubbles ── */
.bubble-refusal {
    background: #1a1400;
    border: 1px solid rgba(255,180,171,0.2);
    border-radius: 16px;
    border-top-left-radius: 4px;
    padding: 14px 16px;
    max-width: 85%;
    font-size: 15px;
    line-height: 1.6;
    color: #ffb4ab;
}
.bubble-missing {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 16px;
    border-top-left-radius: 4px;
    padding: 14px 16px;
    max-width: 85%;
    font-size: 15px;
    line-height: 1.6;
    color: #85948c;
    font-style: italic;
}

/* ── Streamlit chat input override (sticky composer) ── */
.stChatInput {
    background: rgba(11,16,21,0.92) !important;
    backdrop-filter: blur(20px) !important;
    border-top: 1px solid rgba(63,74,67,0.2) !important;
    padding: 12px 0 16px 0 !important;
}
.stChatInput textarea, .stChatInput input {
    background: #0a0f14 !important;
    border: 1px solid #1f2937 !important;
    border-radius: 9999px !important;
    color: #dee3ea !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 15px !important;
    padding: 12px 20px !important;
    caret-color: #44edb7 !important;
}
.stChatInput textarea:focus, .stChatInput input:focus {
    border-color: #44edb7 !important;
    box-shadow: 0 0 0 1px #44edb7 !important;
    outline: none !important;
}
/* Send button */
.stChatInput button {
    background: #00d09c !important;
    border-radius: 9999px !important;
    border: none !important;
    color: #003828 !important;
}
.stChatInput button:hover { background: #44edb7 !important; }

/* ── Streamlit button (chip fallback) ── */
div.stButton > button {
    background: transparent !important;
    border: 1px solid #3c4a43 !important;
    border-radius: 9999px !important;
    color: #dee3ea !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 6px 16px !important;
    transition: border-color 0.2s, color 0.2s !important;
}
div.stButton > button:hover {
    border-color: #44edb7 !important;
    color: #44edb7 !important;
}

/* ── Divider ── */
hr { border-color: #1f2937 !important; }

/* ── Footer disclaimer ── */
.pg-footer {
    font-size: 11px;
    color: #3c4a43;
    text-align: center;
    margin-top: 32px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "chip_query" not in st.session_state:
    st.session_state.chip_query = ""

# ── Header ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="pg-header">
  <h1>MF FAQ Chatbot</h1>
  <p>Groww Trial — HDFC Mutual Fund · 4 Schemes · v1</p>
  <div class="pg-badge">⚡ Facts only &nbsp;·&nbsp; No investment advice</div>
</div>
""", unsafe_allow_html=True)

# ── Chips ─────────────────────────────────────────────────────────────────────

CHIPS = [
    "Minimum SIP for HDFC Flexi Cap Fund",
    "Does HDFC ELSS have a lock-in?",
    "Where do I download capital gains statement?",
]

col1, col2, col3 = st.columns(3)
for col, chip in zip([col1, col2, col3], CHIPS):
    with col:
        if st.button(chip, key=f"chip_{chip}"):
            st.session_state.chip_query = chip

# ── Chat history ──────────────────────────────────────────────────────────────

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    result = msg.get("result")

    if role == "user":
        st.markdown(
            f'<div class="bubble-wrap-user"><div class="bubble-user">{content}</div></div>',
            unsafe_allow_html=True,
        )
    else:
        if result and result["type"] == "answer":
            source_html = (
                f'<a class="source-card" href="{result["source"]}" target="_blank">'
                f'<span><span class="source-label">Source</span>'
                f'<span class="source-url">{result["source"]}</span></span>'
                f'<span>↗</span></a>'
            )
            st.markdown(
                f'<div class="bubble-wrap-ai">'
                f'<div class="bubble-avatar">✦</div>'
                f'<div class="bubble-ai">{content}{source_html}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        elif result and result["type"] == "refusal":
            st.markdown(
                f'<div class="bubble-wrap-ai">'
                f'<div class="bubble-avatar">✦</div>'
                f'<div class="bubble-refusal">{content}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="bubble-wrap-ai">'
                f'<div class="bubble-avatar">✦</div>'
                f'<div class="bubble-missing">{content}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

# ── Sticky composer (st.chat_input is natively sticky) ────────────────────────

chip_q = st.session_state.pop("chip_query", "") if st.session_state.get("chip_query") else ""
prompt = st.chat_input("Ask a mutual fund question…") or chip_q

if prompt:
    result = get_response(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    if result["type"] == "answer":
        reply = result["answer"]
    elif result["type"] == "refusal":
        reply = result["answer"]
    else:
        reply = result["answer"]

    st.session_state.messages.append({"role": "assistant", "content": reply, "result": result})
    st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="pg-footer">
  This chatbot provides factual information about mutual fund schemes only.<br>
  It does not provide investment advice. Mutual fund investments are subject to market risks.
</div>
""", unsafe_allow_html=True)
