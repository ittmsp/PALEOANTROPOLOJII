import pandas as pd
import matplotlib.pyplot as plt

tablo = pd.read_csv("kafatasi_olcumleri.csv")

plt.scatter(
    tablo["genislik_piksel"],
    tablo["yukseklik_piksel"]
)

plt.xlabel("Genislik(piksel)")
plt.ylabel("Yukseklik(piksel)")
plt.title("Kafatasi goruntulerinin olcumleri")
plt.grid(True)
plt.show()