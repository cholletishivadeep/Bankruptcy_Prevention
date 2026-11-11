# Bankruptcy_Prevention
1. Project Overview

The Bankruptcy Prevention System is a Machine Learning classification project that predicts whether a company is likely to face bankruptcy based on six business risk factors.

The main objective is to identify companies that may be at risk of bankruptcy and support better business decision-making.

2. Problem Statement

To build a Machine Learning classification model that predicts whether a company belongs to the bankruptcy or non-bankruptcy category using its business risk factors.

3. Dataset Information

Dataset: Bankruptcy Prevention Dataset

Total Records: 250

Input Features: 6

Target Variable: class

Problem Type: Binary Classification

4. Input Features

Industrial Risk

Management Risk

Financial Flexibility

Credibility

Competitiveness

Operating Risk

5. Target Variable

The target variable contains two classes:

0 – Bankruptcy

1 – Non-Bankruptcy

6. Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Joblib

Streamlit

7. Project Workflow

Data Loading

Data Cleaning

Exploratory Data Analysis (EDA)

Data Preprocessing

Model Building

Model Evaluation

Model Comparison

Model Saving

Streamlit Deployment

8. Machine Learning Algorithms

The following classification algorithms were considered:

Logistic Regression

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Decision Tree

Random Forest

Gradient Boosting

9. Streamlit Application

The trained Machine Learning model is integrated into a Streamlit web application.

Users can enter the six company risk factors and receive a prediction:

Bankruptcy Predicted

Non-Bankruptcy Predicted

10. Project Structure

Bankruptcy-Prevention/
│
├── app.py
├── bankruptcy_model.pkl
├── requirements.txt
├── README.md
└── Bankruptcy_prevention_Dataset(1).csv

Note: The dataset file is optional for running the deployed application if the trained model is already saved.

11. How to Run the Project Locally

Step 1: Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open the project folder

cd Bankruptcy-Prevention

Step 3: Install the required libraries

pip install -r requirements.txt

Step 4: Run the Streamlit application

streamlit run app.py

12. Project Objective

The objective of this project is to apply Machine Learning classification techniques to identify potential bankruptcy risk and develop an interactive web application for company bankruptcy prediction.

13. Author

Shivadeep

14. Application Link

