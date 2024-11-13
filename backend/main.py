from fastapi import FastAPI, HTTPException

from schemas.sentiment import SentimentRequest, SentimentResponse
from services.sentiment_analysis import predict_sentiment

app = FastAPI()

@app.post("/predict_sentiment", response_model=SentimentResponse)
async def predict_sentiment_api(request: SentimentRequest):
    text = request.text
    print("text===", text)
    try:
        sentiment = predict_sentiment(text)
        print("sentiment===", sentiment)
        return SentimentResponse(sentiment=sentiment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))