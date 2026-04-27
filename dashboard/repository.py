import pandas as pd
import streamlit as st

from services import get_executions


def load_executions():

    resp = get_executions(
        st.session_state.token
    )

    if resp.status_code == 200:
        data = resp.json()

        if data:
            return pd.DataFrame(data)

    return pd.DataFrame()