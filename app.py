import streamlit as st
import pandas as pd
import string
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Title
st.title("Customer Support Ticket Classifier")

# Load dataset
df = pd.read_csv("customer_support_tickets.csv")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["clean_text"] = df["Ticket Description"].astype(str).apply(clean_text)

# Feature extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_text"])

y = df["Ticket Type"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# User input
ticket = st.text_area("Enter Customer Support Ticket")

if st.button("Predict Category"):
    
    cleaned = clean_text(ticket)
    
    vector = vectorizer.transform([cleaned])
    
    prediction = model.predict(vector)
    
    st.success(f"Predicted Ticket Category: {prediction[0]}")                   