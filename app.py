import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()




import nltk
nltk.download('punkt')
nltk.download('stopwords')






def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf=pickle.load(open('vectorizer (1).pkl','rb'))
model=pickle.load(open('model (1).pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms=st.text_area("Enter the message")

if st.button('Predict'):


    transformed_sms= transform_text(input_sms)

    vector =tfidf.transform([transformed_sms])

    result=model.predict(vector)[0]

    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")



