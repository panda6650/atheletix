import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Sample dataset (in real project, use actual athlete data)
data = {
    'heart_rate': np.random.randint(50, 100, 1000),
    'blood_pressure_sys': np.random.randint(100, 160, 1000),
    'blood_pressure_dia': np.random.randint(60, 100, 1000),
    'oxygen_level': np.random.randint(90, 100, 1000),
    'training_hours': np.random.uniform(10, 40, 1000),
    'age': np.random.randint(18, 40, 1000),
    'weight': np.random.uniform(50, 100, 1000),
    'height': np.random.uniform(150, 200, 1000),
    'injury_risk': np.random.choice([0, 1], 1000, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Features and target
X = df.drop('injury_risk', axis=1)
y = df['injury_risk']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Save model and scaler
joblib.dump((scaler, knn), 'model.pkl')

print(f"Model trained with accuracy: {knn.score(X_test_scaled, y_test):.2f}")
