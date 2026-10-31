import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

veri = pd.read_csv("skulls.csv")

x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression

model.fit(x_train, y_train)

tahminler = model.predict(x_test)

hata = mean_absolute_error(y_test, tahminler)

print("Gerçek Değerler: ")
print(y_test.head())

print("tahminler: ")
print(tahminler[:5])

print("ortalama mutlak hata: ", hata)
