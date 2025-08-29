import streamlit as st
import pandas as pd
import plotly.express as px

# === Carregar dataset ===
df = pd.read_csv("State_Dengue_Model_Data_w_pop.csv")

df.rename(columns={
    'Year': 'Ano',
    'State': 'Estado',
    'Mean_Tmp': 'Temperatura_Media',
    'Min_Tmp': 'Temperatura_Minima',
    'Max_Tmp': 'Temperatura_Maxima',
    'Percipitation': 'Precipitacao',
    'Change_Tmp': 'Variacao_Temperatura',
    'State_ID': 'ID_Estado',
    'Cases': 'Casos',
    'Region': 'Regiao',
    'State_Area(km2)': 'Area_Estado_km2',
    'Population': 'Populacao'
}, inplace=True)

df["Incidencia"] = (df["Casos"] / df["Populacao"]) * 100000

# Mapeamento estados → regiões
mapa_regioes = {
    "Acre": "Norte", "Amazonas": "Norte", "Pará": "Norte", "Rondônia": "Norte", "Roraima": "Norte", "Amapá": "Norte", "Tocantins": "Norte",
    "Maranhão": "Nordeste", "Piauí": "Nordeste", "Ceará": "Nordeste", "Rio Grande do Norte": "Nordeste", "Paraíba": "Nordeste", "Pernambuco": "Nordeste", "Alagoas": "Nordeste", "Sergipe": "Nordeste", "Bahia": "Nordeste",
    "Minas Gerais": "Sudeste", "Espírito Santo": "Sudeste", "Rio de Janeiro": "Sudeste", "São Paulo": "Sudeste",
    "Paraná": "Sul", "Santa Catarina": "Sul", "Rio Grande do Sul": "Sul",
    "Mato Grosso": "Centro-Oeste", "Mato Grosso do Sul": "Centro-Oeste", "Goiás": "Centro-Oeste", "Distrito Federal": "Centro-Oeste",
    "Brazil": "Brasil"
}
df['Regiao'] = df['Estado'].map(mapa_regioes)

# === Streamlit UI ===
st.title("📊 Dashboard Simplificado de Dengue")

# === Gráfico 1: Casos totais no Brasil ===
st.subheader("📈 Casos Totais de Dengue (2012–2021)")
fig1 = px.area(df.groupby("Ano")["Casos"].sum().reset_index(),
               x="Ano", y="Casos",
               title="Evolução de Casos no Brasil",
               markers=True)
st.plotly_chart(fig1, use_container_width=True)

# === Gráfico 2: Incidência média por ano ===
st.subheader("📉 Incidência Média por Ano")
fig2 = px.bar(df.groupby("Ano")["Incidencia"].mean().reset_index(),
              x="Ano", y="Incidencia",
              title="Taxa de Incidência (média nacional)")
st.plotly_chart(fig2, use_container_width=True)

# === Gráfico 3: Casos por Região ===
st.subheader("📊 Casos de Dengue por Região")
fig3 = px.bar(df.groupby("Regiao")["Casos"].sum().reset_index(),
              x="Casos", y="Regiao", orientation="h",
              color="Regiao",
              title="Distribuição de Casos por Região (2012-2021)")
st.plotly_chart(fig3, use_container_width=True)



