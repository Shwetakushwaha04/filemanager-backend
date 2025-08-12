import jwt
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from app.models.user import User
from app.schemas.user import UserSession

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "f38e97b0cd3c4e20aa74d1a61f5c95f6e7dc8341df53f3d0bcbfda62a4b7c477"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")
    if email is None:
      raise credentials_exception
    user = await UserSession.from_queryset_single(User.get(email=email))
    return user
  except InvalidTokenError:
    raise credentials_exception

gcu = Annotated[UserSession, Depends(get_current_user)]