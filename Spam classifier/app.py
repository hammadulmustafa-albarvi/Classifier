import streamlit as st
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

model = pickle.load(open(BASE_DIR / "spam_predition.pkl", "rb"))
vectorizer = pickle.load(open(BASE_DIR / "vectorizer.pkl", "rb"))

st.header("Applications of Naive Bayes ")
st.title("Spam Classifier")

text = st.text_input("Enter text: ")

if text:
    text = vectorizer.transform([text])
    prediction = model.predict(text)

    if prediction[0] == 1:
        st.write("Spam")
    else:
        st.write("Ham")


st.title("Movie Sentiment Analysis")

sentiment = st.text_input("Enter movie review : ")

m = pickle.load(open(BASE_DIR / "model.pkl", "rb"))
vc = pickle.load(open(BASE_DIR / "vectoriz.pkl", "rb"))

if sentiment:
    sentiment = vc.transform([sentiment])
    pred = m.predict(sentiment)

    if pred[0] == 1:
        st.write("Positive")
    else:
        st.write("Negative")
