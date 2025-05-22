from fastapi import FastAPI
from app.auth import router as auth_router
from app.database import engine
from app.models import Base
from app.routes import questions, answers


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)
app.include_router(questions.router)
app.include_router(answers.router)