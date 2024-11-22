from fastapi import FastAPI, HTTPException

from backend.schemas.sentiment import SentimentRequest, SentimentResponse
from backend.services.sentiment_analysis import predict_sentiment


app = FastAPI()

@app.post("/predict_sentiment", response_model=SentimentResponse)
async def predict_sentiment_api(request: SentimentRequest):
    text = request.text
    try:
        sentiment = predict_sentiment(text)
        return SentimentResponse(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))