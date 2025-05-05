import streamlit as st

# Page configuration
st.set_page_config(page_title="📖 About Us", layout="wide")

# Two-column layout with logo
col1, col2 = st.columns([1, 3])

with col1:
    st.image(
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/BBC_logo_2023.svg/1200px-BBC_logo_2023.svg.png',
        width=100
    )

with col2:
    st.title("📖 About BBC Topic Classifier")
    st.markdown("""
    The **BBC Topic Classifier** is an intelligent web application that leverages **Natural Language Processing (NLP)** to automatically categorize BBC news articles into topics such as:

    - 🏛️ **Politics**
    - 💼 **Business**
    - 🎭 **Entertainment**
    - ⚽ **Sport**
    - 🔬 **Tech**

    ### 💡 Key Features:
    - 🔐 Login with demo credentials
    - 📂 Upload `.txt` or `.csv` files with article text
    - 🤖 Get real-time predictions with a pre-trained ML model
    - 📊 Visualize topic distribution via bar charts

    ### 🧠 Behind the Scenes:
    - **Text preprocessing** (cleaning, tokenization)
    - **Vectorization** using **TF-IDF**
    - Classification using **XGBoost** or **Random Forest**

    ### 🔒 Security Note:
    This is a **demo version** with mock login. For production, replace with secure backend authentication.

    ### 👨‍💻 Developed by:
    - **Your Name**
    - 📧 your.email@example.com

    ---
    """)
