from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.user import User

# Schema for returning user details to client
UserPydantic = pydantic_model_creator(
    User, name="User", exclude=["password"]
)

# Schema for user creation (input)
UserInPydantic = pydantic_model_creator(
    User,name="UserIn", exclude_readonly=True, exclude=["is_active"]
)