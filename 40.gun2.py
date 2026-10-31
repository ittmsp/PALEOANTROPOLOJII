import pandas as pd
import matplotlib.pyplot as plt

tablo = pd.read_csv("kafatasi_olcumleri_temiz.csv")

ortalama = tablo["genislik_piksel"].mean()
standart_sapma = tablo["genislik_piksel"].std()

print("ortalama genislik", ortalama)
print("standart sapma: ", standart_sapma)

plt.boxplot(tablo["genislik_piksel"].dropna())
plt.ylabel("genislik (piksel)")
plt.title("kafatasi genisliklerinin dagilimi")
plt.show()

tablo["z_skoru"] = (
    tablo["genislik_piksel"] - ortalama
) / standart_sapma

supheli = tablo[tablo["z_skoru"].abs()>3]

print("supheli deger adaylari", supheli)

plt.boxplot(tablo["genislik_piksel"].dropna())
plt.ylabel("genislik")
plt.title("kafatasi genisliklerinin dagilimi")
plt.show()