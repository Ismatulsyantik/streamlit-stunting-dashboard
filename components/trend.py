import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df = df.drop(columns=["Unnamed: 0"])
    return df
def trend_chart(data_path):
    df = load_data(data_path)
    trend = df.groupby("tahun").agg({
        "stunting_(%)": "mean",
        "ipm": "mean"
    }).reset_index()
    trend = trend.sort_values("tahun")
    trend["tahun"] = trend["tahun"].astype(str)
    trend["stunting_norm"] = (trend["stunting_(%)"] - trend["stunting_(%)"].min()) / (trend["stunting_(%)"].max() - trend["stunting_(%)"].min())
    trend["ipm_norm"] = (trend["ipm"] - trend["ipm"].min()) / (trend["ipm"].max() - trend["ipm"].min())
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=trend["tahun"],
        y=trend["stunting_norm"],
        name="Stunting (Normalized)",
        mode="lines",
        line=dict(color="#60A4E3", width=4, shape="spline"),
        fill="tozeroy",
        fillcolor="rgba(96, 164, 227, 0.25)"
    ))

    fig.add_trace(go.Scatter(
        x=trend["tahun"],
        y=trend["ipm_norm"],
        name="IPM (Normalized)",
        mode="lines",
        line=dict(color="#6556BF", width=4, shape="spline"),
        fill="tozeroy",
        fillcolor="rgba(101, 86, 191, 0.20)"
    ))

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Tahun",
        yaxis_title="Normalized Value (0–1)",
        hovermode="x unified",
        height=450,
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(orientation="h", x=0.5, xanchor="center", y=1.15)
    )

    return fig
