from .user import router as user_router
from .folder import router as folder_router
from .document import router as document_router
from .file_router import router as file_router

__all__ = ["user_router", "folder_router", "document_router", "file_router"]
