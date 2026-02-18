import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="Dashboard Ventas", layout="wide")

# Función de carga de datos
@st.cache_data
def load_data():
    return pd.read_csv('data/ventas.csv')

df = load_data()

st.title("Reporte de Ventas")
st.write("Datos cargados exitosamente:")
st.dataframe(df.head())

st.markdown("---")

# ==========================================
# ZONA DE TRABAJO
# ==========================================

# Espacio reservado para nuevas funcionalidades

