import streamlit as st


def load_login_styles():
    st.markdown("""
    <style>

    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        background: #0a0a0a !important;
        overflow-x: hidden !important;
        overflow-y: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
    }

    [data-testid="stHeader"],
    header,
    footer,
    #MainMenu,
    section[data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
    }

    .block-container,
    [data-testid="stAppViewContainer"],
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
    }

    .login-center {
        text-align: center;
        margin-top: 70px;
        margin-bottom: 25px;
    }

    .brand {
        color: #ffffff;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 35px;
        letter-spacing: -0.5px;
    }

    .login-title {
        color: #ffffff;
        font-size: 62px;
        font-weight: 700;
        line-height: 1;
        margin-bottom: 4px;
        letter-spacing: -1px;
    }

    label,
    .stTextInput label,
    [data-testid="stTextInput"] label {
        color: #3b82f6 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stTextInput {
        margin-bottom: 18px !important;
    }

    input,
    .stTextInput input,
    [data-testid="stTextInput"] input {
        height: 50px !important;
        font-size: 15px !important;
        border-radius: 12px !important;
        background: #151515 !important;
        color: #ffffff !important;
        border: 1px solid #2b2b2b !important;
        padding: 12px 16px !important;
        box-sizing: border-box !important;
    }

    input:focus,
    .stTextInput input:focus {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79,70,229,0.15) !important;
        outline: none !important;
    }

    input::placeholder {
        color: #5f5f5f !important;
    }

    .forgot {
        color: #8b8b8b;
        font-size: 13px;
        margin-top: 4px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    .forgot:hover {
        color: #6366f1;
    }

    .stButton button,
    .stButton > button {
        width: 100% !important;
        height: 52px !important;
        border-radius: 12px !important;
        border: none !important;
        background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%) !important;
        color: white !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        letter-spacing: 0.8px !important;
        margin-top: 6px !important;
        box-shadow: 0 8px 20px rgba(79,70,229,0.25) !important;
    }

    .stButton button:hover {
        transform: translateY(-1px);
        background: linear-gradient(135deg, #818cf8 0%, #4f46e5 100%) !important;
    }

    .signup {
        color: #8b8b8b;
        font-size: 14px;
        margin-top: 28px;
        text-align: center;
    }

    .signup b {
        color: white;
    }

    @media (max-width: 900px) {

        .login-title {
            font-size: 46px;
        }
    }

    @media (max-width: 480px) {

        .login-center {
            margin-top: 40px;
        }

        .login-title {
            font-size: 38px;
        }

        input {
            height: 46px !important;
        }

        .stButton button {
            height: 48px !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)