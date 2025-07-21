from tortoise import fields
from tortoise.models import Model
from app.models.user import User

class Folder(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(100)
    created_at = fields.DatetimeField(auto_now_add=True)
    
    owner = fields.ForeignKeyField("models.User", related_name="folders")
