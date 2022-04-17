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


aulas_qg = ['Escolha uma Aula',
'A matéria e seus estados físicos', 
'Átomos, elementos e compostos',
'Reações e estequiometria',
'Soluções',
'Ligações químicas',
'Termoquímica',
'Equilíbrio químico']

aulas_fq = ['Escolha uma Aula',
'Gases', 
'Termodinâmica',
'Sistemas coloidais e tensão superficial',
'Cinética química']


with st.sidebar:
    nav = option_menu("Navegação", ["Página Inicial", 'Química Geral', 'Físico-Química', 'Contato'], 
        icons=['house-fill', 'book', 'book-fill', 'chat-left-text'], menu_icon="cast", default_index=0)
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
    st.header('Informações Gerais')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)
    st.markdown('{}'.format(text2), unsafe_allow_html=True)
    st.markdown('{}'.format(text3), unsafe_allow_html=True)

if nav == 'Química Geral':
    #st.header('Curso de Química Inorgânica')
    aula_select = st.selectbox("Selecione a aula: ", aulas_qg)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'A matéria e seus estados físicos':
        st.header('Bem-vindo à Aula: A matéria e seus estados físicos')
        #getaula = pyaula1.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_01/Aula_01.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Átomos, elementos e compostos':
        st.header('Bem-vindo à Aula: Átomos, elementos e compostos')
        #getaula = pyaula2.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_02/Aula_02_Ligacoes_quimicas.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Reações e estequiometria':
        st.header('Bem-vindo à Aula: Reações e estequiometria')
        #getaula = pyaula3.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_03/Aula_03.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Soluções':
        st.header('Bem-vindo à Aula: Soluções')
        #getaula = pyaula4.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_04/Aula_04.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Ligações químicas':
        st.header('Bem-vindo à Aula: Ligações químicas')
        #getaula = pyaula5.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_05/Aula_05.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Termoquímica':
        st.header('Bem-vindo à Aula: Termoquímica')
        #getaula = pyaula6.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_06/Aula_06.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Equilíbrio químico':
        st.header('Equilíbrio químico')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_09/equilibrio_quimico.pdf', 'Aula'), unsafe_allow_html=True)

if nav == 'Físico-Química':
    aula_select = st.selectbox("Selecione a aula: ", aulas_fq)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Gases':
        st.header('Bem-vindo à Aula: Gases')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Termodinâmica':
        st.header('Bem-vindo à Aula: Termodinâmica')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Sistemas coloidais e tensão superficial':
        st.header('Bem-vindo à Aula: Sistemas coloidais e tensão superficial')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Cinética química':
        st.header('Bem-vindo à Aula: Cinética química')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)

if nav == 'Contato':

    #st.header(":mailbox: Entre em contato comigo!!")
    st.header("Entre em contato comigo!!")
    contact_form = """
    <form action="https://formsubmit.co/flavio_olimpio@ufg.br" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" optional>
     <input type="email" name="email" placeholder="Seu email" optional>
     <textarea name="message" placeholder="Digite sua mensagem aqui"></textarea>
     <button type="submit">Enviar</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    local_css("style/style.css")


