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
'TÓPICO 1: ALGUNS CONCEITOS IMPORTANTES PARA QUÍMICA', 
'TÓPICO 2: MODELOS ATÔMICOS',
'TÓPICO 3: SUBSTÂNCIAS E ALGUMAS DE SUAS PROPRIEDADES',
'TÓPICO 4: INTRODUÇÃO À LIGAÇÃO QUÍMICA A PARTIR DO MODELO ORBITAL',
'TÓPICO 5: ESTEQUIOMETRIA E REAÇÕES QUÍMICAS: POR QUE OCORREM?',
'TÓPICO 6: O QUE É UM SISTEMA EM EQUILÍBRIO QUÍMICO?']

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


with st.sidebar:
    nav = option_menu("Navegação", ["Página Inicial", 'Química Geral B', 'Química Geral Experimental', 'Contato'], 
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

if nav == 'Química Geral B':
    #st.header('Curso de Química Inorgânica')
    st.markdown(get_binary_file_downloader_html('QuimicaGeralB/Plano_de_Aula_QuimicaGeralB_pyAulas.pdf', 'Plano de Curso'), unsafe_allow_html=True)
    st.markdown(get_binary_file_downloader_html('QuimicaGeralB/lista_de_exercicios_quimica_geral.pdf', 'Plano de Curso'), unsafe_allow_html=True)
    aula_select = st.selectbox("Selecione a aula: ", aulas_qgb)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'TÓPICO 1: ALGUNS CONCEITOS IMPORTANTES PARA QUÍMICA':
        st.header('Bem-vindo à Aula: TÓPICO 1: ALGUNS CONCEITOS IMPORTANTES PARA QUÍMICA')
        getaula = Texts_QGB()
        text1 = getaula.text1()
        st.write(text1, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Topico_01_Materia.pdf', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'TÓPICO 2: MODELOS ATÔMICOS':
        st.header('Bem-vindo à Aula: TÓPICO 2: MODELOS ATÔMICOS')
        getaula = Texts_QGB()
        text2 = getaula.text2()
        st.write(text2, unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html('Topico_02_Estrutura_Atomica.pdf', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'TÓPICO 3: SUBSTÂNCIAS E ALGUMAS DE SUAS PROPRIEDADES':
        st.header('Bem-vindo à Aula: TÓPICO 3: SUBSTÂNCIAS E ALGUMAS DE SUAS PROPRIEDADES')
        #getaula = pyaula3.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_03_reacoes.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'TÓPICO 4: INTRODUÇÃO À LIGAÇÃO QUÍMICA A PARTIR DO MODELO ORBITAL':
        st.header('Bem-vindo à Aula: TÓPICO 4: INTRODUÇÃO À LIGAÇÃO QUÍMICA A PARTIR DO MODELO ORBITAL')
        #getaula = pyaula5.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)        
        #st.markdown(get_binary_file_downloader_html('exercicios_lista_ligacao_quimica.pdf', 'Exercicio Lista'), unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_Ligacoes_quimicas.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'TÓPICO 5: ESTEQUIOMETRIA E REAÇÕES QUÍMICAS: POR QUE OCORREM?':
        st.header('Bem-vindo à Aula: TÓPICO 5: ESTEQUIOMETRIA E REAÇÕES QUÍMICAS: POR QUE OCORREM?')
        #getaula = pyaula6.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_06_Termodinamica.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'TÓPICO 6: O QUE É UM SISTEMA EM EQUILÍBRIO QUÍMICO?':
        st.header('TÓPICO 6: O QUE É UM SISTEMA EM EQUILÍBRIO QUÍMICO?')
        #getaula = pyaula9.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('LISTA_02_QG.pdf', 'Baixar Lista 2'), unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_Equilibrio_Quimico.pptx', 'Aula'), unsafe_allow_html=True)


if nav == 'Química Geral Experimental':
    st.markdown(get_binary_file_downloader_html('QGE/PLANO_DE_AULA_QGE_pyaulas.pdf', 'Plano de Curso'), unsafe_allow_html=True)
    st.markdown(get_binary_file_downloader_html('QGE/Apostila_QGE_2022_Prof_Flavio.pdf', 'Apostila'), unsafe_allow_html=True)
    #st.markdown(get_binary_file_downloader_html('lista_01_FQ.pdf', 'LISTA 01'), unsafe_allow_html=True)
    aula_select = st.selectbox("Selecione a aula: ", aulas_qge)
    if aula_select == 'Escolha uma Aula':
        pass
    elif aula_select == 'Apresentação da disciplina, normas de segurança e vidraria básica':
        st.header('Bem-vindo à Aula: Apresentação da disciplina, normas de segurança e vidraria básica')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_05_gases.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Equipamentos básicos de laboratório e Técnicas de Trabalho com Material Volumétrico':
        st.header('Bem-vindo à Aula: Equipamentos básicos de laboratório e Técnicas de Trabalho com Material Volumétrico')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_06_Termodinamica.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Densidade de Sólido e Líquidos e a Variação da Densidade em Função da Temperatura':
        st.header('Bem-vindo à Aula: Densidade de Sólido e Líquidos e a Variação da Densidade em Função da Temperatura')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Identificação de Metais utilizando o Teste da Chama':
        st.header('Bem-vindo à Aula: Identificação de Metais utilizando o Teste da Chama')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Solubilidade de Sólidos em Líquidos':
        st.header('Bem-vindo à Aula: Solubilidade de Sólidos em Líquidos')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Reações Químicas em Solução Aquosa':
        st.header('Bem-vindo à Aula: Reações Químicas em Solução Aquosa')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Preparo de solução':
        st.header('Bem-vindo à Aula: Preparo de solução')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Padronização de Soluções Aquosas':
        st.header('Bem-vindo à Aula: Padronização de Soluções Aquosas')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10/Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Titulação ácido-base: Determinação do teor de ácido acetilsalicílico em comprimido':
        st.header('Bem-vindo à Aula: Titulação ácido-base: Determinação do teor de ácido acetilsalicílico em comprimido')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Determinação da acidez no vinagre comercial':
        st.header('Bem-vindo à Aula: Determinação da acidez no vinagre comercial')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)
    elif aula_select == 'Reações de transferências de elétrons':
        st.header('Bem-vindo à Aula: Reações de transferências de elétrons')
        #getaula = pyaula10.Texts()
        #text1 = getaula.text1()
        #st.write(text1, unsafe_allow_html=True)
        #st.markdown(get_binary_file_downloader_html('Aula_10.pptx', 'Aula'), unsafe_allow_html=True)

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


