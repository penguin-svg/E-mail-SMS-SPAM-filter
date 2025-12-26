# E-mail-SMS-SPAM-filter
# Email/SMS Spam Classifier

A machine learning-powered web application that classifies messages as spam or not spam using Natural Language Processing (NLP) techniques.

## Overview

This project uses a trained machine learning model to detect spam in SMS and email messages. The application is built with Streamlit, providing an intuitive web interface for real-time spam detection.

## Features

- **Real-time Classification**: Instantly classify messages as spam or not spam
- **NLP Processing**: Uses advanced text preprocessing including tokenization, stemming, and stop word removal
- **User-Friendly Interface**: Simple and clean Streamlit-based UI
- **Pre-trained Model**: Comes with a ready-to-use trained model and vectorizer

## Technology Stack

- **Python 3.x**
- **Streamlit**: Web application framework
- **NLTK**: Natural Language Toolkit for text processing
- **scikit-learn**: Machine learning library
- **Pickle**: Model serialization

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spam-classifier.git
cd spam-classifier
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Launch the application using the command above
2. Enter your message in the text area
3. Click the "Predict" button
4. View the classification result (Spam or Not Spam)

## Project Structure

```
spam-classifier/
│
├── app.py                    # Main Streamlit application
├── model (1).pkl            # Trained machine learning model
├── vectorizer (1).pkl       # TF-IDF vectorizer
├── requirements.txt         # Python dependencies
├── DEPLOYMENT.md           # Deployment guide
└── README.md               # Project documentation
```

## How It Works

1. **Text Preprocessing**: The input message goes through several preprocessing steps:
   - Conversion to lowercase
   - Tokenization
   - Removal of non-alphanumeric characters
   - Stop word removal
   - Stemming using Porter Stemmer

2. **Vectorization**: The processed text is transformed using TF-IDF vectorization

3. **Classification**: The trained model predicts whether the message is spam or not

## Deployment

This application can be easily deployed to Streamlit Cloud. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Quick Deploy to Streamlit Cloud

1. Push this repository to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Deploy with one click!

## Model Information

The classifier uses:
- **TF-IDF Vectorization** for feature extraction
- **Pre-trained ML Model** (stored in `model (1).pkl`)
- **NLTK** for text preprocessing

## Requirements

- Python 3.7+
- streamlit
- nltk
- scikit-learn

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with Streamlit
- NLP powered by NLTK
- Machine learning with scikit-learn

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Make sure the model files (`model (1).pkl` and `vectorizer (1).pkl`) are present in the project directory before running the application.
