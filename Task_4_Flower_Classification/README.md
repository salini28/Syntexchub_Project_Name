# 🌸 Flower Classification Using Machine Learning

## Project Overview

This project focuses on classifying Iris flowers into three different species using Machine Learning algorithms.

The system predicts the species of an Iris flower based on its measurements.

The three flower species are:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

## Objectives

- Load and understand the Iris dataset.
- Perform Exploratory Data Analysis (EDA).
- Visualize feature relationships.
- Train Machine Learning classification models.
- Evaluate model performance.
- Predict flower species for new inputs.

## Dataset Description

This project uses the built-in Iris dataset from Scikit-learn.

- Total Records: 150
- Total Features: 4

### Features
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Target
- Species

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

## Machine Learning Algorithms

1. Logistic Regression
2. Decision Tree Classifier

## Exploratory Data Analysis (EDA)

The following visualizations were created:

- Histogram
- Species Distribution Bar Chart
- Scatter Plot
- Box Plot
- Pair Plot
- Correlation Heatmap

## Model Evaluation

The models are evaluated using:

- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1-Score

## Flower Prediction System

A prediction system is developed using the trained Logistic Regression model.

Users can enter four flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The system predicts the corresponding flower species.

## Project Structure

```text
Task_4_Flower_Classification/
│
├── models/
├── notebooks/
├── src/
├── outputs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Navigate to the src directory:

```bash
cd src
```

Run the prediction program:

```bash
python predict.py
```

Enter the flower measurements to get the predicted species.

## Author

**Name:** Your Name

**Internship:** Syntexchub

**Project:** Task 4 - Flower Classification

## Conclusion

This project demonstrates how Machine Learning algorithms can classify Iris flower species based on their physical measurements. It provides practical experience in data preprocessing, data visualization, model training, evaluation, and prediction.
