# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    text: str

@app.post("/predict")
async def predict(data: InputData):
    # 模拟推理
    result = {"length": len(data.text), "input": data.text}
    return result
