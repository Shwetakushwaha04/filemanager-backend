from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    email = fields.CharField(100, unique=True)
    password = fields.CharField(128)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username
