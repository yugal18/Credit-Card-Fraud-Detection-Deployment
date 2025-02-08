# Credit Card Fraud Detection

## Overview
This project focuses on detecting fraudulent credit card transactions using machine learning techniques. The dataset used contains transactions labeled as fraudulent or legitimate, and the goal is to build a predictive model to classify transactions accurately.

## Project Structure
```
credit_card_fraud_detection/
|-- __pycache__/               # Compiled Python files
|-- artifacts/                 # Saved models and other artifacts
|-- random_forest_model.pkl    # Trained Random Forest model
|-- scaler.pkl                 # Saved scaler for feature normalization
|-- notebook/                  # Jupyter Notebooks for exploration and analysis
|-- creditcardfraud.ipynb      # Main notebook with data analysis and modeling
|-- Dockerfile                 # Docker configuration for containerization
|-- README.md                  # Project documentation
|-- app.py                     # Flask API for model inference
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
python app.py
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


