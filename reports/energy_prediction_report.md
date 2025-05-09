# Energy Prediction Report

## Approach
1. **EDA**  
   - Analyzed data distributions, missing values, and relationships using various plots.  
   - Evaluated `random_variable1` and `random_variable2` for relevance.

2. **Preprocessing**  
   - Handled non-numeric values in `equipment_energy_consumption`.  
   - Imputed missing values.  
   - Engineered features like `avg_zone_temp` and `temp_humidity_interaction`.

3. **Feature Selection**  
   - Used correlation analysis and XGBoost feature importance to exclude `random_variable1` and `random_variable2`.

4. **Model Development**  
   - Trained an XGBoost model with cross-validation.

5. **Evaluation**  
   - Assessed performance on a test set using RMSE, MAE, and R².

---

## Key Insights
- Temperature-related features (`avg_zone_temp`, `indoor_outdoor_temp_diff`) are strong predictors of energy consumption.
- Time-based features (`hour`, `day_of_week`) indicate daily usage patterns.
- `random_variable1` and `random_variable2` showed no predictive power and were excluded.
- The model generalizes well based on cross-validation scores.

---

## Model Performance
- **RMSE**: 115.81 Wh  
- **MAE**: 37.15 Wh  
- **R²**: 0.25  

---

## Plots
![Distribution of Energy Consumption](reports/figures/distribution.png)  
*Distribution*

![Correlation Matrix](reports/figures/correlation_matrix.png)  
*Correlation Matrix*

![Time Series of Energy Consumption](reports/figures/time_series.png)  
*Time Series*

![Box Plot of Energy by Category](reports/figures/box_plot.png)  
*Box Plot*

![Energy vs. Temperature Scatter](reports/figures/scatter_energy_temp.png)  
*Scatter Plot (Energy vs Temp)*

![Energy vs. Random Variable 1](reports/figures/scatter_energy_random1.png)  
*Scatter Plot (Energy vs Random 1)*

![Energy vs. Random Variable 2](reports/figures/scatter_energy_random2.png)  
*Scatter Plot (Energy vs Random 2)*

![Pair Plot of Features](reports/figures/pair_plot.png)  
*Pair Plot*

![Feature Importance](reports/figures/feature_importance.png)  
*Feature Importance*

![Predicted vs Actual Energy](reports/figures/predicted_vs_actual.png)  
*Predicted vs Actual*

---

## Recommendations
- **Optimize HVAC**: Adjust cooling in high-temperature zones.  
- **Schedule Production**: Shift high-energy tasks to off-peak hours.  
- **Sensor Maintenance**: Fix sensors reporting invalid values.  
- **Monitor Outdoor Conditions**: Use weather forecasts to adjust settings.

---

## Limitations
- Missing data in some zones may affect accuracy.  
- Non-numeric values required extensive preprocessing.  
- Performance on the private holdout set is unknown.  
- Outliers were not explicitly handled; future work could explore robust methods.
