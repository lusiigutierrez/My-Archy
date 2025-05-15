from pathlib import Path
from llama_index.core import Settings #Configuracion de la IA
from llama_index.embeddings.ollama import OllamaEmbedding #Uso de vectores de Ollama
from llama_index.llms.ollama import Ollama #Modelo de lenguaje de Ollama

class AppConfig:
    # Directorios
    DATA_DIR = Path("data")
    STORAGE_DIR = Path("storage")
    ASSETS_DIR = Path("assets")
    
    # Modelo
    EMBED_MODEL = "mistral"
    LLM_MODEL = "mistral:7b-instruct-v0.2-q4_K_M"
    #Large language model 

    
    # Parámetros técnicos
    CHUNK_SIZE = 512 #textos en bloques de 512 palabras
    CHUNK_OVERLAP = 64 #solapa 64 palabras entre bloque y bloque
    TEMPERATURE = 0.3 #Creatividad de la IA (0 muy seria - 1 creativa)
    CONTEXT_WINDOW = 4096 #Puede manejar a la vez 4096 tokens (palabras) -> Mistral por defecto suele tener 4096


    @classmethod
    def setup_llm(cls):
        Settings.embed_model = OllamaEmbedding(model_name=cls.EMBED_MODEL)
        Settings.llm = Ollama(
            model=cls.LLM_MODEL,
            temperature=cls.TEMPERATURE,
            num_ctx=cls.CONTEXT_WINDOW,
            request_timeout=120,
            system_prompt="Eres un experto en RSA Archer. Responde siempre en ESPAÑOL usando SOLO los documentos proporcionados."
        )

