import pandas as pd
import matplotlib.pyplot as plt

tablo = pd.read_csv("kafatasi_olcumleri_temiz.csv")

print(tablo.head())
print(tablo.columns)

plt.scatter(
    tablo["genislik_piksel"],
    tablo["yukseklik_piksel"]
)

plt.xlabel("genislik (piksel)")
plt.ylabel("yukseklik (piksel)")
plt.title("genislik ve yukseklik")

plt.show()