from fastapi import APIRouter
from app.schemas.user import UserPydantic, UserInPydantic
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserPydantic)
async def create_user(user: UserInPydantic):
    obj = await User.create(**user.dict())
    return await UserPydantic.from_tortoise_orm(obj)

@router.get("/{user_id}", response_model=UserPydantic)
async def get_user(user_id: int):
    return await UserPydantic.from_queryset_single(User.get(id=user_id))
