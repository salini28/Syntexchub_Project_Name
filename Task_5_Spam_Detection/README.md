# SMS Spam Detection Using Machine Learning

## Project Overview

This project is a Machine Learning-based SMS Spam Detection System. It classifies SMS messages into two categories: **Spam** and **Ham (Genuine Message)**.

The system uses text preprocessing and machine learning algorithms to identify unwanted spam messages.

## Objectives

- Analyze SMS messages using Exploratory Data Analysis (EDA).
- Clean and preprocess text data.
- Convert text messages into numerical features.
- Train Machine Learning classification models.
- Evaluate model performance.
- Predict whether a new SMS message is Spam or Ham.

## Dataset

**UCI SMS Spam Collection Dataset**

The dataset contains SMS messages classified into two categories:

- Ham – Genuine messages.
- Spam – Unwanted or promotional messages.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- Joblib

## Machine Learning Algorithms

1. Multinomial Naive Bayes
2. Logistic Regression

## Text Preprocessing

- Convert text to lowercase.
- Remove punctuation.
- Remove numbers.
- Remove English stopwords.
- Tokenize messages.

## Feature Extraction

- CountVectorizer
- TF-IDF Vectorizer

## Model Evaluation

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

## Project Structure

```text
Task_5_Spam_Detection/
│
├── models/
│   └── spam_detection_pipeline.pkl
│
├── notebooks/
│   └── Spam_Detection.ipynb
│
├── src/
│   └── predict.py
│
├── outputs/
│   ├── spam_ham_distribution.png
│   ├── message_length_distribution.png
│   ├── message_length_boxplot.png
│   ├── model_comparison.png
│   ├── naive_bayes_confusion_matrix.png
│   └── logistic_regression_confusion_matrix.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository and navigate to the project folder.

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the prediction system:

```bash
python src/predict.py
```

Enter an SMS message when prompted.

The system will display one of the following predictions:

- Spam
- Ham

## Example

**Input:**

```text
Congratulations! You won a free prize. Claim now!
```

**Expected Prediction:**

```text
Spam
```

## Author

Data Science Internship Project

## Project Category

Machine Learning | Natural Language Processing | Text Classification
