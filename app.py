import streamlit as st
import pandas as pd
from dq_checks import run_dq_checks
from dashboard import show_dashboard

st.set_page_config(page_title="DQ Demo", layout="wide")

st.title("Datakwaliteit Demo")

uploaded_file = st.file_uploader("Upload je dataset (CSV)", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Dataset succesvol ingeladen!")
        st.dataframe(df.head())

        dq_result = run_dq_checks(df)
        show_dashboard(dq_result)

    except Exception as e:
        st.error(f"Fout bij inlezen bestand: {e}")
