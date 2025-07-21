from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.folder import Folder

# Schema for returning folder data
FolderPydantic = pydantic_model_creator(
    Folder, name="Folder", exclude=["user"]
)

# Schema for folder creation (input)
FolderInPydantic = pydantic_model_creator(
    Folder, name="FolderIn", exclude_readonly=True, exclude=["user_id"]
)
