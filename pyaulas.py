import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from texts import Texts
import os
import base64
from Aula2 import pyaula2
from Aula3 import pyaula3
from Aula4 import pyaula4
from Aula5 import pyaula6
from Aula6 import pyaula6

st.set_page_config(page_title="PyAulas",layout="wide",initial_sidebar_state="expanded")


aulas = ['Escolha uma Aula',
'Aula 1 - Elementos dos blocos s, p, d e f', 
'Aula 2 - Sólidos iônicos: estrutura e entalpia de rede',
'Aula 3 - Ligação química e geometria molecular',
'Aula 4 - Orbitais moleculares de moléculas diatômicas',
'Aula 5 - Reações de oxirredução: estabilidade redox e diagramas de representação',
'Aula 6 - Ácidos e bases duros e moles: aplicações do conceito a complexos metálicos',
'Aula 7 - Simetria molecular e grupos pontuais',
'Aula 8 - Complexos de metais de transição: campo cristalino e campo ligante',
'Aula 9 - Espectroscopia eletrônica de compostos de coordenação',
'Aula 10 - Organometálicos de metais de transição do bloco d: reações e aplicações em catálise']


st.sidebar.markdown('# Navegação:')
nav = st.sidebar.radio('Ir para:', ['Página Inicial', 'Aulas'])


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f"""<h2 style='text-align: justify; color: black;'><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Baixar {file_label}</a></h2>"""
    return href

if nav == 'Página Inicial':
    gettext = Texts()
    text1 = gettext.text1()
    text2 = gettext.text2()
    text3 = gettext.text3()
    #st.header('## Curso de Química Inorgânica')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)
    st.markdown('{}'.format(text2), unsafe_allow_html=True)
    st.markdown('{}'.format(text3), unsafe_allow_html=True)

if nav == 'Aulas':
    #st.header('Curso de Química Inorgânica')
    aula_select = st.selectbox("Selecione a aula: ", aulas)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Aula 1 - Elementos dos blocos s, p, d e f':
        st.header('Bem vindo a Aula 1 - Elementos dos blocos s, p, d e f')
    elif aula_select == 'Aula 2 - Sólidos iônicos: estrutura e entalpia de rede':
        getaula = pyaula2.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula2/Aula2_SolidosIonicos.ppt', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 3 - Ligação química e geometria molecular':
        getaula = pyaula3.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula3/Ligacoes_quimicas.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 4 - Orbitais moleculares de moléculas diatômicas':
        getaula = pyaula4.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula4/OrbitaisMoleculares.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 5 - Reações de oxirredução: estabilidade redox e diagramas de representação':
        getaula = pyaula5.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula4/OrbitaisMoleculares.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 6 - Ácidos e bases duros e moles: aplicações do conceito a complexos metálicos':
        getaula = pyaula6.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula4/OrbitaisMoleculares.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 7 - Simetria molecular e grupos pontuais':
        st.header('Bem vindo a Aula 7 - Simetria molecular e grupos pontuais')
    elif aula_select == 'Aula 8 - Complexos de metais de transição: campo cristalino e campo ligante':
        st.header('Bem vindo a Aula 8 - Complexos de metais de transição: campo cristalino e campo ligante')
    elif aula_select == 'Aula 9 - Espectroscopia eletrônica de compostos de coordenação':
        st.header('Bem vindo a Aula 9 - Espectroscopia eletrônica de compostos de coordenação')
    elif aula_select == 'Aula 10 - Organometálicos de metais de transição do bloco d: reações e aplicações em catálise':
        st.header('Bem vindo a Aula 10 - Organometálicos de metais de transição do bloco d: reações e aplicações em catálise')
