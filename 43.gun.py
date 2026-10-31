import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


veri = pd.read_csv("skulls3.csv")

x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(x_train, y_train)

tahminler = model.predict(x_test)

print("gercek degeler: ")
print(y_test.head())

print("model tahminler: ")
print(tahminler[:5])

sonuclar = pd.DataFrame({
    "gercek_deger": y_test.to_numpy(),
    "tahmin": tahminler
}, index=y_test.index)

sonuclar["mutlak_hata"] = (
    sonuclar["gercek_deger"] - sonuclar["tahmin"]
).abs()

print(sonuclar)

hata = mean_absolute_error(y_test, tahminler)
print("ortalama mutlak hata: ", hata)





alt = min(y_test.min(), tahminler.min())
ust = max(y_test.max(), tahminler.max())

plt.scatter(y_test, tahminler)
plt.plot([alt, ust], [alt, ust])

plt.xlabel("gercek yuz yuksekligi")
plt.ylabel("tahmin edilen yuz yuksekligi")
plt.title("tahmin basarisini inceleme")

plt.show()

