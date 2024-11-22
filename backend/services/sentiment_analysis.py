from backend.services.model_operations import load_model, load_vectorizer

def predict_sentiment(text):
    model = load_model()
    vectorizer = load_vectorizer()
    
    processed_text = [text]
    text_tfidf = vectorizer.transform(processed_text)
    
    prediction = model.predict(text_tfidf)
    return prediction[0]