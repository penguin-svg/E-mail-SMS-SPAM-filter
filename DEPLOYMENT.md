# Deployment Guide

This project is a Streamlit app that can be easily deployed to **Streamlit Cloud**.

## Prerequisites

1.  **GitHub Account**: You need a GitHub account.
2.  **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io/).

## Steps to Deploy

1.  **Push to GitHub**:
    *   Create a new repository on GitHub.
    *   Push all the files in this project to that repository.
    *   Ensure `requirements.txt`, `app.py`, `model (1).pkl`, and `vectorizer (1).pkl` are included.

2.  **Deploy on Streamlit Cloud**:
    *   Go to [share.streamlit.io](https://share.streamlit.io/).
    *   Click "New app".
    *   Select your GitHub repository, branch (usually `main` or `master`), and the main file path (`app.py`).
    *   Click "Deploy".

## Notes

*   **Dependencies**: The `requirements.txt` file lists the necessary Python libraries (`streamlit`, `nltk`, `scikit-learn`). Streamlit Cloud will automatically install them.
*   **NLTK Data**: The `app.py` file already includes `nltk.download('punkt')` and `nltk.download('stopwords')`, which ensures the necessary NLTK data is downloaded during the app startup.
