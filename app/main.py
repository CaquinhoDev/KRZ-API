__version__ = "0.0.1"
__author__ = "Júnior Krz"


import os
from fastapi import FastAPI, HTTPException, Depends, Header

from app.bot import chatbot


# Allowed access token
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN') or 'MyS3cur3T0k3n'


app = FastAPI()


def verify_token(authorization: str = Header(...)):
    if authorization != f"Bearer {ACCESS_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid token")
    return authorization


@app.get("/")
async def root():
    return {
                "message": "KrzBot API Online!",
                "author": __author__,
                "version": __version__
            }


@app.get("/get_response/{question}")
async def get_response(question: str, authorization: str = Depends(verify_token)):
    response = chatbot.get_response(question)
    return {"response": str(response)}