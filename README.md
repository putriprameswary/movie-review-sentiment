# 🎬 Movie Mood Meter
> *Let AI read between the lines of your movie review 😉*

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-34C759?style=for-the-badge)

**An NLP-powered web app that detects whether your movie review is positive or negative — instantly.**

[🚀 Try Live Demo](https://movie-mood-meter.streamlit.app) · [📓 View Notebook](https://colab.research.google.com/drive/1vg7bfwsYSn3cBH_LaX4CIXJSgr4KugJ3?usp=sharing) · [📦 Dataset on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/data)

</div>

---

## ✨ What Is This?

**Movie Mood Meter** is a end-to-end sentiment analysis app — from model training to a live web interface. Paste any movie review, and the AI will tell you whether the vibe is 😊 **Positive** or 😠 **Negative**, along with a confidence score.

Built with real NLP, not vibes. Trained on **10,000 real IMDB reviews** (sampled from 50K) using TF-IDF + Logistic Regression.

---

## 🧠 How It Works

```
User Input → Text Cleaning → TF-IDF Vectorization → Logistic Regression → Sentiment + Confidence Score
```

1. **Preprocessing** — lowercasing, HTML tag removal, punctuation stripping
2. **Feature Extraction** — TF-IDF Vectorizer (top 5,000 features)
3. **Classification** — Logistic Regression model
4. **Output** — Positive / Negative label + confidence percentage

---

## ⚙️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| ML | Scikit-learn |
| NLP | TF-IDF Vectorizer |
| Classifier | Logistic Regression |
| Frontend | Streamlit |
| Training Env | Google Colab |
| Dataset | IMDB 50K Movie Reviews |

---

## ✅ Features

- 🔍 Real-time sentiment prediction
- 📊 Confidence score with visual progress bar
- 🧹 Auto text preprocessing pipeline
- 💡 Example reviews to try instantly
- 🎨 Clean, minimal Apple-inspired UI

---

## 🔬 Model Training

The model was trained in Google Colab. The pipeline covers:

- Sampling 10,000 reviews from the 50K IMDB dataset
- Cleaning text (lowercase, remove HTML, punctuation, whitespace)
- Label encoding (`positive=1`, `negative=0`)
- 80/20 train-test split
- TF-IDF vectorization (max 5,000 features)
- Logistic Regression training (`max_iter=1000`)

📓 **[Open Training Notebook →](https://colab.research.google.com/drive/1vg7bfwsYSn3cBH_LaX4CIXJSgr4KugJ3?usp=sharing)**

---

## ▶️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/movie-mood-meter.git
cd movie-mood-meter

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

> ⚠️ Make sure `model.pkl` and `vectorizer.pkl` are in the root directory. Download them from the Colab notebook above.

---

## 📂 Project Structure

```
movie-mood-meter/
├── app.py                 # Streamlit web app
├── model.pkl              # Trained Logistic Regression model
├── vectorizer.pkl         # Fitted TF-IDF vectorizer
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 📸 Preview

> *(Screenshot coming soon - or try it live!)*

---

## 📌 Notes

This project is intentionally simple — the focus is on building a clean, working end-to-end NLP pipeline and making it accessible through a friendly UI. Great starting point for learning applied NLP!

---

## 👤 Author

Made with ❤️ by **Riri**

---

<div align="center">
<sub>Built with Streamlit. Riri's NLP Project</sub>
</div>
