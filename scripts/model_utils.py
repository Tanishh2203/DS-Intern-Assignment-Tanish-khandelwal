import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, is_training=True):
    df.replace(['???', 'na', 'NA', 'null', '', 'None'], np.nan, inplace=True)

    for col in df.columns:
        if col != 'timestamp':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Check for non-numeric columns after initial conversion
    print("Data types after initial conversion:")
    print(df.dtypes)
    non_numeric_cols = [col for col in df.columns if col != 'timestamp' and df[col].dtype not in [np.float64, np.int64]]
    if non_numeric_cols:
        print(f"Non-numeric columns found after initial conversion: {non_numeric_cols}")
        for col in non_numeric_cols:
            print(f"Sample values in {col}: {df[col].head().tolist()}")
    
    # Convert timestamp to datetime and extract features
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    df['month'] = df['timestamp'].dt.month
    
    # Feature Engineering
    zone_temp_cols = [col for col in df.columns if 'zone' in col and 'temperature' in col]
    zone_humidity_cols = [col for col in df.columns if 'zone' in col and 'humidity' in col]
    df['avg_zone_temp'] = df[zone_temp_cols].mean(axis=1)
    df['avg_zone_humidity'] = df[zone_humidity_cols].mean(axis=1)
    df['temp_humidity_interaction'] = df['avg_zone_temp'] * df['avg_zone_humidity']
    df['indoor_outdoor_temp_diff'] = df['avg_zone_temp'] - df['outdoor_temperature']
    
    # Lagged energy consumption
    if is_training:
        df['energy_lag1'] = df['equipment_energy_consumption'].shift(1)
    
    # Drop irrelevant columns 
    columns_to_drop = ['timestamp', 'equipment_energy_consumption', 'random_variable1', 'random_variable2']
    if not is_training:
        columns_to_drop.remove('equipment_energy_consumption')
    X = df.drop(columns=columns_to_drop, errors='ignore')
    
    # Print data types and sample values before imputation
    print("\nData types before imputation:")
    print(X.dtypes)
    print("\nSample values before imputation:")
    for col in X.columns:
        print(f"{col}: {X[col].head().tolist()}")
    
    # Impute missing values
    imputer = SimpleImputer(strategy='median')
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    
    # Scale features
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    return X, {'imputer': imputer, 'scaler': scaler}

def predict_energy(model, X):
    y_pred_log = model.predict(X)
    y_pred = np.expm1(y_pred_log)
    return y_pred