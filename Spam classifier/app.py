import streamlit as st
import pickle 
model = pickle.load(open("spam_predition.pkl.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
st.header("Applications of Naive Bayes ")
st.title("Spam Classifier")
text = st.text_input("Enter text: ")
if text:
    text = vectorizer.transform([text])
    prediction = model.predict(text)
    if prediction == 1:
        st.write("Spam")
    else:
        st.write("Ham")
        
        
st.title("Movie Sentiment Analysis")
sentiment =    st.text_input("Enter movie review : ")
m = pickle.load(open("model.pkl", "rb"))
vc = pickle.load(open("vectoriz.pkl", "rb"))
if sentiment:
    sentiment = vc.transform([sentiment])
    pred = m.predict(sentiment)
    if pred == 1:
         st.write("Positive")
    else:

        st.write("Negative")




