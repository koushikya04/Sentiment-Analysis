import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Sentiment Analysis App", layout="wide")
st.title("🧠 Sentiment Analysis of Reviews")

st.sidebar.header("Upload & Options")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # Select column with text
    text_col = st.sidebar.selectbox("Select column containing text", df.columns)
    df = df.dropna(subset=[text_col])

    # Analyze with TextBlob
    def get_textblob_sentiment(text):
        polarity = TextBlob(str(text)).sentiment.polarity
        return 'positive' if polarity > 0.1 else 'negative' if polarity < -0.1 else 'neutral'

    df['Sentiment'] = df[text_col].apply(get_textblob_sentiment)

    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = df['Sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

    st.subheader("☁️ WordClouds")
    for sentiment in ['positive', 'negative']:
        texts = " ".join(df[df['Sentiment'] == sentiment][text_col].astype(str))
        if texts.strip():
            wordcloud = WordCloud(width=800, height=300, background_color='white').generate(texts)
            st.markdown(f"#### {sentiment.capitalize()} Reviews")
            st.image(wordcloud.to_array())
        else:
            st.warning(f"No {sentiment} reviews found to generate a WordCloud.")

    if st.checkbox("Show processed data"):
        st.dataframe(df)

# Analyze single input
st.subheader("💬 Analyze Single Review")
user_input = st.text_area("Enter your review text below:")

if st.button("Analyze Sentiment"):
    if user_input:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        final = 'positive' if polarity > 0.1 else 'negative' if polarity < -0.1 else 'neutral'
        st.write("### TextBlob Polarity:", polarity)
        st.success(f"Overall Sentiment: {final.upper()}")
    else:
        st.warning("Please enter some text to analyze.")