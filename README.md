# Parkinson's Disease Predictor

This is a machine learning-based web application built with Streamlit that predicts whether a person has Parkinson's Disease based on biomedical voice measurements.

## Project Structure

Parkinson Predictor/

├── app.py # Streamlit app for prediction

├── Parkinson's_Disease_Prediction.ipynb # Jupyter Notebook for model training

├── parkinsons.data # Dataset file

├── requirements.txt # Python dependencies

└── .gitignore # Git ignored files


## Dataset

- Source: UCI Machine Learning Repository
- File: `parkinsons.data`
- Features: 22 biomedical voice measures
- Target: `status` (1 = Parkinson’s, 0 = healthy)

**How to Run**

**Clone the repository**

Open a terminal and run:
git clone https://github.com/AkashG-03/Parkinson-s-Disease-Predictor.git
cd Parkinson-s-Disease-Predictor

**Create a virtual environment**

Run the following commands:
python -m venv .venv
.\.venv\Scripts\activate (on Windows)

**Install dependencies**

Run:
pip install -r requirements.txt

Run the Streamlit app
Run:
streamlit run app.py
Then open your browser and go to:
http://localhost:8501



**Tech Stack**

->Python 

->Streamlit 

->scikit-learn 

->pandas, numpy

**Model**

StandardScaler for feature normalization

SVM classifier for prediction
