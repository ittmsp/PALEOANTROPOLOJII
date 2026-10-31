import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


ab = pd.read_csv("skulls3.csv")

print(ab.columns)


X = ab[["skull_length", "skull_width", "skull_height"]]

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

r2 = r2_score(y_test, tahmin)

print("R²:", r2)