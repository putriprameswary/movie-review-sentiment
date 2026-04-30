import streamlit as st
import pickle
import re
import string

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🎬",
    layout="centered"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* ===== GLOBAL ===== */
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #fafafa;
}

/* ===== CONTAINER ===== */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 700px;
}

/* ===== HEADER ===== */
h1 {
    text-align: center;
    font-weight: 600;
    letter-spacing: -0.5px;
    margin-bottom: 0.3em;
}

.subtitle {
    text-align: center;
    color: #6e6e73;
    font-size: 15px;
    margin-bottom: 2.5rem;
}

/* ===== TEXT AREA ===== */
textarea {
    border-radius: 12px !important;
    border: 1px solid #d2d2d7 !important;
    padding: 12px !important;
    font-size: 15px !important;
}

/* ===== BUTTON ===== */
.stButton > button {
    border-radius: 10px;
    padding: 10px 18px;
    background-color: #0071e3;
    color: white;
    border: none;
    font-weight: 500;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #005bb5;
}

.stButton > button:active {
    transform: scale(0.97);
}

/* ===== RESULT CARD ===== */
.result-box {
    padding: 24px;
    border-radius: 16px;
    background: #ffffff;
    border: 1px solid #e5e5ea;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    text-align: center;
    margin-top: 30px;
}

/* ===== TEXT COLOR ===== */
.success-text {
    color: #34c759;
    font-weight: 500;
    font-size: 18px;
}

.error-text {
    color: #ff3b30;
    font-weight: 500;
    font-size: 18px;
}

/* ===== PROGRESS ===== */
.stProgress > div > div {
    background-color: #0071e3;
}

/* ===== EXAMPLE BOX ===== */
.stAlert {
    border-radius: 12px !important;
    border: 1px solid #e5e5ea !important;
    background-color: #f5f5f7 !important;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    color: #8e8e93;
    font-size: 12px;
    margin-top: 50px;
}
/* CARD WRAPPER */
.card {
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #e5e5ea;
    background: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    margin-top: 25px;
}

/* RESULT TEXT */
.result-positive {
    color: #34c759;
    font-weight: 600;
    font-size: 18px;
    text-align: center;
}

.result-negative {
    color: #ff3b30;
    font-weight: 600;
    font-size: 18px;
    text-align: center;
}

/* CENTER ELEMENTS */
.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown("<h1>🎬 Movie Mood Meter</h1>", unsafe_allow_html=True)
st.markdown("<h3>Let AI read between the lines of your movie review 😉</h3>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>NLP-powered movie review analyzer (trained on 10,000 real opinions)</div>", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# ---------------- PREPROCESS ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    return text

# ---------------- INPUT ----------------
user_input = st.text_area(
    "✍️ Drop your honest review here",
    placeholder="e.g. This movie was absolutely fantastic...",
    height=150
)

st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
analyze = st.button("Analyze")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESULT ----------------
if analyze:
    if user_input.strip() == "":
        st.warning("Please enter a review first.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        prob = model.predict_proba(vectorized)[0]

        confidence = max(prob) * 100

        st.markdown("<div class='result-wrapper'>", unsafe_allow_html=True)

        if prediction == 1:
            st.success("Positive 😊")
        else:
            st.error("Negative 😠")

        st.progress(int(confidence))
        st.caption(f"{confidence:.2f}% confidence")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EXAMPLES ----------------
st.markdown("### Try example inputs")

col1, col2 = st.columns(2)

with col1:
    st.info("This movie was amazing and full of emotion.")

with col2:
    st.info("The movie was boring and a waste of time.")

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>Built with ❤️ using Streamlit · Riri's NLP Project</div>",
    unsafe_allow_html=True
)