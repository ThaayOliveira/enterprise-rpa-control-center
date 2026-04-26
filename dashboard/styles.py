import streamlit as st


def load_styles(theme="light"):

    if theme == "dark":
        bg = "#0f172a"
        card = "#111827"
        border = "#1e293b"
        text = "#f8fafc"
        sub = "#94a3b8"

    else:
        bg = "#f8fafc"
        card = "#ffffff"
        border = "#e5e7eb"
        text = "#0f172a"
        sub = "#64748b"

    st.markdown(f"""
    <style>

    .stApp {{
        background-color: {bg};
        color: {text};
    }}

    header[data-testid="stHeader"] {{
        background-color: {bg};
    }}

    div[data-testid="stToolbar"] {{
        background-color: transparent;
    }}

    div[data-testid="stDecoration"] {{
        background: none;
    }}

    div[data-testid="stStatusWidget"] * {{
        color: {text} !important;
    }}

    section[data-testid="stSidebar"] {{
        background-color: {card};
        border-right: 1px solid {border};
    }}

    .main-title {{
        font-size: 44px;
        font-weight: 700;
        color: {text};
        margin-bottom: 0;
    }}

    .subtitle {{
        color: {sub};
        margin-top: 0;
        margin-bottom: 30px;
    }}

    h1, h2, h3, h4, p, span, label {{
        color: {text} !important;
    }}

    div[data-testid="metric-container"] {{
        background: {card};
        border: 1px solid {border};
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}

    /* BOTÕES NORMAIS */
    div.stButton > button {{
        width: 100%;
        height: 48px;
        border-radius: 12px;
        background: {card};
        color: {text};
        border: 1px solid {border};
        font-weight: 600;
    }}

    div.stButton > button:hover {{
        border: 1px solid #3b82f6;
        transform: translateY(-1px);
        transition: 0.2s;
    }}

    /* DOWNLOAD BUTTON */
    div[data-testid="stDownloadButton"] > button {{
        width: 100%;
        height: 48px;
        border-radius: 12px;
        background: #3b82f6;
        color: white;
        border: none;
        font-weight: 600;
    }}

    div[data-testid="stDownloadButton"] > button:hover {{
        opacity: 0.92;
    }}

    .stDataFrame {{
        background: {card};
        border-radius: 14px;
        overflow: hidden;
    }}

    hr {{
        border-color: {border};
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    </style>
    """, unsafe_allow_html=True)