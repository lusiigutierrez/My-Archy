import streamlit as st
import time
import os
import random
import base64
from src.config import AppConfig
from src.chat import ArcherChatEngine
from src.exceptions import ChatEngineError

st.set_page_config(
    page_title="My Archy",
    page_icon="🤖",
    layout="wide"
)


AppConfig.setup_llm()
chat_engine = ArcherChatEngine()


#Estilo de la interfaz
def interface_style():
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background-color: #1c2b36;
            color: white;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }

        .stChatMessage {
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .stChatMessage.user {
            background-color: #ffe6e6;
            color: #5c0000;
        }

        .stChatMessage.assistant {
            background-color: #e6f7ff;
            color: #004466;
        }

        .stTextInput > div > div > input {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 8px;
            font-size: 1rem;
            color: #333;
        }

        .sidebar-logo-container {
            text-align: center;
            margin-top: 1rem;
        }

        .sidebar-logo-container img {
            width: 100px;
            border-radius: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }

        .sidebar-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 0.5rem;
            color: white;
        }

        .sidebar-subtitle {
            text-align: center;
            font-size: 0.9rem;
            color: #ccc;
            margin-bottom: 1.5rem;
        }

        .stButton > button {
            background-color: #ffffff11;
            color: white;
            border: 1px solid #ffffff33;
            border-radius: 6px;
        }

     
        .stCheckbox label,
        .stCheckbox div,
        .stCheckbox span,
        section[data-testid="stSidebar"] label {
            color: #f0f0f0 !important;
        }

        footer {visibility: hidden;}
        section[data-testid="stSidebar"] *:focus,
        .block-container *:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.5);
        }

        html, body {
            border-top: none !important;
        }
        *, *:focus {
            outline: none !important;
            box-shadow: none !important;
            border-color: transparent !important;
        }

        header[data-testid="stHeader"] {
            background: none !important;
            border: none !important;
            box-shadow: none !important;
        }

        div[data-testid="stDecoration"] {
            background: none !important;
            box-shadow: none !important;
        }
        .stButton > button:hover {
            background-color: #ff80bf !important;
            border-color: #ff66aa !important;
            color: white !important;
        }

        hr {
            border: none;
            border-top: 1px solid #ccc;
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)


#Frases para el titulo aleatorias. 
frases_creativas = [
    "My Archy te enseña y nunca se queja, trabaja contigo y todo lo despeja.",
    "Pregúntale a Archy, no es ningún parche, responde seguro, ¡directo y sin embrollos!",
    "Con My Archy no te lías, todo fluye y lo dominas.",
    "My Archy no falla, responde y detalla.",
    "La duda te atrapa… ¡Archy la desata!",
    "My Archy te guía, optimiza tu día.",
    "Tu aliado perfecto, preciso y directo.",
    "Conocimiento claro, soporte diario.",
    "Sin rodeos ni prisas: respuestas precisas.",
    "My Archy no improvisa, consulta y analiza.",
    "Donde hay caos documental, Archy es esencial.",
    "Tus PDFs son un lío… Archy dice: desafío asumido."
]

frase_aleatoria = random.choice(frases_creativas)


#Para poner fotos con st.markdown() es necesario pasar la imagen a texto codificado en base64
def get_base64_logo():
    logo_path = AppConfig.ASSETS_DIR / "logo.png"
    with open(logo_path, "rb") as image_file: #lee la imagen en modo lectura binaria y la guarda en image_file
        return base64.b64encode(image_file.read()).decode() #bytes binarios se convierten en una cadena codificada en base64 que pasa a una cadena de texto normal 
    


#Cuenta los pdf que hay en la carpeta data
def get_loaded_documents_count():
    try:
        return len([f for f in os.listdir(AppConfig.DATA_DIR) if f.endswith(".pdf")])
    except Exception:
        return 0


#Muestra las metricas tecnicas 
def show_metrics():
    st.markdown("## 📊 Métricas Técnicas")
    total_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
    total_time = st.session_state.get("total_response_time", 0)
    total_responses = st.session_state.get("response_count", 1)
    avg_time = total_time / total_responses

    last_question = ""
    for msg in reversed(st.session_state.messages):
        if msg["role"] == "user":
            last_question = msg["content"]
            break

    st.metric("🧠 Consultas realizadas", total_messages)
    st.metric("⏱ Tiempo medio de respuesta", f"{avg_time:.2f} s") #.2f para que muestre solo dos decimales 
    st.metric("📌 Última consulta", last_question if last_question else "Ninguna")
    st.metric("📁 Documentos cargados", get_loaded_documents_count())


#Toda la interfaz
def setup_interface():
    interface_style()

    st.sidebar.markdown(f"""
        <div class="sidebar-logo-container">
            <img src="data:image/png;base64,{get_base64_logo()}" alt="Logo Archy" />
            <div class="sidebar-title">My Archy</div>
            <div class="sidebar-subtitle">Tu asistente técnico</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style='text-align: center; font-size: 3rem; color: #003366;'>My Archy</h1>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <p style='text-align: center; font-size: 1.2rem; color: #444;'>{frase_aleatoria}</p>
        <div style='height:1px; background-color:#ccc; margin:2rem 0;'></div>
    """, unsafe_allow_html=True) #Para que interprete el HTML


#Arranca 
def main():
    setup_interface()

    st.sidebar.title("⚙️ Opciones")
    mostrar_metricas = st.sidebar.checkbox("📊 Mostrar métricas técnicas", key="show_metrics")
    st.sidebar.markdown("---")

    if st.sidebar.button("🔄 Nueva conversación"):
        st.session_state.messages = [
            {"role": "assistant", "content": "¿En qué puedo ayudarte con Archer hoy?"}
        ]
        st.session_state.total_response_time = 0
        st.session_state.response_count = 1
        st.rerun() #recarga toda la pagina 

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¿En qué puedo ayudarte con Archer hoy?"}
        ]
    if "total_response_time" not in st.session_state:
        st.session_state.total_response_time = 0
    if "response_count" not in st.session_state:
        st.session_state.response_count = 1

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_input := st.chat_input("Escribe tu consulta técnica..."):
        try:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.write(user_input)

            with st.chat_message("assistant"):
                start_time = time.time()
                response = chat_engine.chat(user_input) #Se genera aquí la respuesta.
                full_response = ""
                container = st.empty()
                for token in response.response_gen: #respuesta con el efecto maquina de escribir 
                    full_response += token
                    container.markdown(full_response + "▌")
                    time.sleep(0.02)
                container.markdown(full_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )
                end_time = time.time()
                duration = end_time - start_time
                st.session_state.total_response_time += duration
                st.session_state.response_count += 1

        except ChatEngineError as e:
            st.error(f"🚨 Error técnico: {str(e)}")

    if mostrar_metricas:
        show_metrics()

    st.markdown("""<div style='height:1px; background-color:#ccc; margin:2rem 0;'></div>""", unsafe_allow_html=True)
    st.markdown(
        "<center><small>🧠 Desarrollado por Lucía Gutiérrez Cano · 2025</small></center>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    try:
        chat_engine.initialize() #inicializa el motor
        main()
    except Exception as e:
        st.error(f"⚠️ Error crítico: {str(e)}. Verifica los documentos en /data")
