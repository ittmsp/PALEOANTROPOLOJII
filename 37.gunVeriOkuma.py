import pandas as pd

tablo = pd.read_csv("kafatasi_olcumleri")

print(tablo.head())
print(tablo.columns)
print(tablo.describe())

