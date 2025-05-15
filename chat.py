from llama_index.core import load_index_from_storage, StorageContext
from .config import AppConfig
from .exceptions import ChatEngineError

class ArcherChatEngine:
    def __init__(self):
        self._engine = None #motor hablador se inicia apagado 
    
        
    def initialize(self): #cuando se arranca el motor 
        try:
            storage_context = StorageContext.from_defaults(
                persist_dir=str(AppConfig.STORAGE_DIR)
            )
            
            index = load_index_from_storage(storage_context) #se carga un indice con los embeddings ya generados
            
            self._engine = index.as_chat_engine( #motor listo para recibir preguntas y responder
                chat_mode="context",
                similarity_top_k=3, #3 partes que mas separecen 
                verbose=False #no logs por pantalla
            )
            
        except Exception as e:
            raise ChatEngineError(f"Error inicializando motor: {str(e)}")

    def chat(self, query: str): #recibe la pregunta del usuario
        if not self._engine:
            raise ChatEngineError("Motor no inicializado")
            
        try:
            return self._engine.stream_chat(query) #genera la respuesta
        except Exception as e:
            raise ChatEngineError(f"Error generando respuesta: {str(e)}")