class ArcherAIException(Exception):
    """Base exception para errores personalizados"""
    
class IngestionError(ArcherAIException):
    """Errores durante el procesamiento de documentos"""
    
class ChatEngineError(ArcherAIException):
    """Errores en el motor de chat"""
    
class ConfigurationError(ArcherAIException):
    """Errores de configuración"""