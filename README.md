# Credit Card Fraud Detection

## Overview
This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The dataset used contains transactions labeled as fraudulent or legitimate, and the goal is to build a predictive model to classify transactions accurately.


## Goal : 1) Supervised(Classification) Machine Learning Task

## 2) We want to avoid false negatives as much as possible and will do that using the RECALL metric.

## Dataset Overview
The dataset contains 284,807 transactions.

It is highly imbalanced, meaning the number of fraudulent transactions (Class = 1) is significantly lower than the number of non-fraudulent ones (Class = 0).

The dataset is useful for fraud detection models that classify transactions as either fraudulent (1) or non-fraudulent (0).

## Columns Explanation

Time: The time elapsed (in seconds) since the first transaction in the dataset.

V1 to V28: These are anonymized features obtained via Principal Component Analysis (PCA) for privacy reasons. They contain numerical values that represent transformed transaction details.

Amount: The transaction amount in currency units.

Class: The target variable: 0 → Legitimate transaction 1 → Fraudulent transaction

## Key Points

The features V1 to V28 are not directly interpretable due to PCA transformation. The dataset is imbalanced, meaning special techniques like SMOTE (Synthetic Minority Over-sampling Technique), undersampling, or cost-sensitive learning may be required for model training.

## Project Structure
```
credit_card_fraud_detection/
|-- __pycache__/               # Compiled Python files
|-- artifacts/                 # Saved models and other artifacts
    -- random_forest_model.pkl    # Trained Random Forest model
    -- scaler.pkl                 # Saved scaler for feature normalization
|-- notebook/                  # Jupyter Notebooks for exploration analysis.
    -- creditcardfraud.ipynb      # Main notebook with data analysis, modeling, and evaluation.
|-- Dockerfile                 # Docker configuration for containerization
|-- README.md                  # Project documentation
|-- app.py                     # FastAPI for model inference 
|-- requirements.txt            # Python dependencies
```

## Installation
### Prerequisites
- Python 3.8+
- pip
- Virtual environment (optional but recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yugal18/Credit-Card-Fraud-Detection-Deployment.git
   cd credit_card_fraud_detection
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Model Training
Run the Jupyter Notebook to explore the dataset and train the model:
```sh
jupyter notebook creditcardfraud.ipynb
```

### Running the API
Start the FastAPI to serve the model:
```sh
python app.py or uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Using Docker
Build and run the containerized application:
```sh
docker build -t fraud-detection .
docker run -p 8000:8000 fraud-detection
```

## Dataset
The dataset used in this project is from Kaggle’s [Credit Card Fraud Detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud). It contains real transactions made by European cardholders in September 2013.

## Machine Learning Approach
- **Data Preprocessing**: feature scaling, and balancing classes.
- **Modeling**: Implementing Random Forest Classifier
- **Evaluation Metrics**: Recall(Important, our end goal is to detect fraudulant transaction) and AUC-ROC.

## API Endpoints
| Method | Endpoint   | Description |
|--------|-----------|-------------|
| POST   | /predict  | Predicts if a transaction is fraudulent |

Example request:


## License
This project is open-source and available under the MIT License.


