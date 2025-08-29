from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure the VADER lexicon is available (done at build time, but safe here too)
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

app = FastAPI(title="VADER Sentiment API", version="1.0.0")
analyzer = SentimentIntensityAnalyzer()

class TextIn(BaseModel):
    sentence: str

class SentimentOut(BaseModel):
    sentence: str
    sentiment: str
    scores: dict

@app.get("/")
def root():
    return {"status": "ok", "message": "VADER Sentiment API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/analyze", response_model=SentimentOut)
def analyze_sentiment(data: TextIn):
    scores = analyzer.polarity_scores(data.sentence)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"sentence": data.sentence, "sentiment": sentiment, "scores": scores}
