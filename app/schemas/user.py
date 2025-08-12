from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.user import User
from pydantic import BaseModel, EmailStr

# Schema for returning user details to client
UserPydantic = pydantic_model_creator(
    User, name="User", exclude=["passwrd"]
)

UserSession = pydantic_model_creator(User, name="User", exclude=['passwd'])


# Schema for user creation (input)
UserTempPydantic = pydantic_model_creator(
    User,name="UserIn", exclude_readonly=True, exclude=["is_active"]
)

class UserInPydantic(UserTempPydantic):
  passwd: str

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str