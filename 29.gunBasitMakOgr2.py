import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression

ab = pd.read_csv("skulls3.csv")
print(ab.head())
print(ab.columns)

X = ab[["skull_length", "skull_width"]]
y = ab["face_height"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state = 42
)

model1 = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model2 = LinearRegression()

model1.fit(X_train, y_train)
model2.fit(X_train, y_train)

tahmin1 = model1.predict(X_test)
tahmin2 = model2.predict(X_test)

mae1 = mean_absolute_error(y_test, tahmin1)
mae2 = mean_absolute_error(y_test, tahmin2)

r2_1 = r2_score(y_test, tahmin1)
r2_2 = r2_score(y_test, tahmin2)

print("Karar Ağacı MAE: ", mae1)
print("Doğrusal Regresyon MAE: ", mae2)

print("Karar Ağacı R2: ", r2_1)
print("Doğrusal Regresyon R2: ", r2_2)

modeller = ["Karar Ağacı", "doğrusal Regresyon"]
hatalar = [mae1, mae2]
plt.bar(modeller, hatalar)
plt.title("Modellerin Ortalama Mutlak Hataları")
plt.ylabel("MAE")
plt.xlabel("Model")

plt.show()

plt.scatter(y_test, tahmin1)

alt = min(y_test.min(), tahmin1.min())
ust = max(y_test.max(), tahmin1.max)

plt.plot([alt, ust], [alt, ust], linestyle="--")

plt.xlabel("Gerçek Yüz Yüksekliği")
plt.ylabel("Tahmin Edilen Yüz Yüksekliği")
plt.title("Gerçek ve Tahmin Değerleri")
plt.show()