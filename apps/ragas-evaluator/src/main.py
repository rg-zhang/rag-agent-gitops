import sys
mock_mod = type("mock_mod", (), {"ChatVertexAI": None})
sys.modules["langchain_community.chat_models.vertexai"] = mock_mod

from fastapi import FastAPI
from ragas import evaluate

app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}
