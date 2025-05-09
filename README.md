Smart Factory Energy Prediction Challenge
Overview
This project develops a machine learning model to predict equipment energy consumption for SmartManufacture Inc. using sensor data from a manufacturing facility. The goal is to help facility managers optimize operations for energy efficiency.
Author: Tanish Khandelwal
Repository Structure
.
├── data/
│   └── data.csv          # Dataset
├── docs/
│   └── data_description.md  # Feature descriptions
├── notebooks/
│   └── energy_prediction.ipynb  # Main analysis notebook
├── scripts/
│   └── model_utils.py    # Preprocessing and prediction functions
├── reports/
│   └── figures/          # Saved plots
│   └── energy_prediction_report.md  # Final report
└── README.md             # This file

Approach

EDA: Analyzed data distributions, missing values, and relationships. Evaluated random_variable1 and random_variable2 for relevance.
Preprocessing: Handled non-numeric values, missing data, and engineered features.
Feature Selection: Excluded random_variable1 and random_variable2 based on low predictive power.
Model Development: Trained an XGBoost model with cross-validation.
Evaluation: Assessed performance using RMSE, MAE, and R².
Insights: Provided recommendations for energy efficiency.

Results

Model performance metrics are in reports/energy_prediction_report.md.
Key findings:
Temperature and time-based features are strong predictors.
random_variable1 and random_variable2 were excluded.


Recommendations include optimizing HVAC, scheduling production, and maintaining sensors.

How to Run

Ensure Anaconda is installed.
Launch Jupyter Notebook via Anaconda Navigator.
Navigate to D:\DS-Intern-Assignment-Tanish Khandelwal\notebooks.
Open energy_prediction.ipynb.
Run all cells (Shift + Enter).
View the report in reports/energy_prediction_report.md.

Requirements

Python 3.9
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost

