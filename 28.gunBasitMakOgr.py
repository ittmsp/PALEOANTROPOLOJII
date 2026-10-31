import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

ab = pd.read_csv("skulls3.csv")

print("İlk satırlar: ")
print(ab.head())
print("Sütunlar: ")
print(ab.columns)
print(ab.isnull().sum())

X = ab[["skull_length", "skull_width"]]
y = ab["face_height"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

tahminler = model.predict(X_test)

print("MAE: ", mean_absolute_error(y_test, tahminler))
mse = mean_squared_error(y_test, tahminler)
print("MSE: ", mean_squared_error(y_test, tahminler))
print("R2: ", r2_score(y_test, tahminler))