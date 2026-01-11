import streamlit as st
import sqlite3
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Aviation Maintenance Dashboard", layout="wide")

st.title("✈️ Aviation Maintenance Analytics")
st.markdown("Visualização em tempo real das manutenções de aeronaves.")

# 1. Função para carregar os dados do Banco de Dados
def carregar_dados():
    conexao = sqlite3.connect('manutencao_aero.db')
    query = "SELECT * FROM logs"
    df = pd.read_sql_query(query, conexao)
    conexao.close()
    return df

df = carregar_dados()

# 2. Sidebar para Filtros
st.sidebar.header("Filtros")
prefixo_selecionado = st.sidebar.multiselect(
    "Selecione o Prefixo da Aeronave:",
    options=df["prefixo"].unique(),
    default=df["prefixo"].unique()
)

df_filtrado = df[df["prefixo"].isin(prefixo_selecionado)]

# 3. Métricas Principais (KPIs)
col1, col2 = st.columns(2)
with col1:
    st.metric("Total de Manutenções", len(df_filtrado))
with col2:
    st.metric("Aeronaves Únicas", len(df_filtrado["prefixo"].unique()))

st.divider()

# 4. Gráfico de Manutenções por Aeronave
st.subheader("📈 Manutenções por Aeronave")
contagem_aeronaves = df_filtrado["prefixo"].value_counts()
st.bar_chart(contagem_aeronaves)

# 5. Tabela de Dados Detalhada
st.subheader("📋 Lista Detalhada de Registros")
st.dataframe(df_filtrado, use_container_width=True)