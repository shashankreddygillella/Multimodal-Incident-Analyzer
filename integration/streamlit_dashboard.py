"""
Simple Streamlit dashboard for the final master incident report.

Run from repository root:
    streamlit run integration/streamlit_dashboard.py
"""

from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "integration" / "master_incident_report_fixed.csv"

st.set_page_config(page_title="Multimodal Incident Analyzer", layout="wide")
st.title("Multimodal Incident Report Analyzer")
st.write("Dashboard for structured incident records produced from audio, PDF, image, video, and text data.")

if not DATA_PATH.exists():
    st.error("master_incident_report_fixed.csv not found. Run: python integration/04_merge_all_modalities.py")
    st.stop()

df = pd.read_csv(DATA_PATH).fillna("N/A")

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Sources", df["Source"].nunique() if "Source" in df.columns else 0)
col3.metric("High Severity", int((df["Severity"] == "High").sum()) if "Severity" in df.columns else 0)

source_filter = st.multiselect("Filter by source", sorted(df["Source"].unique()), default=sorted(df["Source"].unique()))
severity_filter = st.multiselect("Filter by severity", sorted(df["Severity"].unique()), default=sorted(df["Severity"].unique()))

filtered = df[df["Source"].isin(source_filter) & df["Severity"].isin(severity_filter)]

st.subheader("Incident Records")
st.dataframe(filtered, use_container_width=True)

st.subheader("Severity Count")
st.bar_chart(filtered["Severity"].value_counts())

st.subheader("Source Count")
st.bar_chart(filtered["Source"].value_counts())
