from fastapi import APIRouter
from app.models.document import Document
from app.schemas.document import DocumentInPydantic, DocumentPydantic

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=DocumentPydantic)
async def upload_document(doc: DocumentInPydantic):
    obj = await Document.create(**doc.dict())
    return await DocumentPydantic.from_tortoise_orm(obj)

@router.get("/", response_model=list[DocumentPydantic])
async def get_documents():
    return await DocumentPydantic.from_queryset(Document.all())
