import streamlit as st
from components.kpi_cards import kpi_cards
from components.trend import trend_chart 
import geopandas as gpd
from streamlit_folium import st_folium
import folium
import branca.colormap as cm
from components.clustering_map import clustering_map
from components.radar_chart import radar_chart
import pandas as pd
from components.scater_plot import scatter_cluster_plot
from components.chatbot import chatbot_ui


st.set_page_config(
    page_title="Dashboard Stunting & IPM",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>
/* Hilangkan padding kiri-kanan */
.block-container {
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 20px;
    padding-right: 20px;
}
/* Hilangkan jarak antar elemen terlalu jauh */
section.main > div {
    padding-top: 5px !important;
}
</style>
""", unsafe_allow_html=True) 

# === LOAD CSS ===
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: CSS file not found at {file_path}. Custom styles will not be applied.")

load_css("assets/style.css")
with st.container():
    st.markdown("<div class='block-card'>", unsafe_allow_html=True)
    st.markdown(
        "<h2 style='text-align: center; font-weight: 700;'>Dashboard Stunting & Indeks Pembangunan Manusia (IPM) Jawa Timur</h2>",
        unsafe_allow_html=True
    )
    kpi_cards()
    st.markdown("</div>", unsafe_allow_html=True)


# ====== 2 KOLUMN: Trend (kiri) dan Cluster (kanan) ======
with st.container():
    col_left, col_right = st.columns([1, 1], gap = "small")

    # --- LEFT: TREND ---
    with col_left:
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align: center; font-weight: 600;'>Trend Stunting & IPM 2019–2024</h3>",
            unsafe_allow_html=True
        )
        fig_trend = trend_chart("C:/Users/Hype AMD/STREAMLITE/Ipm_Stunting.csv")
        st.plotly_chart(fig_trend, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- RIGHT: MAP ---
    with col_right:
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align: center; font-weight: 600;'> Clustering Jawa Timur 2020–2024</h3>",
            unsafe_allow_html=True
        )
        
        cluster_colors = {
            0: "#ff7f0e",
            1: "#1f77b4",
        }

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown(
                f"""
                <div style='text-align:center;'>
                  <div style='display:flex;align-items:center;gap:10px;'>
                     <div style='width:18px;height:18px;background:{cluster_colors[0]};border-radius:4px;'></div>
                     <span>Cluster 0</span>
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_b:
            st.markdown(
                f"""
                <div style='text-align:center;'>
                  <div style='display:flex;align-items:center;gap:10px;'>
                    <div style='width:18px;height:18px;background:{cluster_colors[1]};border-radius:4px;'></div>
                    <span>Cluster 1</span>  
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        clustering_map()
        st.markdown("</div>", unsafe_allow_html=True)
# ======================
#    RADAR + SCATTER
# ======================
df_radar = pd.read_csv("C:\\Users\\Hype AMD\\STREAMLITE\\data_radar.csv", index_col=0)
df_plot = pd.read_csv("C:\\Users\\Hype AMD\\STREAMLITE\\plot_cluster.csv")

with st.container():
    col1, col2 = st.columns([1, 1], gap = "small")

    # --- RADAR ---
    with col1:
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align: center; font-weight: 600;'>Perbandingan Profil Cluster</h3>",
            unsafe_allow_html=True)
        radar_chart(df_radar)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- SCATTER ---
    with col2:
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align: center; font-weight: 600;'>Visualisasi Cluster pada PCA Scatter Plot</h3>",
            unsafe_allow_html=True)
        fig = scatter_cluster_plot(df_plot)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

df_cluster = pd.read_csv("C:\\Users\\Hype AMD\\STREAMLITE\\hasil_cluster.csv", index_col=0)
with st.container():
   col3, col4 = st.columns([1,1], gap = "small")
   with col3 :
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.dataframe(df_cluster, use_container_width=True,height=300)
   with col4 :
        st.markdown("<div class='block-card'>", unsafe_allow_html=True)
        st.subheader("💬 Chatbot Analisis Data")
        st.write("Tanya apa saja tentang clustering, IPM, stunting, atau rekomendasi kebijakan.")
        chatbot_ui(df_cluster)
        st.markdown("</div>", unsafe_allow_html=True)