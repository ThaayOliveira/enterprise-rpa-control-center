import streamlit as st
import pandas as pd
import plotly.express as px

from services import executar_bot
from repository import load_executions
from auth import refresh_access_token


def render_header():
    st.title("Enterprise RPA Control Center")
    st.caption("Plataforma centralizada de automações corporativas")


def render_buttons():
    st.subheader("🚀 Executar Bots")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("📄 Report Bot", width="stretch"):
        executar("report")

    if col2.button("❤️ Health Bot", width="stretch"):
        executar("health")

    if col3.button("📡 Monitor Bot", width="stretch"):
        executar("monitor")

    if col4.button("📊 Reconcile Bot", width="stretch"):
        executar("reconcile")


def executar(bot_name):
    token = st.session_state.token

    resp = executar_bot(bot_name, token)

    if resp.status_code == 401:
        if refresh_access_token():
            token = st.session_state.token
            resp = executar_bot(bot_name, token)

    if resp.status_code == 200:
        st.success(f"{bot_name} executado com sucesso")
    else:
        st.error("Erro ao executar bot")


def render_metrics():
    st.subheader("📊 Métricas")

    df = load_executions()

    if df.empty:
        st.info("Sem dados disponíveis")
        return

    total = len(df)
    success = len(df[df["status"] == "success"])
    error = len(df[df["status"] == "error"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Execuções", total)
    col2.metric("Sucesso", success)
    col3.metric("Erro", error)


def render_charts():
    st.subheader("📈 Gráficos")

    df = load_executions()

    if df.empty:
        st.info("Sem dados para gráficos")
        return

    status_count = df["status"].value_counts().reset_index()
    status_count.columns = ["status", "count"]

    fig = px.pie(
        status_count,
        names="status",
        values="count",
        title="Distribuição de Status"
    )

    st.plotly_chart(fig, width="stretch")


def render_table():
    st.subheader("📋 Histórico")

    df = load_executions()

    if df.empty:
        st.info("Sem histórico disponível")
        return

    st.dataframe(df, width="stretch")