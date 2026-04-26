import streamlit as st

from services import login, refresh_token
from login_styles import load_login_styles


def init_session():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if "token" not in st.session_state:
        st.session_state.token = None

    if "refresh_token" not in st.session_state:
        st.session_state.refresh_token = None


def logout():

    st.session_state.authenticated = False
    st.session_state.token = None
    st.session_state.refresh_token = None


def render_login():

    load_login_styles()

    left, right = st.columns([1, 1.7])

    with left:

        st.markdown(
            """
            <div class="brand">🏠 RPA ENTERPRISE</div>
            <div class="login-title">Sign In</div>
            """,
            unsafe_allow_html=True
        )

        username = st.text_input(
            "User Name",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter Password"
        )

        st.markdown(
            "<div class='forgot'>FORGOT PASSWORD?</div>",
            unsafe_allow_html=True
        )

        if st.button(
            "SIGN IN",
            use_container_width=True
        ):

            resp = login(username, password)

            if resp.status_code == 200:

                data = resp.json()

                st.session_state.token = data["access_token"]
                st.session_state.refresh_token = data["refresh_token"]
                st.session_state.authenticated = True

                st.rerun()

            else:
                st.error("Invalid credentials")

        st.markdown(
            "<div class='signup'>Don't have an account? <b>Sign up</b></div>",
            unsafe_allow_html=True
        )

    with right:

        st.image(
            "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1400&q=80",
            use_container_width=True
        )


def require_login():

    init_session()

    if not st.session_state.authenticated:
        render_login()
        st.stop()


def refresh_access_token():

    resp = refresh_token(
        st.session_state.refresh_token
    )

    if resp.status_code == 200:

        data = resp.json()

        st.session_state.token = data["access_token"]
        return True

    logout()
    return False