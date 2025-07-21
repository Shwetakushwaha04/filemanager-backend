from fastapi import APIRouter
from app.models.folder import Folder
from app.schemas.folder import FolderPydantic, FolderInPydantic

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/", response_model=FolderPydantic)
async def create_folder(folder: FolderInPydantic):
    obj = await Folder.create(**folder.dict())
    return await FolderPydantic.from_tortoise_orm(obj)

@router.get("/", response_model=list[FolderPydantic])
async def list_folders():
    return await FolderPydantic.from_queryset(Folder.all())
