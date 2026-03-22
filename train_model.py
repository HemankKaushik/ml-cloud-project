import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load data (The Iris flower dataset)
data = load_iris()
X = data.data
y = data.target

# 2. Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# 3. Save the model to a file (This is what we 'deploy' to the cloud)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl!")