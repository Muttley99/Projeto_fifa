import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

arquivo = r"C:\Users\vinil\OneDrive\Documents\ASIMOV ACADEMY PYTHON\Streamlit\Projeto Streamlit FIFA\datasets\CLEAN_FIFA23_official_data.csv"
if "data" not in st.session_state:
    df_data= pd.read_csv(arquivo,index_col=0)
    df_data['Contract Valid Until']=df_data['Contract Valid Until'].apply(int)
    hoje = datetime.today().year
    df_data = df_data[df_data["Contract Valid Until"] >= hoje]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data
df_data = st.session_state["data"]


st.markdown('# FIFA 2023 DATASET! ⚽️')
st.markdown('Desenvolvido por [Asimov Academy](https://asimov.academy)')
btn = st.button('Acesse os dados no Kaggle')

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)

