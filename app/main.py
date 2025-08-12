from app.db.db import init_db
from fastapi import FastAPI
from app.routers import file, user, folder, document, token


app = FastAPI()

app.include_router(user.router, tags=["Users"])
app.include_router(folder.router, tags=["Folders"])
app.include_router(document.router, tags=["Documents"])
app.include_router(file.router, prefix="/files", tags=["Files"])
app.include_router(token.router, tags=["Auth"]) 

init_db(app)

