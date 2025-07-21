from app.db.db import init_db
from fastapi import FastAPI
from app.routers import file, user, folder, document


app = FastAPI()

app.include_router(user.router)
app.include_router(folder.router)
app.include_router(document.router)
app.include_router(file.router)


init_db(app)


app.include_router(file.router, prefix="/files", tags=["Files"])
