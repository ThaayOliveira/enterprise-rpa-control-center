import streamlit as st
import pandas as pd
import plotly.express as px

from services import executar_bot

from repository import load_executions


def render_header():
    st.markdown(
        """
        <div class="main-title">
            Enterprise RPA Control Center
        </div>

        <div class="subtitle">
            Plataforma centralizada de automações corporativas
        </div>
        """,
        unsafe_allow_html=True
    )


def executar_bot_com_refresh(bot_name):
    resp = executar_bot(
        bot_name,
        st.session_state.token
    )

    if resp.status_code == 401:
        ok = refresh_access_token()

        if ok:
            resp = executar_bot(
                bot_name,
                st.session_state.token
            )

    return resp.json()


def render_buttons():
    st.subheader("🚀 Executar Bots")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📄 Report Bot"):
            resultado = executar_bot_com_refresh("report")
            mostrar_resultado(resultado)

    with col2:
        if st.button("❤️ Health Bot"):
            resultado = executar_bot_com_refresh("health")
            mostrar_resultado(resultado)

    with col3:
        if st.button("📡 Monitor Bot"):
            resultado = executar_bot_com_refresh("monitor")
            mostrar_resultado(resultado)

    with col4:
        if st.button("📊 Reconcile Bot"):
            resultado = executar_bot_com_refresh("reconcile")
            mostrar_resultado(resultado)

    st.divider()


def mostrar_resultado(resultado):
    if resultado.get("status") == "success":
        st.success(resultado["message"])

    elif resultado.get("detail"):
        st.error(resultado["detail"])

    else:
        st.error(
            resultado.get(
                "message",
                "Erro ao executar bot"
            )
        )


def render_metrics():
    df = get_executions()

    total = len(df)
    success = len(df[df["status"] == "success"])
    error = len(df[df["status"] == "error"])

    avg = round(
        df["duration"].mean(),
        2
    ) if total > 0 else 0

    st.subheader("📈 Indicadores")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Execuções", total)
    col2.metric("Sucessos", success)
    col3.metric("Falhas", error)
    col4.metric("Tempo Médio", f"{avg}s")

    st.divider()


def render_charts():
    df = load_executions()

    if df.empty:
        return

    st.subheader("📊 Analytics")

    col1, col2 = st.columns(2)

    bot_counts = (
        df["bot_name"]
        .value_counts()
        .reset_index()
    )

    bot_counts.columns = [
        "Bot",
        "Execuções"
    ]

    fig1 = px.bar(
        bot_counts,
        x="Bot",
        y="Execuções",
        title="Execuções por Bot",
        text_auto=True
    )

    col1.plotly_chart(
        fig1,
        use_container_width=True
    )

    status_counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Status",
        "Total"
    ]

    fig2 = px.pie(
        status_counts,
        names="Status",
        values="Total",
        title="Sucessos x Falhas",
        hole=0.45
    )

    col2.plotly_chart(
        fig2,
        use_container_width=True
    )

    avg_time = (
        df.groupby("bot_name")["duration"]
        .mean()
        .reset_index()
    )

    avg_time.columns = [
        "Bot",
        "Tempo Médio"
    ]

    fig3 = px.bar(
        avg_time,
        x="Bot",
        y="Tempo Médio",
        title="Tempo Médio por Bot (s)",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.divider()


def render_table():
    df = load_executions()

    st.subheader("📋 Histórico de Execuções")

    if df.empty:
        st.info("Nenhuma execução registrada.")
        return

    df = df.copy()

    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    col1, col2, col3, col4 = st.columns(4)

    bots = ["Todos"] + sorted(
        df["bot_name"]
        .unique()
        .tolist()
    )

    bot_filter = col1.selectbox(
        "Bot",
        bots
    )

    status_options = ["Todos"] + sorted(
        df["status"]
        .unique()
        .tolist()
    )

    status_filter = col2.selectbox(
        "Status",
        status_options
    )

    periodo = col3.selectbox(
        "Período",
        [
            "Tudo",
            "Hoje",
            "7 dias",
            "30 dias"
        ]
    )

    busca = col4.text_input("Buscar")

    if bot_filter != "Todos":
        df = df[
            df["bot_name"] == bot_filter
        ]

    if status_filter != "Todos":
        df = df[
            df["status"] == status_filter
        ]

    hoje = pd.Timestamp.now()

    if periodo == "Hoje":
        df = df[
            df["created_at"].dt.date
            == hoje.date()
        ]

    elif periodo == "7 dias":
        df = df[
            df["created_at"]
            >= hoje - pd.Timedelta(days=7)
        ]

    elif periodo == "30 dias":
        df = df[
            df["created_at"]
            >= hoje - pd.Timedelta(days=30)
        ]

    if busca:
        df = df[
            df["message"].str.contains(
                busca,
                case=False,
                na=False
            )
            |
            df["bot_name"].str.contains(
                busca,
                case=False,
                na=False
            )
        ]

    df["status"] = df["status"].replace({
        "success": "🟢 success",
        "error": "🔴 error"
    })

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Exportar CSV",
        data=csv,
        file_name="relatorio_execucoes_filtrado.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("")

    st.dataframe(
        df,
        use_container_width=True,
        height=520
    )