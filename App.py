# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:31:39 2023

@author: Josa -- josageof@gmail.com
"""

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="byCubes -- Soluções b2b", 
                   page_icon="🎯", 
                   layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")



#%% ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/4f8be7d8-b9ab-4a41-b7a9-c13a5f65af48/KzBJo8MfJu.json")
img_lottie_animation = Image.open("assets/trellodash.png")
img_contact_form = Image.open("assets/bycubes_view.png")



#%% ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("#")
        st.subheader("Eu sou a byCubes :wave:")
        st.title("Especialista em _Gestão_ por _Análise de Dados_")
        st.write(
            '''🎯 Determinada em transformar a gestão em algo acessível, inteligente e, acima de tudo, divertido.
            
            " Te mostrarei como faremos dos números e estratégias os seus melhores amigos 📈 "'''
        )
        st.write("[Conheça também o meu auxiliar >](https://www.linkedin.com/in/josageof/)")
    with right_column:
        _left, mid, _right = st.columns(3)
        with mid:
            st.write("##")
            st.image("assets/animation-rocket_cutted.gif")



#%% ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1, 1))
    with left_column:
        st.header("O que eu faço? Vou te contar um pouco 🦜")
        st.write("##")
        st.markdown(
            """
            Para início de conversa, não vou te bombardear com termos complicados. A ideia é te levar na cara do gol ⚽:

            - Com simples análises, Vou mostrar o que os teus <span style="font-size: 18px; text-decoration: underline; color: orange;">dados</span> realmente estão tentando dizer;<br>
            - Vamos transformar sua <span style="font-size: 18px; text-decoration: underline; color: orange;">gestão de projetos</span> em uma aventura emocionante e sem estresse;<br>
            - O <span style="font-size: 18px; text-decoration: underline; color: orange;">engajamento</span> do seu time, levará a sua produtividade a um nível jamais visto antes;<br>
            - Mapearemos cada detalhe dos <span style="font-size: 18px; text-decoration: underline; color: orange;">novos clientes</span>, de tal forma que até a tia do café vai vender. ☕<br>

            Não estou propondo mágica ou arte, é apenas ciência 👩‍🔬.
            """, unsafe_allow_html=True
        )
        st.write("[💬 Fale pelo WhatsApp >](https://wa.me/qr/EGQ6JJJBAG3XP1)")
    with right_column:
        # st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/josageof@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Seu nome" required>
            <input type="email" name="email" placeholder="Seu e-mail" required>
            <textarea name="message" placeholder="Sua mensagem aqui" required></textarea>
            <button type="submit">Enviar</button>
        </form>
        """
        _left, mid, _right = st.columns((1,5,1))
        with mid:
            st.write("#### Aproveita e me manda logo uma mensagem?")
            st.markdown(contact_form, unsafe_allow_html=True)



# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Meus projetos recentes")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Desperte o Potencial da Sua Equipe com Nosso Dashboard Inovador!")
        st.markdown(
            """
            📊  Conheça essa ferramenta que vai transformar o <span style="color: orange;">desempenho</span> da sua equipe, promovendo o engajamento genuíno e a autogestão 😃.<br>
            Com ela você terá um resumo do seu time em diferentes escalas: <span style="color: orange;">semanal</span>, <span style="color: orange;">mensal</span> e <span style="color: orange;">anual</span>. 
            Seja por <span style="color: orange;">esforço</span>, <span style="color: orange;">tempo</span> e/ou <span style="color: orange;">estado</span> dos recursos.<br>
            Ah, você gosta do <span style="color: orange;">Tello</span>? Ela importa os dados, processa e leva a informação as suas mãos. E o melhor: nem precisa ser Premium 💰.<br>
            Juntos, podemos transformar a sua gestão e levar o seu time a novos patamares de sucesso 🚀. 
            """, unsafe_allow_html=True
        )
        st.markdown("[Veja no LinkedIn...](https://www.linkedin.com/posts/josageof_transform-your-trello-board-management-https-activity-7053756227507396609-O9XQ?utm_source=share&utm_medium=member_desktop)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Aproveite as Facilidades desse DataViz Interativo, Moderno e Flexível")
        st.markdown(
            """
            🚀 Confira essa ferramenta desenvolvida para tornar a análise de dados mais <span style="color: orange;">acessível</span> e <span style="color: orange;">eficaz</span>!<br>
            Há informações sobre <span style="color: orange;">diversos tópicos</span> relevantes e todos os gráficos e mapas são <span style="color: orange;">interativos</span>.<br>
            E sabe a melhor parte? A adição de <span style="color: orange;">novos dados</span> é ilimitada, basta você solicitar...<br>
            ⛵ Navegue, escolha o que deseja ver, analise e tire suas conclusões...📊💡
            """, unsafe_allow_html=True
        )
        st.markdown("[Utilize agora...](https://bycubes-view.streamlit.app)")
