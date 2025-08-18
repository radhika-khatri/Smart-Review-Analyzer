# backend.py - FastAPI example
from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Load your original models (same as Streamlit)
@app.on_event("startup")
async def load_models():
    global sentiment_pipeline, zero_shot_pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    zero_shot_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class TextInput(BaseModel):
    text: str

class ClassifyInput(BaseModel):
    text: str
    labels: list[str]

@app.post("/api/sentiment")
async def analyze_sentiment(input_data: TextInput):
    try:
        result = sentiment_pipeline(input_data.text, truncation=True)[0]
        return {"label": result["label"], "score": result["score"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

LABELS = ["battery", "camera", "performance", "price", "build quality"]

@app.post("/api/classify")
async def classify_features(input_data: ClassifyInput):
    try:
        result = zero_shot_pipeline(input_data.text, input_data.labels, multi_label=False)
        return {"labels": result["labels"], "scores": result["scores"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)