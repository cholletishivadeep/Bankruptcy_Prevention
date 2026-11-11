# Bankruptcy_Prevention
Project Overview

The Bankruptcy Prevention System is a Machine Learning classification project that predicts whether a company is likely to face bankruptcy based on different business risk factors.

The objective is to help identify companies that may be at risk of bankruptcy and support better business decision-making.

Problem Statement

To develop a classification model that predicts whether a company belongs to the bankruptcy or non-bankruptcy category using six business risk factors.

Dataset Information

Dataset: Bankruptcy Prevention Dataset

Total Records: 250

Total Features: 6

Target Variable: class

Problem Type: Binary Classification

Input Features

Industrial Risk

Management Risk

Financial Flexibility

Credibility

Competitiveness

Operating Risk

Target Variable

0 – Bankruptcy

1 – Non-Bankruptcy

Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Joblib

Streamlit

Project Workflow

Data Loading

Data Cleaning

Exploratory Data Analysis (EDA)

Data Preprocessing

Model Building

Model Evaluation

Model Comparison

Model Saving

Streamlit Deployment

Machine Learning Models

The project explores multiple classification algorithms:

Logistic Regression

K-Nearest Neighbors

Support Vector Machine

Decision Tree

Random Forest

Gradient Boosting

Streamlit Application

The trained model is integrated into a Streamlit web application.

Users can enter the six company risk factors and receive a bankruptcy prediction.

Project Structure

Bankruptcy-Prevention/
│
├── app1.py
├── bankruptcy_model.pkl
├── requirements.txt
├── README.md
└── Bankruptcy_prevention_Dataset(1).csv

How to Run the Project Locally

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Install the required libraries:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app1.py

Project Objective

To apply Machine Learning classification techniques to identify bankruptcy risk and build an interactive prediction application.

Author
