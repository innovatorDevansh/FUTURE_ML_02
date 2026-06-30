# ==========================================================
# Support Ticket Intelligence System
# helper.py
# ==========================================================

import os
import re
import string
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ==========================================================
# Download NLTK Resources (Only if Missing)
# ==========================================================

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

# ==========================================================
# Model Paths
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

TFIDF_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
TYPE_MODEL_PATH = os.path.join(MODEL_DIR, "ticket_type_model.pkl")
PRIORITY_MODEL_PATH = os.path.join(MODEL_DIR, "ticket_priority_model.pkl")

# ==========================================================
# Load Models
# ==========================================================

tfidf = joblib.load(TFIDF_PATH)

ticket_model = joblib.load(TYPE_MODEL_PATH)

priority_model = joblib.load(PRIORITY_MODEL_PATH)

# ==========================================================
# Text Cleaning Function
# ==========================================================

def clean_text(text):

    text = str(text)

    text = text.lower()

    # Remove placeholders
    text = re.sub(r"\{.*?\}", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove emails
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s\-]{8,}\d", " ", text)

    # Remove digits
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    cleaned_words = []

    for word in words:

        if word not in stop_words:

            cleaned_words.append(
                lemmatizer.lemmatize(word)
            )

    return " ".join(cleaned_words)

# ==========================================================
# Confidence Score
# ==========================================================

def get_confidence(model, vector):

    try:

        probabilities = model.predict_proba(vector)

        confidence = round(
            probabilities.max() * 100,
            2
        )

    except Exception:

        # LinearSVC does not support predict_proba
        confidence = "N/A"

    return confidence

# ==========================================================
# Team Assignment
# ==========================================================

def get_team(ticket_type):

    mapping = {

        "Technical issue": "Technical Support Team",

        "Billing inquiry": "Finance Team",

        "Refund request": "Customer Success Team",

        "Cancellation request": "Retention Team",

        "Product inquiry": "Sales Team"

    }

    return mapping.get(ticket_type, "General Support Team")

# ==========================================================
# SLA Recommendation
# ==========================================================

def get_sla(priority):

    mapping = {

        "Critical": "Respond within 15 Minutes",

        "High": "Respond within 1 Hour",

        "Medium": "Respond within 4 Hours",

        "Low": "Respond within 24 Hours"

    }

    return mapping.get(priority, "Standard SLA")

# ==========================================================
# Prediction Function
# ==========================================================

def predict_ticket(subject, product, description):

    # Same feature engineering used during training
    combined_text = f"{subject} {product} {description}"

    cleaned_text = clean_text(combined_text)

    vector = tfidf.transform([cleaned_text])

    ticket_type = ticket_model.predict(vector)[0]

    priority = priority_model.predict(vector)[0]

    confidence = get_confidence(ticket_model, vector)

    team = get_team(ticket_type)

    sla = get_sla(priority)

    return {

        "ticket_type": ticket_type,

        "priority": priority,

        "confidence": confidence,

        "team": team,

        "sla": sla

    }

# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    result = predict_ticket(

        subject="Payment Failed",

        product="Stripe Payment Gateway",

        description="Money has been deducted from my account but payment failed."

    )

    print(result)