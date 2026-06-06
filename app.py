
import streamlit as st
import joblib
import os
import google.generativeai as genai

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("model.pkl")

st.title("Fake News Detector + AI Summary")

st.write("Enter a news article to check whether it is Fake or Real and get AI summary.")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
else:
    gemini_model = None

news_input = st.text_area("News Article:")

# --------------------------
# Prediction
# --------------------------
if st.button("Check News"):

    if news_input.strip():

        # ML Prediction
        transformed_input = vectorizer.transform([news_input])
        prediction = model.predict(transformed_input)

        if prediction[0] == 1:
            st.success("The News is Real!")
        else:
            st.error("The News is Fake!")

        if gemini_model:
            with st.spinner("Generating AI summary..."):
                response = gemini_model.generate_content(
                    "Summarize the following news article in 4-5 bullet points:\n\n"
                    + news_input
                )

            st.subheader("News Summary")
            st.write(response.text)

        else:
            st.warning("Gemini API key not configured.")

    else:
        st.warning("Please enter a news article.")
