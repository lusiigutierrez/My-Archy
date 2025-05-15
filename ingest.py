from pathlib import Path
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from .config import AppConfig
from .exceptions import IngestionError

# Usar Mistral local (cuantizado) para generar embeddings
Settings.embed_model = OllamaEmbedding(model_name="mistral:7b-instruct-v0.2-q4_K_M")

class DocumentProcessor:
    @staticmethod
    def validate_directory(path: Path):
        if not path.exists():
            raise IngestionError(f"No se encuentra la carpeta: {path}.")
        if not any(path.iterdir()): #mira si dentro del path haay al menos uno pdf
            raise IngestionError(f"En la carpeta {path} no se encuentra ningún pdf.")

    @classmethod
    def process_documents(cls):
        try:
            cls.validate_directory(AppConfig.DATA_DIR)
            
            documents = SimpleDirectoryReader(
                str(AppConfig.DATA_DIR),
                filename_as_id=True
            ).load_data() #lee los documentos y los convierte en texto

            index = VectorStoreIndex.from_documents( #convierte los documentos en vectores
                documents,
                show_progress=True 
            )
            
            index.storage_context.persist(
                persist_dir=str(AppConfig.STORAGE_DIR) #gurada el indice en storage
            )
            
            return True
            
        except Exception as e:
            raise IngestionError(f"Error al procesar los documentos: {str(e)}")
        

if __name__ == "__main__":
    print("Se encuentran en quirófano los pdf...")
    try:
        result = DocumentProcessor.process_documents()
        if result:
            print("Operación perfecta !!✅")
    except IngestionError as e:
        print(f"❌ Error durante la operación: {e}")