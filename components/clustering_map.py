import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import st_folium
def clustering_map():

    try:
        gdf = gpd.read_file("C:\\Users\\Hype AMD\\STREAMLITE\\stunting_geo.geojson")
        gdf = gdf.to_crs(4326)

        center_lat = gdf.geometry.centroid.y.mean()
        center_lon = gdf.geometry.centroid.x.mean()

        cluster_colors = {
            0: "#ff7f0e",
            1: "#1f77b4",
        }

        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=7.3,
            tiles=None,      # Remove basemap
            zoom_control=False,
            scrollWheelZoom=False,
            dragging=False
        )

        # Boundary aesthetic
        folium.GeoJson(
            gdf.boundary,
            style_function=lambda x: {"color": "#eeeeee", "weight": 1.1}
        ).add_to(m)

        # Cluster polygons
        folium.GeoJson(
            gdf,
            style_function=lambda feature: {
                "fillColor": cluster_colors.get(feature["properties"]["cluster"]),
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

        # 🧼 Force transparent background (fix!)
        m.get_root().html.add_child(folium.Element("""
        <style>
        .leaflet-container {
            background: transparent !important;
        }
        </style>
        """))

        st_folium(m, width=520, height=430)

    except Exception as e:
        st.error(f"Gagal memuat peta: {e}")