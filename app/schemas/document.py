from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.document import Document

# schema for returning to clients
DocumentPydantic = pydantic_model_creator(
    Document, name="Document", exclude=["user"]
)

# Input schema for creating new documents
DocumentInPydantic = pydantic_model_creator(
    Document, name="DocumentIn", exclude_readonly=True, exclude=["user_id"]
)
