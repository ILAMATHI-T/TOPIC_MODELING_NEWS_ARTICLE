import streamlit as st

# Page configuration
st.set_page_config(page_title="🔐 BBC News Classifier - Login", layout="centered")

# Background styling with newspaper image
st.markdown("""
    <style>
    .stApp {
        background: url("https://st.depositphotos.com/1032463/1373/i/450/depositphotos_13732950-stock-photo-background-of-old-vintage-newspapers.jpg") no-repeat center center fixed;
        background-size: cover;
        padding: 2rem;
    }
    .login-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 3rem 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        max-width: 500px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: #0B5FA5;
    }
    </style>
""", unsafe_allow_html=True)

# Login form container
with st.container():
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("## 🔐 BBC Topic Classifier - Login")

    # Input fields
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    # Login button
    if st.button("Login"):
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.switch_page("Predict")  # Switch to the Predict page (without the ".py" extension)
        else:
            st.error("❌ Invalid credentials. Try again.")

    st.markdown("</div>", unsafe_allow_html=True)
