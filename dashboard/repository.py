import pandas as pd
import streamlit as st

from services import get_executions
from auth import refresh_access_token


def load_executions():
    token = st.session_state.get("token")

    if not token:
        return pd.DataFrame()

    resp = get_executions(token)

    if resp.status_code == 401:

        ok = refresh_access_token()

        if ok:
            resp = get_executions(
                st.session_state.token
            )

    if resp.status_code == 200:
        data = resp.json()

        if data:
            return pd.DataFrame(data)

    return pd.DataFrame()