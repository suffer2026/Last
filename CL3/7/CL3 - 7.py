import numpy as np
import random

def generate_dummy_data(samples=100, features=3):
    X = np.random.rand(samples, features)
    
    y = []
    for sample in X:
        s = sum(sample)
        if s < 1:
            y.append(0)  # Healthy
        elif s < 2:
            y.append(1)  # Minor Damage
        else:
            y.append(2)  # Severe Damage
    return np.array(X), np.array(y)


class AIS_Model:
    def __init__(self, num_detectors=10, mutation_rate=0.1):
        self.num_detectors = num_detectors
        self.mutation_rate = mutation_rate

    def train(self, X, y):
        indices = np.random.choice(len(X), self.num_detectors, replace=False)
        self.detectors = X[indices]
        self.detector_labels = y[indices]

        # Mutation (Clonal Selection idea)
        for i in range(len(self.detectors)):
            if np.random.rand() < self.mutation_rate:
                self.detectors[i] += np.random.normal(0, 0.1, size=self.detectors[i].shape)

    def predict(self, X):
        predictions = []
        for sample in X:
            distances = np.linalg.norm(self.detectors - sample, axis=1)
            predictions.append(self.detector_labels[np.argmin(distances)])
        return np.array(predictions)


def label_to_text(label):
    if label == 0:
        return "Healthy"
    elif label == 1:
        return "Minor Damage"
    else:
        return "Severe Damage"


X, y = generate_dummy_data(samples=200, features=3)

split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = AIS_Model(num_detectors=15, mutation_rate=0.1)
model.train(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print(f"Model Accuracy: {accuracy:.2f}")


print("\nEnter 3 feature values (between 0 and 1):")
user_input = []

for i in range(3):
    val = float(input(f"Feature {i+1}: "))
    user_input.append(val)

user_input = np.array(user_input).reshape(1, -1)

# Prediction
prediction = model.predict(user_input)[0]
print("\nPrediction:", label_to_text(prediction))
