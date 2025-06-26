from fastapi import FastAPI
from app.auth import router as auth_router
from app.database import engine
from app.models import Base
from app.routes import questions, answers, vote
from app.routes import me


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)
app.include_router(questions.router)
app.include_router(answers.router)
app.include_router(vote.router)
app.include_router(me.router)