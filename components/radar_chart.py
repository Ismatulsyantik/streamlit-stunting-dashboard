import plotly.graph_objects as go
import streamlit as st

def radar_chart(df):
    df_plot = df.copy()

    # Normalisasi
    df_norm = (df_plot - df_plot.min()) / (df_plot.max() - df_plot.min())

    variables = df_norm.columns.tolist()

    # Warna cluster
    colors = ["#ff7f0e", "#1f77b4"]

    fig = go.Figure()

    for idx, cluster in enumerate(df_norm.index):
        fig.add_trace(
            go.Scatterpolar(
                r=df_norm.loc[cluster].values,
                theta=variables,
                fill='toself',
                name=f"Cluster {cluster}",
                line=dict(color=colors[idx], width=3)
            )
        )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, showgrid=True, gridcolor="#dddddd"),
        ),
        showlegend=True,
        template="plotly_white",
        height=520,
        width=680,
    )

    st.plotly_chart(fig, use_container_width=True)