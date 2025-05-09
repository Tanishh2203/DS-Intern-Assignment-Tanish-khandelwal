# Smart Factory Energy Prediction Challenge

## Overview
This project develops a machine learning model to predict equipment energy consumption for SmartManufacture Inc. using sensor data from a manufacturing facility. The goal is to help facility managers optimize operations for energy efficiency.  
**Author**: Tanish Khandelwal

---

## Repository Structure

```
.
├── data/
│ └── data.csv # Dataset
├── notebook/
│ └── energy_prediction.ipynb 
├── scripts/
│ └── model_utils.py 
├── reports/
│ ├── figures/ 
│ └── energy_prediction_report.md # Final report
└── README.md

```

---

## Approach

### 1. **Exploratory Data Analysis (EDA)**
- Analyzed data distributions, missing values, and relationships.
- Evaluated `random_variable1` and `random_variable2` for relevance.

### 2. **Preprocessing**
- Handled non-numeric values, missing data, and engineered features.

### 3. **Feature Selection**
- Excluded `random_variable1` and `random_variable2` based on low predictive power.

### 4. **Model Development**
- Trained an XGBoost model with cross-validation.

### 5. **Evaluation**
- Assessed performance using RMSE, MAE, and R².

### 6. **Insights**
- Provided recommendations for energy efficiency.

---

## Results

Model performance metrics are available in `reports/energy_prediction_report.md`.

### Key Findings:
- Temperature and time-based features are strong predictors.
- `random_variable1` and `random_variable2` were excluded due to low relevance.

### Recommendations:
- Optimize HVAC systems.
- Schedule production more effectively.
- Maintain sensors for better data accuracy.

---

## How to Run

1. Ensure **Anaconda** is installed.
2. Launch **Jupyter Notebook** via **Anaconda Navigator**.
3. Navigate to the following directory:  
   `D:\DS-Intern-Assignment-Tanish Khandelwal\notebooks`
4. Open `energy_prediction.ipynb`.
5. Run all cells (`Shift + Enter`).
6. View the report in `reports/energy_prediction_report.md`.

---

## Requirements

- Python 3.9  
- Libraries:
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  
  - scikit-learn  
  - xgboost
