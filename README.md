# 🎫 AI-Powered Support Ticket Classification & Prioritization System

An end-to-end Machine Learning and NLP solution that automatically classifies customer support tickets into categories and predicts their priority level. The system helps organizations streamline support operations, reduce manual effort, and improve response times through intelligent ticket routing.

---

## 📌 Project Overview

Customer support teams receive hundreds of tickets every day from multiple channels such as email, chat, and web forms. Manually categorizing and prioritizing these tickets is time-consuming and often delays responses to critical issues.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to automatically:

- Classify support tickets into predefined categories.
- Predict ticket priority levels.
- Assign the appropriate support team.
- Recommend a Service Level Agreement (SLA).
- Provide an interactive Streamlit-based web application for real-time predictions.

---

## 🚀 Features

- 📝 Automatic Support Ticket Classification
- ⚡ Ticket Priority Prediction
- 🧹 Text Cleaning & NLP Preprocessing
- 📊 TF-IDF Feature Engineering
- 🤖 Multiple Machine Learning Models Comparison
- 📈 Model Performance Evaluation
- 👨‍💻 Automatic Team Assignment
- ⏱ SLA Recommendation
- 🎨 Interactive Streamlit Dashboard
- 📄 Download Prediction Summary

---

## 🧠 Machine Learning Workflow

```
Raw Ticket Data
        │
        ▼
Data Cleaning
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Model Training
        │
        ▼
Prediction
        │
        ▼
Support Team Assignment
        │
        ▼
SLA Recommendation
```

---

# 📂 Project Structure

```
FUTURE_ML_02/
│
├── App/
│   ├── app.py
│   ├── helper.py
│   ├── config.py
│   └── style.css
│
├── Data/
│   └── customer_support_tickets.csv
│
├── Images/
│   ├── dashboard.png
│   ├── prediction.png
│   ├── eda1.png
│   ├── eda2.png
│   ├── confusion_matrix_type.png
│   └── confusion_matrix_priority.png
│
├── Models/
│   ├── tfidf_vectorizer.pkl
│   ├── ticket_type_model.pkl
│   └── ticket_priority_model.pkl
│
├── Notebook/
│   └── Support_Ticket_Classification.ipynb
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 📊 Dataset

**Dataset Used**

Customer Support Ticket Dataset

- Contains customer support tickets
- Ticket descriptions
- Ticket categories
- Ticket priorities
- Customer details

Dataset Size

- **Total Records:** 8,469
- **Ticket Categories:** 5
- **Priority Levels:** 4

---

# 🎯 Ticket Categories

- Technical Issue
- Billing Inquiry
- Refund Request
- Cancellation Request
- Product Inquiry

---

# 🚨 Priority Levels

- Critical
- High
- Medium
- Low

---

# 🛠 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Matplotlib
- Seaborn
- WordCloud

### Web Framework

- Streamlit

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# 🔍 NLP Pipeline

The ticket descriptions go through several preprocessing steps before training the machine learning models.

- Lowercase Conversion
- Remove Punctuation
- Remove Numbers
- Remove URLs
- Remove Stopwords
- Lemmatization
- TF-IDF Vectorization

---

# 🤖 Machine Learning Models Evaluated

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest Classifier
- Linear Support Vector Machine (SVM)

The best-performing models were selected based on evaluation metrics.

---

# 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

# 📷 Application Screenshots

## Streamlit Dashboard

> Add image here

```
Images/dashboard.png
```

---

## Prediction Result

> Add image here

```
Images/prediction.png
```

---

## Exploratory Data Analysis

> Add EDA screenshots here

```
Images/eda1.png
Images/eda2.png
```

---

## Model Evaluation

> Add confusion matrix screenshots here

```
Images/confusion_matrix_type.png
Images/confusion_matrix_priority.png
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/innovatorDevansh/FUTURE_ML_02.git
```

Move into the project directory

```bash
cd FUTURE_ML_02
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run App/app.py
```

---

# 💻 How It Works

1. Enter the ticket subject.
2. Enter the product name.
3. Enter the ticket description.
4. Click **Predict Ticket**.
5. The system predicts:
   - Ticket Category
   - Ticket Priority
   - Assigned Team
   - Recommended SLA
   - Confidence Score

---

# 📌 Business Value

This system helps organizations:

- Reduce manual ticket triaging
- Improve response times
- Automate support workflows
- Prioritize critical issues
- Increase operational efficiency
- Enhance customer satisfaction

---

# 🚀 Future Improvements

- Deep Learning models (LSTM/BERT)
- Multi-label ticket classification
- Sentiment Analysis
- Auto Ticket Routing
- Email Integration
- CRM Integration
- Real-time API Deployment
- Explainable AI (XAI)
- User Authentication
- Dashboard Analytics

---

# 👨‍💻 Author

**Devansh**

Future Interns Machine Learning Internship

Project: FUTURE_ML_02

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- Future Interns
- Kaggle
- Scikit-learn
- Streamlit
- NLTK
- Open Source Community

---

## 📬 Feedback

If you have any suggestions or feedback, feel free to open an issue or contribute to the project.

⭐ If you found this project helpful, consider giving it a star on GitHub.
