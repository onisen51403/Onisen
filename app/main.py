from fastapi import FastAPI
from .confg import settings
from . import models
from .database import engine
from .routers import post, user, auth, vote
from typing import Union
from fastapi.middleware.cors import CORSMiddleware


print(settings.database_username)

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"message": "Hello Onisen Chikwanda!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#fetch('http://localhost:8000/').then(res => res.json()).then(console.log)