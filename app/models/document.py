from tortoise import fields
from tortoise.models import Model
from app.models.user import User
from app.models.folder import Folder

class Document(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(100)
    file_uuid = fields.CharField(100, unique=True)
    size = fields.IntField()
    type = fields.CharField(20)
    uploaded_at = fields.DatetimeField(auto_now_add=True)
    
    owner = fields.ForeignKeyField("models.User", related_name="documents")
    folder = fields.ForeignKeyField("models.Folder", related_name="documents", null=True)
