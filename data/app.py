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

# Funcionalidad B: KPIs Generales
total_ingresos = df['ingreso'].sum()
total_unidades = df['unidades'].sum()

col1, col2 = st.columns(2)
col1.metric("Ingresos Totales", f"${total_ingresos}")
col2.metric("Unidades Vendidas", f"{total_unidades}")


