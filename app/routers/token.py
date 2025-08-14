import jwt

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta, timezone

from typing import Annotated

from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.exceptions import DoesNotExist, IntegrityError

from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token

SECRET_KEY = "f38e97b0cd3c4e20aa74d1a61f5c95f6e7dc8341df53f3d0bcbfda62a4b7c477"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

router = APIRouter()

ph = PasswordHasher()
# register route
@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate):
    hashed_pw = ph.hash(user.password)
    try:
        new_user = await User.create(
            email=user.email,
            name=user.name,
            passwd=hashed_pw
        )
        return new_user  # Pydantic will auto-convert to UserOut
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Email already registered")
        
# login route
@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    print("Login attempt:", form_data.username)

    try:
        user = await User.get(email=form_data.username)
        print("User found:", user.email)

        try:
            ph.verify(user.passwd, form_data.password)
            print("Password matched")

            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            payload = {
                "sub": user.email,
                "name": user.name,
                "exp": expire
            }

            access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            print("Access token generated")

            return Token(access_token=access_token, token_type="bearer")

        except VerifyMismatchError:
            print("Password mismatch")
            raise HTTPException(status_code=400, detail="Incorrect username or password")

    except DoesNotExist:
        print("User not found")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
