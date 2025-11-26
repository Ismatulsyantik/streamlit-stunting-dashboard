import plotly.graph_objs as go
import numpy as np
from scipy.spatial import ConvexHull

# Fungsi konversi HEX → RGBA
def hex_to_rgba(hex_color, alpha=0.25):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def scatter_cluster_plot(df, x_col="PC1", y_col="PC2", cluster_col="Cluster", label_col="Label",  theme="light"):
    font_color = "#ffffff" if theme.lower() == "dark" else "#000000"
    grid_color = "rgba(200,200,200,0.25)" if theme.lower() == "light" else "rgba(255,255,255,0.25)"
    # Warna untuk 2 cluster (bisa lebih kalau nanti bertambah)
    colors = {
        0: "#ff7f0e",   # biru
        1: "#1f77b4",   # oranye
        2: "#2ca02c",   # hijau (standby)
        3: "#d62728",   # merah (standby)
    }

    fig = go.Figure()

    # Pastikan cluster diurutkan
    for c in sorted(df["Cluster"].unique()):
        sub = df[df["Cluster"] == c]
        points = sub[["PC1", "PC2"]].values

        # ---- Scatter titik ----
        fig.add_trace(go.Scatter(
            x=sub["PC1"],
            y=sub["PC2"],
            mode="markers+text",
            text=sub["Label"],
            textposition="top center",
            marker=dict(
                size=11,
                color=colors.get(c, "#000000"),
                line=dict(color="white" if theme == "dark" else "black", width=1)
            ),
            name=f"Cluster {c}",
            showlegend=True
        ))

        # ---- Convex Hull kalau titik >= 3 ----
        if len(points) >= 3:
            try:
                hull = ConvexHull(points)
                hull_points = points[hull.vertices]

                fig.add_trace(go.Scatter(
                    x=hull_points[:, 0],
                    y=hull_points[:, 1],
                    fill='toself',
                    mode='lines',
                    line=dict(color=colors.get(c, "#000000")),
                    fillcolor=hex_to_rgba(colors.get(c, "#000000"), 0.22),
                    name=f"Area Cluster {c}"
                ))
            except:
                pass  # Biar tidak error kalau hull gagal

    # Layout
    fig.update_layout(
        width = 2000,
        height = 600,
        margin=dict(l=60, r=60, t=20, b=60),
        font=dict(size=12, color=font_color),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            borderwidth=0
        ),
        xaxis_title=x_col,
        yaxis_title=y_col,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_xaxes(showgrid=True, gridcolor=grid_color)
    fig.update_yaxes(showgrid=True, gridcolor=grid_color)

    return fig