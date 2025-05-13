# My Archy

**My Archy** es un asistente virtual basado en inteligencia artificial, desarrollado como parte de mi Trabajo de Fin de Grado en Ingeniería Informática. Utiliza la técnica **RAG (Retrieval-Augmented Generation)**, que combina búsqueda inteligente de información con generación de texto, para ofrecer respuestas contextualizadas, rápidas y autónomas a preguntas en lenguaje natural basadas en documentación técnica sobre RSA Archer.


## 📌 Funcionalidad

- Carga y analiza documentos PDF del sistema Archer.
- Genera embeddings (vectores semánticos) a partir del contenido.
- Recupera fragmentos relevantes usando la técnica RAG (Retrieval-Augmented Generation).
- Responde preguntas técnicas usando solo la documentación proporcionada.
- Conserva el historial de conversación y calcula tiempos de respuesta.
- Incluye una interfaz moderna e interactiva con Streamlit.
- Muestra métricas técnicas (número de consultas, documentos, tiempos, etc.).


## 🚀 Tecnologías utilizadas

- **Python 3.x**
- [Streamlit](https://streamlit.io/)
- [llama-index](https://docs.llamaindex.ai/)
- [Ollama](https://ollama.com/) – para ejecutar modelos LLM localmente
- [Mistral 7B Instruct](https://ollama.com/library/mistral)


## 💻 Requisitos

Instala las dependencias necesarias ejecutando:
```text
pip install -r requirements.txt
```

🔽 Descargar el modelo Mistral (una vez)

My Archy utiliza el modelo Mistral 7B Instruct a través del servidor local Ollama.
Este modelo no viene preinstalado, por lo que es necesario descargarlo manualmente la primera vez:
```text
ollama run mistral:7b-instruct-v0.2-q4_K_M
```

## ▶️ Cómo usar
### 1. Iniciar el servidor Ollama
Primero, asegúrate de que Ollama está en ejecución. Desde la terminal:
```text
ollama serve
```
### 2. Cargar documentos (opcional, solo si vas a indexar nuevos PDFs)
Coloca tus archivos `.pdf` dentro de la carpeta `data/`
Luego ejecuta en la terminal: 
```text
python -m src.ingest
```
### 3. Iniciar My Archy
Activa tu entorno virtual y lanza la interfaz de usuario:
```text
cd ~/my-archy
source env/bin/activate
streamlit run app.py
```
La aplicación se abrirá en tu navegador. Desde ahí podrás interactuar con My Archy escribiendo tus preguntas.

## 🧪 Ejemplo de uso
- **Pregunta:**
  ```text
  ¿Qué es Archer?
  ```

- **Respuesta generada:**  
  Archer es una plataforma de gestión de riesgos y compliancia desarrollada por SAS Institute. Permite a las organizaciones automatizar, administrar y analizar 
  procesos de riesgo y compliancia en un solo lugar. Ofrece funcionalidades como creación de aplicaciones personalizadas, diseño de interfaz intuitiva, definición 
  de flujos de trabajo avanzados, configuración del orden de ejecución de campos calculados y control de acceso a usuarios y permisos.


## 📊 Métricas disponibles

Desde la interfaz, se pueden consultar:
- Número total de consultas realizadas.
- Tiempo medio de respuesta.
- Última pregunta enviada.
- Número de documentos cargados.

## 🗂️ Estructura del proyecto
  ```text
├── app.py # Interfaz principal en Streamlit
├── chat.py # Motor de conversación
├── config.py # Configuración global del sistema
├── ingest.py # Procesamiento e indexación de PDFs
├── exceptions.py # Manejo personalizado de errores
├── requirements.txt # Dependencias del proyecto
├── data/ # Documentación de Archer en PDFs
├── storage/ # Índices generados 
├── env/ # Entorno virtual
  ```

## 👩‍💻 Autora
Lucía Gutiérrez Cano
Trabajo de Fin de Grado – Ingeniería Informática
