import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

ab = pd.read_csv("skulls3.csv")

x = ab[["skull_length", "skull_width"]]

y = ab["face_height"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)
tahmin = model.predict(x_test)
print("Tahminler")
print(tahmin)
print("*****")
print("Gerçek Değerler:")
print(y_test.values)
print("*****")
skor = model.score(x_test, y_test)
print("Model Skoru", skor)