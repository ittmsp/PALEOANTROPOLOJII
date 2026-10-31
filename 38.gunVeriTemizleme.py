import pandas as pd

tablo = pd.read_csv("kafatasi_olcumleri.csv")

print("orijinal tablo")
print(tablo)

print("eksik veriler")
print(tablo.isnull().sum())

print("tekrarların satır sayısı")
print(tablo.duplicated().sum())

print("gecersiz yükseklikler")
print(tablo[tablo["yukseklik_piksel"] <= 0])

print("gecersiz genislikler")
print(tablo[tablo["genislik_piksel"] <= 0])

temiz_tablo = tablo.dropna().drop_duplicates()
temiz_tablo.to_csv("kafatasi_olcumleri_temiz.csv", index=False)

print("\ntemizlenmiş tablo")
print(temiz_tablo)