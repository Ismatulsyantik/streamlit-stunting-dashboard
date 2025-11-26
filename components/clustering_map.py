import streamlit as st
import folium
import json
from streamlit_folium import st_folium

def clustering_map():

    try:
        # Load geojson (gunakan relative path, bukan C:/ )
        with open("stunting_geo.geojson", "r", encoding="utf-8") as f:
            gdf = json.load(f)

        # Ambil koordinat untuk center map
        coords = []
        for feature in gdf["features"]:
            geom = feature["geometry"]
            if geom["type"] == "Polygon":
                coords += geom["coordinates"][0]
            elif geom["type"] == "MultiPolygon":
                for poly in geom["coordinates"]:
                    coords += poly[0]

        # Hitung rata-rata koordinat
        center_lat = sum([c[1] for c in coords]) / len(coords)
        center_lon = sum([c[0] for c in coords]) / len(coords)

        # Warna cluster
        cluster_colors = {
            0: "#ff7f0e",
            1: "#1f77b4",
        }

        # Create map
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=7.3,
            tiles="cartodbpositron"
        )

        # Tambahkan polygon dengan warna cluster
        folium.GeoJson(
            gdf,
            style_function=lambda feature: {
                "fillColor": cluster_colors.get(feature["properties"]["cluster"], "#cccccc"),
                "color": "white",
                "weight": 1.2,
                "fillOpacity": 0.9,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["kabupaten/kota", "stunting_(%)", "cluster"],
                aliases=["Kabupaten/Kota:", "Stunting (%):", "Cluster:"],
                localize=True
            )
        ).add_to(m)

        st_folium(m, width=520, height=430)

    except Exception as e:
        st.error(f"Gagal memuat peta: {e}")
