from enum import unique
import json
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static

st.title("Emitentes")

# Lendo dados
emitentes = pd.read_csv("Data/emitentes_cnae.csv")
emitentes["cnae_fiscal"] = emitentes["cnae_fiscal"].apply(str)
emitentes.rename(columns={"CÓDIGO NCM/SH":"NCM"}, inplace=True)
emitentes["NCM"] = emitentes["NCM"].apply(str)

# Filtros
cnaes = emitentes["cnae_fiscal"].unique()
cnae = st.sidebar.text_input("Escreva o CNAE desejado:")

ncms = emitentes["NCM"].unique()
ncm = st.sidebar.text_input("Escreva o NCM desejado:")

ufs = emitentes["UF EMITENTE"].unique()
uf = st.sidebar.multiselect("Selecione a(s) UF(s):",ufs)

if cnae != '':
    emitentes_filtro = emitentes.query(f"cnae_fiscal.str.startswith('{cnae}')")
if len(uf) > 0:  
    emitentes_cnae = emitentes_filtro.query(f"`UF EMITENTE` in {uf}")
if ncm != '':
    emitentes_filtro = emitentes_filtro.query(f"NCM.str.startswith('{ncm}')")


st.table(emitentes_filtro.sort_values(["total_notas","total_emi"], ascending=False))
