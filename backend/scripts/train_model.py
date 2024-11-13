import pandas as pd
from backend.services.data_preprocessing import preprocess_text
from backend.services.model_operations import train_and_save_model
from backend.config import DATASET_PATH

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    
    if 'text' not in data.columns or 'label' not in data.columns:
        raise ValueError("CSV must contain 'text' and 'label' columns")
    
    data['processed_text'] = data['text'].apply(preprocess_text)
    
    X = data['processed_text']
    y = data['label']
    return X, y

def main():
    X, y = load_and_preprocess_data(DATASET_PATH)
    
    train_and_save_model(X, y)

if __name__ == "__main__":
    main()
