import streamlit as st
import pandas as pd
import numpy as np
from texts import Texts
import os
import base64
from streamlit_option_menu import option_menu
from Aula_01 import pyaula1
from Aula_02 import pyaula2
from Aula_03 import pyaula3
from Aula_04 import pyaula4
from Aula_05 import pyaula5
from Aula_06 import pyaula6
from Aula_07 import pyaula7
from Aula_08 import pyaula8
from Aula_09 import pyaula9
from Aula_10 import pyaula10

st.set_page_config(page_title="PyAulas",layout="wide",initial_sidebar_state="expanded")


aulas = ['Escolha uma Aula',
'Aula 1 - Estrutura Atômica: átomos multieletrônicos', 
'Aula 2 - Ligação Química e Geometria Molecular',
'Aula 3 - Estequiometria',
'Aula 4 - Reações em meio aquoso',
'Aula 5 - Propriedade dos Gases',
'Aula 6 - 1ª Lei da Termodinâmica',
'Aula 7 - 2ª Lei da Termodinâmica',
'Aula 8 - Eletroquímica',
'Aula 9 - Equilíbrio Químico',
'Aula 10 - Cinética Química']


with st.sidebar:
    nav = option_menu("Navegação", ["Página Inicial", 'Aulas', 'Contato'], 
        icons=['house', 'book', 'chat-left-text-fill'], menu_icon="cast", default_index=0)
    nav

#st.sidebar.markdown('# Navegação:')
#nav = st.sidebar.radio('Ir para:', ['Página Inicial', 'Aulas', 'Contato'])


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f"""<h2 style='text-align: justify; color: black;'><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Baixar {file_label}</a></h2>"""
    return href

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if nav == 'Página Inicial':
    gettext = Texts()
    text1 = gettext.text1()
    text2 = gettext.text2()
    text3 = gettext.text3()
    st.header('Curso de Química Geral')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)
    st.markdown('{}'.format(text2), unsafe_allow_html=True)
    st.markdown('{}'.format(text3), unsafe_allow_html=True)

if nav == 'Aulas':
    #st.header('Curso de Química Inorgânica')
    aula_select = st.selectbox("Selecione a aula: ", aulas)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Aula 1 - Estrutura Atômica: átomos multieletrônicos':
        st.header('Bem-vindo à Aula 1 - Estrutura Atômica: átomos multieletrônicos')
        getaula = pyaula1.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_01/Aula_01.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 2 - Ligação Química e Geometria Molecular':
        st.header('Bem-vindo à Aula 2 - Ligação Química e Geometria Molecular')
        getaula = pyaula2.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_02/Aula_02_Ligacoes_quimicas.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 3 - Estequiometria':
        st.header('Bem-vindo à Aula 3 - Estequiometria')
        getaula = pyaula3.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_03/Aula_03.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 4 - Reações em meio aquoso':
        st.header('Bem-vindo à Aula 4 - Reações em meio aquoso')
        getaula = pyaula4.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_04/Aula_04.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 5 - Propriedade dos Gases':
        st.header('Bem-vindo à Aula 5 - Propriedade dos Gases')
        getaula = pyaula5.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_05/Aula_05.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 6 - 1ª Lei da Termodinâmica':
        st.header('Bem-vindo à Aula 6 - 1ª Lei da Termodinâmica')
        getaula = pyaula6.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_06/Aula_06.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 7 - 2ª Lei da Termodinâmica':
        st.header('Bem-vindo à Aula 7 - 2ª Lei da Termodinâmica')
        getaula = pyaula7.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_07/Aula_07_Entropy.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 8 - Eletroquímica':
        st.header('Bem-vindo à Aula 8 - Eletroquímica')
        getaula = pyaula8.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_08/Aula_08_UFG.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 9 - Equilíbrio Químico':
        st.header('Bem-vindo à Aula 9 - Equilíbrio Químico')
        getaula = pyaula9.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_09/equilibrio_quimico.pdf', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Aula 10 - Cinética Química':
        st.header('Bem-vindo à Aula 10 - Cinética Química')
        getaula = pyaula10.Texts()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)

if nav == 'Contato':

    #st.header(":mailbox: Entre em contato comigo!!")
    st.header("Entre em contato comigo!!")
    contact_form = """
    <form action="https://formsubmit.co/flavio_olimpio@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" optional>
     <input type="email" name="email" placeholder="Seu email" optional>
     <textarea name="message" placeholder="Digite sua mensagem aqui"></textarea>
     <button type="submit">Enviar</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    local_css("style/style.css")


