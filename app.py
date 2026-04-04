import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# ===== CSS Styling =====
st.markdown("""
<style>

/* Background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1548092372-0d1bd40894a3?q=80&w=1170&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Dark overlay */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    z-index: 0;
}

/* Bring content above overlay */
.block-container {
    position: relative;
    z-index: 1;
}

/* Title */
h1 {
    color: 9E4770;
    text-align: center;
    font-size: 42px;
}

/* Labels */
label, p {
    color: white !important;
    font-weight: 500;
}

/* Input */
.stNumberInput input {
    background-color: rgba(255,255,255,0.2);
    color: white;
    border-radius: 10px;
}

/* Checkbox */
.stCheckbox label {
    color: white !important;
}

/* Button */
.stButton button {
    background-color: #2E2532;
    color: white;
    border-radius: 12px;
    padding: 10px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover {
    background-color: #44334a;
}

/* Code output */
code {
    color: #00ffcc;
    font-size: 18px;
}

/* Glass effect container */
div[data-testid="stVerticalBlock"] {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.title("🔐 Password Generator")

# ===== INPUT =====
length = st.number_input("Enter password length", min_value=4, max_value=50, value=12)

upper = st.checkbox("Include Uppercase", value=True)
digits = st.checkbox("Include Numbers", value=True)
symbols = st.checkbox("Include Symbols", value=True)

# ===== INFO =====
st.info("💡 Tip: Use at least 12 characters with uppercase, numbers & symbols for strong passwords.")

# ===== FUNCTION =====
def generate_password(length, upper, digits, symbols):
    characters = string.ascii_lowercase
    
    if upper:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if characters == "":
        return None
    
    return ''.join(random.choice(characters) for _ in range(length))

# ===== BUTTON =====
if st.button("Generate Password 🚀"):
    password = generate_password(length, upper, digits, symbols)

    if password:
        st.code(password, language=None)

        # Strength checker
        if len(password) >= 12 and symbols and upper and digits:
            st.success("Strong Password 💪")
        elif len(password) >= 8:
            st.warning("Medium Password ⚠️")
        else:
            st.error("Weak Password ❌")
    else:
        st.error("Please select at least one option!")
