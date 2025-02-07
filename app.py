import pickle
import pandas as pd
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define paths for model and scaler
BASE_DIR = os.path.join(os.getcwd(), "artifacts")
MODEL_PATH = os.path.join(BASE_DIR, "random_forest_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")  

# Load the model and scaler
try:
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
    logger.info("Model pkl loaded successfully.")
    
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

try:
    with open(SCALER_PATH, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    logger.info("Scaler pkl loaded successfully.")
    
except Exception as e:
    logger.error(f"Error loading scaler: {e}")
    raise

# FastAPI application setup
app = FastAPI()

class TransactionData(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

@app.post("/predict/")  
def predict_transaction(transaction: TransactionData):
    try:
        # Convert input data into a DataFrame
        transaction_dict = transaction.dict()
        transaction_df = pd.DataFrame([transaction_dict])

        # Validate input
        if transaction_df["Amount"].iloc[0] < 0:
            raise HTTPException(status_code=400, detail="Amount cannot be negative.")

        # Scale the 'Amount' feature only
        #transaction_df["Amount"] = scaler.transform(transaction_df[["Amount"]])
        amount_values = transaction_df[["Amount"]].values  # Get the raw values without column names
        transaction_df["Amount"] = scaler.transform(amount_values)
        # Make the prediction
        prediction = model.predict(transaction_df)

        return {"Prediction": int(prediction[0])}

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction error.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


