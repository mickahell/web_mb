"""
#############################################
#
# 9_Check.py
#
# health check page
#
#############################################
"""
import streamlit as st
from call import Call
from helpers import Configuration


def alive():
    """Healthcheck function."""
    st.markdown("### Healcheck")
    a_live = Call()
    a_live.req_url(endpoint="health", protocol="get")

    if a_live.status_code != 200:
        st.error("The CosmoAppy doesn't respond.")
    else:
        st.success("The CosmoAppy is ready.")
        st.json(a_live.response)


def status():
    """Status function."""
    st.markdown("### Status")
    a_status = Call()
    a_status.req_url(endpoint="auth/status", protocol="get")

    if a_status.status_code != 200:
        st.error("The CosmoAppy doesn't respond.")
    else:
        st.success("Everything looks fine.")
        st.json(a_status.response)


def profile():
    """Profile function."""
    st.markdown("### Profile")
    myconf = Configuration()
    st.json(vars(myconf), expanded=False)


st.set_page_config(
    page_title="Check",
    page_icon=":busts_in_silhouette:",
    layout="wide",
    initial_sidebar_state="auto",
)

st.write("# Check page ! ⚙️")

alive()
status()
profile()
