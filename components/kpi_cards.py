import streamlit as st

def kpi_cards():
    mean_stunting_2024 = 18.96
    mean_ipm_2024 = 73.31
    mean_stunting_2020 = 17.75
    national_drop = mean_stunting_2024 - mean_stunting_2020
    cluster_count = 2
    
    col1, col2, col3, col4 = st.columns(4)

    # KPI 1
    with col1:
        st.metric("Rata-rata Stunting 2020", f"{mean_stunting_2020:.2f} %")

    # KPI 2
    with col2:
        st.metric("Rata-rata Stunting 2024", f"{mean_stunting_2024:.2f} %")

    # KPI 3
    with col3:
        st.metric(
            "Perubahan Stunting (2020–2024)", 
            f"{national_drop:.2f} %",
            delta=f"{national_drop:.2f} %",
            delta_color="inverse",
        )

    # KPI 4
    with col4:
        st.metric("Jumlah Cluster", int(cluster_count))