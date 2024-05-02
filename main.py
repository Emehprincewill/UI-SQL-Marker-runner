# from flask import Flask, redirect

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Redirect to the desired web page
#     return redirect("https://61eb-197-210-84-202.ngrok-free.app")

# # if __name__ == '__main__':
# #     app.run(debug=True)


# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.llms import Ollama

# Define FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Initialize Ollama
llm = Ollama(model="llama3")

# Define request body model
class TextRequest(BaseModel):
    text: str

# Prediction endpoint
@app.post("/predict")
async def predict(text_request: TextRequest):
    response_text = llm.invoke(text_request.text)
    return {"prediction": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

