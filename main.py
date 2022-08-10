import pandas as pd
import streamlit as st

# Definindo tema da aplicação

# Definindo funções úteis



@st.cache
def lendo_nfs(file = "APP/Data/202109_202206_NFe.parquet"):
    nfs = pd.read_parquet(file)
    nfs["DATA EMISSÃO"] = pd.to_datetime(nfs["DATA EMISSÃO"])
    nfs.set_index("DATA EMISSÃO",inplace=True)
    return nfs

def Info_geral(df_notas):

    # Diconário de saída
    infos = {
        #Informações gerais
        "Número de observações" : df_notas.shape[0],
        "Número de ncms" : df_notas["CÓDIGO NCM/SH"].unique().__len__(),
        "Número de descrições" : df_notas["DESCRIÇÃO DO PRODUTO/SERVIÇO"].unique().__len__(),
        "Número de notas" : df_notas["CHAVE DE ACESSO"].unique().__len__(),

        # Emitentes
        "Número de emitentes" : df_notas["CPF/CNPJ Emitente"].unique().__len__(),
        "Número de ufs emitentes" : df_notas["UF EMITENTE"].unique().__len__(),
        "Número de mun emitentes" : df_notas["MUNICÍPIO EMITENTE"].unique().__len__(),

        # Destinatários
        "Número de destinatários" : df_notas["CNPJ DESTINATÁRIO"].unique().__len__(),
        "Número de ufs destinatárias" : df_notas["UF DESTINATÁRIO"].unique().__len__(),
        "Número de consumo" : df_notas["CONSUMIDOR FINAL"].apply(lambda x: int(x.split("-")[0])).mean() * 100
    }

    return infos

# Coletando informações
df_notas = lendo_nfs()

info_geral = Info_geral(df_notas)
# Extraindo filtros
#ncm = df_notas[["CÓDIGO NCM/SH","NCM/SH (TIPO DE PRODUTO)"]].drop_duplicates().dropna()
#ncm["NCM"] = ncm.apply(lambda x: str(x[0]) + ' - ' + x[1] ,axis=1)

# Definindo layut do app

st.title("Notas fiscais Portal da Transparência")

# Informações gerais
st.subheader("Informações gerais")
col1,col2,col3,col4 = st.columns(4)
with col1: st.metric("Número de observações",info_geral["Número de observações"])
with col2: st.metric("Número de notas fiscais",info_geral["Número de notas"])
with col3: st.metric("Número de NCMs",info_geral["Número de ncms"])
with col4: st.metric("Número de descrições",info_geral["Número de descrições"])

# Emitentes
st.subheader("Emitentes")
col1,col2,col3,_ = st.columns(4)
with col1: st.metric("Número de emitentes",info_geral["Número de emitentes"])
with col2: st.metric("Número de UFs emitentes",info_geral["Número de ufs emitentes"])
with col3: st.metric("Número de municípios emitentes",info_geral["Número de mun emitentes"])

# Destinatários
st.subheader("Destinatários")
col1,col2,col3,_ = st.columns(4)
with col1: st.metric("Número de destinatários",info_geral["Número de destinatários"])
with col2: st.metric("Número de UFs destinatárias",info_geral["Número de ufs destinatárias"])
with col3: st.metric("% de consumidores finais",round(info_geral["Número de consumo"],2))

