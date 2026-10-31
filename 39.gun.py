import pandas as pd
import matplotlib.pyplot as plt

tablo = pd.read_csv("kafatasi_olcumleri_temiz.csv")

print(tablo.head())

ortalama_genislik = tablo["genislik_piksel"].mean()
ortalama_yukseklik = tablo["yukseklik_piksel"].mean()

print("En buyuk genislik: ", tablo["genislik_piksel"].max())
print("En kucuk genislik: ", tablo["genislik_piksel"].min())

print("En buyuk yukseklik: ", tablo["yukseklik_piksel"].max())
print("En kucuk yukseklik: ", tablo["yukseklik_piksel"].min())

en_genis_satir = tablo["genislik_piksel"].idxmax()
print(tablo.loc[en_genis_satir])

en_dar_satir = tablo["genislik_piksel"].idxmin()
print(tablo.loc[en_dar_satir])

plt.scatter(
    tablo["genislik_piksel"],
    tablo["yukseklik_piksel"]
)

plt.xlabel("genislik")
plt.ylabel("yukseklik")
plt.title("kafatasi goruntulerinin olcumleri")

plt.show()

korelasyon = tablo["genislik_piksel"].corr(
tablo["yukseklik_piksel"]
)
print("Korelasyon", korelasyon)



























