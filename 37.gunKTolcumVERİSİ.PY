import pandas as pd

veriler = {
    "goruntu": [
        "kafatasi1.jpg",
        "kafatasi2.jpg",
        "kafatasi3.jpg"
    ],
    "yukseklik_piksel": [350, 320, 370],
    "genislik_piksel": [240, 225, 260]
}

tablo = pd.DataFrame(veriler)

print(tablo)

tablo.to_csv(
    "kafatasi_olcumleri.csv",
    index=False
)

print("olcum tablosu kaydedildi")