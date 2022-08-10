import pandas as pd
import streamlit as st
from millify import millify

# Definindo tema da aplicação

# Definindo funções úteis


# Coletando informações
info_geral = pd.read_csv("Data/info_gerais.csv",index_col=0)
st.write(info_geral)
# Extraindo filtros
# Definindo layut do app

st.title("Notas fiscais Portal da Transparência")

# Informações gerais
st.subheader("Informações gerais")
col1,col2,col3,col4 = st.columns(4)
with col1: st.metric("Número de observações",info_geral.loc["Número de observações"])
with col2: st.metric("Número de notas fiscais",info_geral.loc["Número de notas fiscais"])
with col3: st.metric("Número de NCMs",info_geral.loc["Número de NCMs"])
with col4: st.metric("Número de descrições",info_geral.loc["Número de descrições"])

# Emitentes
st.subheader("Emitentes")
col1,col2,col3,_ = st.columns(4)
with col1: st.metric("Número de emitentes",info_geral.loc["Número de emitentes"])
with col2: st.metric("Número de UFs emitentes",info_geral.loc["Número de UFs emitentes"])
with col3: st.metric("Número de municípios emitentes",info_geral.loc["Número de municípios emitentes"])

# Destinatários
st.subheader("Destinatários")
col1,col2,col3,_ = st.columns(4)
with col1: st.metric("Número de destinatários",info_geral.loc["Número de destinatários"])
with col2: st.metric("Número de UFs destinatárias",info_geral.loc["Número de UFs destinatárias"])
with col3: st.metric("Consumidores finais (%)",round(info_geral.loc["Consumidores finais (%)"],2))

