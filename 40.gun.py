import pandas as pd

tablo = pd.read_csv("kafatasi_olcumleri_temiz.csv")
print(tablo.head())

ortalama = tablo["genislik_piksel"].mean()

standart_sapma = tablo["genislik_piksel"].std()

print("ortalama: ", ortalama)
print("standart sapma: ", standart_sapma)

tablo["z_skoru"] = (
    tablo["genislik_piksel"] - ortalama
) / standart_sapma

print(tablo[["goruntu", "genislik_piksel", "z_skoru"]])

supheli_degerler = tablo[
    tablo["z_skoru"].abs() > 3
]

print(supheli_degerler)