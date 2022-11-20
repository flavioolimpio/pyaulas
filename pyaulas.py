import streamlit as st
import pandas as pd
import numpy as np
from texts import Texts
from texts_qgb import Texts_QGB
import os
import base64
from streamlit_option_menu import option_menu

st.set_page_config(page_title="PyAulas",layout="wide",initial_sidebar_state="expanded")


aulas_qgb = ['Escolha uma Aula',
'Ligações Químicas', 
'Funções Inorgânicas', 
'Estequiometria', 
'Soluções', 
'Termodinâmica', 
'Eletroquímica', 
'Cinética Química', 
'Equilíbrio Químico',
'Introdução à Química Orgânica', 
'Métodos Clássicos e Instrumentais de Análise']

aulas_qge = ['Escolha uma Aula',
'Apresentação da disciplina, normas de segurança e vidraria básica', 
'Equipamentos básicos de laboratório e Técnicas de Trabalho com Material Volumétrico',
'Densidade de Sólido e Líquidos e a Variação da Densidade em Função da Temperatura',
'Identificação de Metais utilizando o Teste da Chama', 
'Solubilidade de Sólidos em Líquidos', 
'Reações Químicas em Solução Aquosa'
'Preparo de solução', 
'Padronização de Soluções Aquosas',
'Titulação ácido-base: Determinação do teor de ácido acetilsalicílico em comprimido',
'Determinação da acidez no vinagre comercial', 
'Reações de transferências de elétrons']

aulas_fqe = ['Escolha uma Aula',
'Apresentação da disciplina, normas de segurança e vidraria básica', ]

with st.sidebar:
    nav = option_menu("Navegação", ["Página Inicial", 'Química Geral I', 'Química Geral Experimental',  'Contato'], 
        icons=['house-fill', 'book', 'book-fill', 'chat-left-text'], menu_icon="cast", default_index=0)
    nav


@st.cache
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

if nav == 'Química Geral I':
    #st.markdown(get_binary_file_downloader_html('Plano_de_Aula_Quim_Geral_B_Eng_Civil', 'Plano de Curso'), unsafe_allow_html=True)
    link = 'https://drive.google.com/drive/folders/1agv9d5L_VODDFNBFsgRnALLHf4mpmAdT'
    
    st.markdown("Baixar plano de curso:", unsafe_allow_html=True)
    st.markdown(link, unsafe_allow_html=True)
    aula_select = st.selectbox("Selecione a aula: ", aulas_qgb)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Ligações Químicas':
        st.header('Bem-vindo à Aula: Ligações Químicas')
        #getaula = Texts_QGB()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
    elif aula_select == 'Funções Inorgânicas':
        st.header('Bem-vindo à Aula: Funções Inorgânicas',)
        #getaula = Texts_QGB()
        #text2 = getaula.text2()
        #st.write(text2, unsafe_allow_html=True)
    elif aula_select == 'Estequiometria':
        st.header('Bem-vindo à Aula: TÓPICO 3: Estequiometria')
        getaula = Texts_QGB()
        text3 = getaula.text3()
        st.write(text3, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Aula_Estequiometria_atualizada.pdf', 'Baixar Aula'), unsafe_allow_html=True)
    elif aula_select == 'Soluções':
        st.header('Bem-vindo à Aula: Soluções')
        #getaula = pyaula5.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)        
    elif aula_select == 'Termodinâmica':
        st.header('Bem-vindo à Aula: Termodinâmica')
        #getaula = pyaula6.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
    elif aula_select == 'Eletroquímica':
        st.header('Bem-vindo à Aula: Eletroquímica')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Cinética Química':
        st.header('Bem-vindo à Aula: Cinética Química')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Equilíbrio Químico':
        st.header('Bem-vindo à Aula: Equilíbrio Químico')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Introdução à Química Orgânica':
        st.header('Bem-vindo à Aula: Introdução à Química Orgânica')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Métodos Clássicos e Instrumentais de Análise':
        st.header('Bem-vindo à Aula: Métodos Clássicos e Instrumentais de Análise')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()


if nav == 'Química Geral Experimental':
    #st.markdown(get_binary_file_downloader_html('Apostila_QGE_2022_2.pdf', 'Apostila'), unsafe_allow_html=True)
    #st.markdown(get_binary_file_downloader_html('Template_Relatorio_QGE.pdf', 'Template Relatório'), unsafe_allow_html=True)
    st.write(text1, unsafe_allow_html=True)
    aula_select = st.selectbox("Selecione a aula: ", aulas_qge)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Apresentação da disciplina, normas de segurança e vidraria básica':
        st.header('Bem-vindo à Aula: Apresentação da disciplina, normas de segurança e vidraria básica')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Equipamentos básicos de laboratório e Técnicas de Trabalho com Material Volumétrico':
        st.header('Bem-vindo à Aula: Equipamentos básicos de laboratório e Técnicas de Trabalho com Material Volumétrico')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Densidade de Sólido e Líquidos e a Variação da Densidade em Função da Temperatura':
        st.header('Bem-vindo à Aula: Densidade de Sólido e Líquidos e a Variação da Densidade em Função da Temperatura')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Identificação de Metais utilizando o Teste da Chama':
        st.header('Bem-vindo à Aula: Identificação de Metais utilizando o Teste da Chama')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Solubilidade de Sólidos em Líquidos':
        st.header('Bem-vindo à Aula: Solubilidade de Sólidos em Líquidos')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Reações Químicas em Solução Aquosa':
        st.header('Bem-vindo à Aula: Reações Químicas em Solução Aquosa')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Preparo de solução':
        st.header('Bem-vindo à Aula: Preparo de solução')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Padronização de Soluções Aquosas':
        st.header('Bem-vindo à Aula: Padronização de Soluções Aquosas')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Titulação ácido-base: Determinação do teor de ácido acetilsalicílico em comprimido':
        st.header('Bem-vindo à Aula: Titulação ácido-base: Determinação do teor de ácido acetilsalicílico em comprimido')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Determinação da acidez no vinagre comercial':
        st.header('Bem-vindo à Aula: Determinação da acidez no vinagre comercial')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
    elif aula_select == 'Reações de transferências de elétrons':
        st.header('Bem-vindo à Aula: Reações de transferências de elétrons')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()

if nav == 'Contato':

    #st.header(":mailbox: Entre em contato comigo!!")
    st.header("Entre em contato comigo!!")
    contact_form = """
    <form action="https://formsubmit.co/flavio_olimpio@ufg.br" method="post">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Seu nome" optional>
     <input type="email" name="email" placeholder="Seu email" optional>
     <textarea name="message" placeholder="Digite sua mensagem aqui"></textarea>
     <button type="submit">Enviar</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    local_css("style/style.css")
