import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ab = pd.read_csv("skulls3.csv")

X = ab[["skull_length", "skull_width"]]
y = ab["face_height"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

tahmin = model.predict(X_test)

print("MODEL DEĞERLENDİRME")

mae = mean_absolute_error(y_test, tahmin)

mse = mean_squared_error(y_test, tahmin)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, tahmin)