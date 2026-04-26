import streamlit as st

from auth import require_login, logout
from styles import load_styles

from components import (
    render_header,
    render_buttons,
    render_metrics,
    render_charts,
    render_table
)

st.set_page_config(
    page_title="Enterprise RPA Control Center",
    layout="wide"
)

require_login()

st.sidebar.title("⚙️ Configurações")

theme = st.sidebar.radio(
    "Tema",
    ["light", "dark"]
)

if st.sidebar.button("Sair"):
    logout()
    st.rerun()

load_styles(theme)

render_header()
render_buttons()
render_metrics()
render_charts()
render_table()