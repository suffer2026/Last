import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

data = load_wine(as_frame=True)
df = data.frame.copy()

# Convert multiclass target into binary target
df["target"] = (df["target"] == 0).astype(int)

selected_features = [
    "alcohol",
    "flavanoids",
    "color_intensity",
    "proline"
]

df = df[selected_features + ["target"]]

print("First 5 rows of the dataset:")
print(df.head())
print("\nSelected features:", selected_features)
print("\nDataset shape:", df.shape)
print("\nTarget value counts:")
print(df["target"].value_counts())

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy, 4))
print("\nConfusion Matrix:")
print(cm)

print("\nEnter values for a new prediction.")
print("Press Enter to use the mean value for that feature.\n")

default_values = X_train.mean(numeric_only=True)
user_values = []

for col in X.columns:
    value = input(f"{col} [{default_values[col]:.4f}]: ").strip()
    if value == "":
        user_values.append(default_values[col])
    else:
        user_values.append(float(value))

user_df = pd.DataFrame([user_values], columns=X.columns)

prediction = model.predict(user_df)[0]
probabilities = model.predict_proba(user_df)[0]

print("\nPrediction Result:")
if prediction == 1:
    print("Predicted class: class_0")
else:
    print("Predicted class: not_class_0")

print("\nPrediction Probabilities:")
print(f"not_class_0: {probabilities[0]:.4f}")
print(f"class_0:     {probabilities[1]:.4f}")







