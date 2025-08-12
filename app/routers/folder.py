from fastapi import APIRouter
from app.models.folder import Folder
from app.schemas.folder import FolderPydantic, FolderInPydantic
from app.lib.gcu import gcu

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/", response_model=FolderPydantic)
async def create_folder(folder: FolderInPydantic, user= gcu):
    obj = await Folder.create(**folder.dict(), user=user)
    return await FolderPydantic.from_tortoise_orm(obj)

@router.get("/", response_model=list[FolderPydantic])
async def list_folders(user= gcu):
    folders = await Folder.filter(user=user)
    return await FolderPydantic.from_queryset(Folder.all())

