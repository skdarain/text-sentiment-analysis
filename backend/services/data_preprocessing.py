import re

def preprocess_text(text):
    print("text===", text)
    if type(text) is not str:
        print("type(text)==", type(text))
        return " "
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower().strip()
    return text
