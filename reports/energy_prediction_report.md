# Energy Prediction Report

---

## Approach

- **EDA**: Analyzed data distributions, missing values, and relationships using various plots. Evaluated `random_variable1` and `random_variable2` for relevance.
- **Preprocessing**: Handled non-numeric values in `equipment_energy_consumption`, imputed missing values, and engineered features like `avg_zone_temp` and `temp_humidity_interaction`.
- **Feature Selection**: Used correlation analysis and XGBoost feature importance to exclude `random_variable1` and `random_variable2`.
- **Model Development**: Trained an XGBoost model with cross-validation.
- **Evaluation**: Assessed performance on a test set using RMSE, MAE, and R².

---

## Key Insights

- Temperature-related features (`avg_zone_temp`, `indoor_outdoor_temp_diff`) are strong predictors of energy consumption.
- Time-based features (`hour`, `day_of_week`) indicate daily patterns in energy use.
- `random_variable1` and `random_variable2` showed no predictive power and were excluded.
- The model generalizes well based on cross-validation scores.

---

## Model Performance

- **RMSE**: `115.81 Wh`  
- **MAE**: `37.15 Wh`  
- **R²**: `0.25`

---

## Plots

- Distribution Plot  
- Correlation Matrix  
- Time Series Plot  
- Box Plot  
- Scatter Plot: Energy vs. Temperature  
- Scatter Plot: Energy vs. `random_variable1`  
- Scatter Plot: Energy vs. `random_variable2`  
- Pair Plot  
- Feature Importance Plot  
- Predicted vs. Actual Plot

---

## Recommendations

- **Optimize HVAC**: Adjust cooling in high-temperature zones.
- **Schedule Production**: Shift high-energy tasks to off-peak hours.
- **Sensor Maintenance**: Fix or replace sensors reporting invalid values.
- **Monitor Outdoor Conditions**: Use weather forecasts to proactively adjust indoor settings.

---

## Limitations

- Missing data in some zones may affect prediction accuracy.
- Non-numeric values in the dataset required custom preprocessing.
- Performance on a private holdout or deployment set is not yet evaluated.
- Outliers were not explicitly handled; future work could incorporate robust techniques.

