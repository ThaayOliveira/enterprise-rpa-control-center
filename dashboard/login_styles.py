import streamlit as st


def load_login_styles():

    st.markdown("""
    <style>

    .stApp{
        background:#000;
    }

    section[data-testid="stSidebar"]{
        display:none;
    }

    .brand{
        color:white;
        font-size:24px;
        font-weight:700;
        margin-top:30px;
        margin-bottom:100px;
    }

    .login-title{
        color:white;
        font-size:58px;
        font-weight:700;
        margin-bottom:45px;
    }

    .forgot{
        color:#5b7cff;
        font-size:14px;
        margin-top:8px;
        margin-bottom:22px;
    }

    .signup{
        color:white;
        opacity:.75;
        margin-top:120px;
        font-size:15px;
    }

    .stTextInput{
        max-width:420px;
    }

    .stTextInput label{
        color:white !important;
        font-size:15px;
        margin-bottom:6px;
    }

    .stTextInput input{
        background:#111;
        color:white;
        border:1px solid #2a2a2a;
        border-radius:10px;
        height:48px;
        padding:0 16px;
        font-size:16px;
        line-height:48px;
    }

    .stTextInput input::placeholder{
        color:#777;
        opacity:1;
    }

    .stButton{
        max-width:420px;
    }

    .stButton button{
        height:50px;
        background:#4a46ff;
        color:white;
        border:none;
        border-radius:10px;
        font-weight:700;
        font-size:16px;
        margin-top:14px;
    }

    .stButton button:hover{
        background:#3730ff;
    }

    #MainMenu, footer, header{
        visibility:hidden;
    }

    </style>
    """, unsafe_allow_html=True)