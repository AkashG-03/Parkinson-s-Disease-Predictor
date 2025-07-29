import streamlit as st
import numpy as np
import pickle


model = pickle.load(open("parkinsons_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Parkinson's Disease Predictor", layout="centered")
st.title("Parkinson's Disease Prediction App")

st.markdown("Enter the voice measurements below to predict the presence of Parkinson's disease.")


feature_names = [
    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
    'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
    'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
    'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
]

user_input = []
for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0)
    user_input.append(value)


if st.button("Predict"):
    input_array = np.array([user_input])
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("The model predicts that the person may have Parkinson's Disease.")
    else:
        st.success("The model predicts that the person does not have Parkinson's Disease.")
