import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Dummy prediction logic with topic probabilities
def predict_topic(texts):
    # For simplicity, this returns a random distribution of probabilities for topics
    topics = ['Business', 'Politics', 'Tech', 'Entertainment']
    if isinstance(texts, pd.Series):
        return [dict(zip(topics, [random.random() for _ in topics])) for _ in texts]
    elif isinstance(texts, str):
        return dict(zip(topics, [random.random() for _ in topics]))

# Config
st.set_page_config(page_title="📄 Predict BBC Topic", layout="wide")

# Authentication check
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("🔐 Please log in to access this page.")
    st.stop()

# Layout
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/BBC_logo_2023.svg/1200px-BBC_logo_2023.svg.png", width=90)
with col2:
    st.title("📄 Upload News Article for Topic Prediction")
    st.markdown("""
    Upload a `.txt` or `.csv` file containing **BBC news articles** to classify them into categories like *Politics*, *Tech*, *Business*, etc.
    """)

# Upload file
uploaded_file = st.file_uploader("📂 Choose a `.txt` or `.csv` file", type=["txt", "csv"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "txt":
        text = uploaded_file.read().decode("utf-8")
        st.subheader("📰 Article Content:")
        # Display the content in a text area for viewing
        st.text_area("Article Content", text, height=300)

        # Get prediction for topics in text
        predicted_topic = predict_topic(text)
        st.success(f"✅ **Predicted Topics:** {predicted_topic}")

        # Create a bar chart with topic probabilities
        st.subheader("📊 Category Visualization")
        fig, ax = plt.subplots()
        topics = list(predicted_topic.keys())
        probabilities = list(predicted_topic.values())

        ax.bar(topics, probabilities, color='royalblue')
        ax.set_ylabel("Probability")
        ax.set_title("Topic Distribution")
        st.pyplot(fig)

    elif file_type == "csv":
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("📊 Uploaded CSV Preview:")
            st.dataframe(df.head())

            # Identify a column with article content if no specific column is named 'text', 'content', or 'article'
            text_col = None
            for col in df.columns:
                if col.lower() in ['text', 'content', 'article']:
                    text_col = col
                    break
            
            # If no specific text column found, just use the first column as the fallback
            if not text_col:
                text_col = df.columns[0]

            # Get prediction for each article in the dataframe
            predicted_topics = predict_topic(df[text_col])
            topic_data = pd.DataFrame(predicted_topics)

            # Combine prediction data with the original dataframe
            df = pd.concat([df, topic_data], axis=1)
            st.subheader("📑 Predictions")
            st.dataframe(df[[text_col] + list(topic_data.columns)])

            st.subheader("📊 Category Distribution")
            topic_counts = topic_data.apply(lambda x: x.idxmax(), axis=1).value_counts()

            fig, ax = plt.subplots()
            topic_counts.plot(kind='bar', color='mediumseagreen', ax=ax)
            ax.set_ylabel("Number of Articles")
            ax.set_title("Predicted Categories")
            st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error processing CSV file: {e}")
