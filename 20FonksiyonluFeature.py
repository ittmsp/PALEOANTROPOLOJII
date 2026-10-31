import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def model_test(feature):
    ab = pd.read_csv("skulls3.csv")
    X = ab[feature]
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

    return r2

r2_uzunluk = model_test(["skull_length"])

r2_genislik = model_test(["skull_width"])

r2_ikisi = model_test([
    "skull_length",
    "skull_width"
])

print("----- SONUÇLAR -----")

print("Sadece skull_length:", r2_uzunluk)

print("Sadece skull_width :", r2_genislik)

print("İkisi birlikte     :", r2_ikisi)