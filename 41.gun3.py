
import pandas as pd
import matplotlib.pyplot as plt

tablo = pd.read_csv("kafatasi_olcumleri_temiz.csv")
print(tablo.columns)


tablo["yukseklik_genislik_orani"] = (
    tablo["yukseklik_piksel"] / tablo["genislik_piksel"]
)

print(
    tablo[
        [
            "goruntu",
            "yukseklik_piksel",
            "genislik_piksel",
            "yukseklik_genislik_orani"
        ]
    ]
)


ortalama_yukseklik = tablo["yukseklik_piksel"].mean()


tablo["yukseklik_farki"] = (
    tablo["yukseklik_piksel"] - ortalama_yukseklik
)


print(
    tablo[
        [
            "goruntu",
            "yukseklik_piksel",
            "yukseklik_farki"
        ]
    ]
)

print("****************************************")


print(
    tablo[
        [
            "genislik_piksel",
            "yukseklik_piksel",
            "yukseklik_genislik_orani"
        ]
    ].describe()
)
