# Fake News Detection with AI-Powered News Summarization

## Project Overview

This project is a Machine Learning and Generative AI based web application that detects whether a news article is **Fake** or **Real** and generates an AI-powered summary of the news article.

The application uses a trained Machine Learning model for classification and Google's Gemini API for generating concise summaries.

---

## Dataset

This project was trained using a publicly available Fake and Real News Dataset from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

The dataset contains labeled news articles categorized as Fake and Real, which were used for training and evaluating the machine learning model.

---

## Features

* Fake News Detection using Machine Learning
* Real News Detection
* AI-generated News Summaries using Gemini API
* User-friendly Streamlit Web Interface
* Cloud Deployment using Streamlit Community Cloud

---

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* Joblib
* Google Gemini API
* GitHub

---

## Project Workflow

1. User enters a news article.
2. Text is transformed using a TF-IDF Vectorizer.
3. Trained Machine Learning model predicts whether the news is Fake or Real.
4. Gemini AI generates a concise summary of the news article.
5. Results are displayed on the Streamlit web application.

---

## Files Included

* `Fake_News_Detection.ipynb` – Model training notebook
* `app.py` – Streamlit application
* `model.pkl` – Trained Machine Learning model
* `vectorizer.pkl` – TF-IDF Vectorizer
* `requirements.txt` – Required Python packages

---

## Deployment

### Streamlit App

https://fake-news-detection-using-ai.streamlit.app/

### GitHub Repository

https://github.com/Sau-ai28706/Fake_News_Detection

---

## Future Enhancements

* Multi-language support
* Confidence score visualization
* Fact-checking using trusted news sources
* URL-based news verification
* Mobile application deployment

---

## References

https://docs.streamlit.io/

https://scikit-learn.org/stable/

https://ai.google.dev/gemini-api/docs

https://docs.python.org/3/

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset


---

## Author

Developed as a Capstone Project for internship/project submission.
