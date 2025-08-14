from app.db.db import init_db
from fastapi import FastAPI
from app.routers import file, user, folder, document, token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",  # Angular dev server
    "http://127.0.0.1:4200",  # In case you use 127.0.0.1 instead of localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE...
    allow_headers=["*"],  # Authorization, Content-Type...
)

app.include_router(user.router, tags=["Users"])
app.include_router(folder.router, tags=["Folders"])
app.include_router(document.router, tags=["Documents"])
app.include_router(file.router, prefix="/files", tags=["Files"])
app.include_router(token.router, tags=["Auth"]) 

init_db(app)

