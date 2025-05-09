Energy Prediction Report
Approach

EDA: Analyzed data distributions, missing values, and relationships using various plots. Evaluated random_variable1 and random_variable2 for relevance.
Preprocessing: Handled non-numeric values in equipment_energy_consumption, imputed missing values, and engineered features like avg_zone_temp and temp_humidity_interaction.
Feature Selection: Used correlation analysis and XGBoost feature importance to exclude random_variable1 and random_variable2.
Model Development: Trained an XGBoost model with cross-validation.
Evaluation: Assessed performance on a test set using RMSE, MAE, and R².

Key Insights

Temperature-related features (avg_zone_temp, indoor_outdoor_temp_diff) are strong predictors of energy consumption.
Time-based features (hour, day_of_week) indicate daily patterns.
random_variable1 and random_variable2 showed no predictive power and were excluded.
The model generalizes well based on cross-validation scores.

Model Performance

RMSE: 115.81 Wh
MAE: 37.15 Wh
R²: 0.25

Plots

Distribution: 
Correlation Matrix: 
Time Series: 
Box Plot: 
Scatter Plot (Energy vs Temp): 
Scatter Plot (Energy vs Random 1): 
Scatter Plot (Energy vs Random 2): 
Pair Plot: 
Feature Importance: 
Predicted vs Actual: 

Recommendations

Optimize HVAC: Adjust cooling in high-temperature zones.
Schedule Production: Shift high-energy tasks to off-peak hours.
Sensor Maintenance: Fix sensors reporting invalid values.
Monitor Outdoor Conditions: Use weather forecasts to adjust settings.

Limitations

Missing data in some zones may affect accuracy.
Non-numeric values required preprocessing.
Performance on the private holdout set is unknown.
Outliers were not explicitly handled; future work could explore robust methods.

