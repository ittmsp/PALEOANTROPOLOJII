import pandas as pd
ab = pd.read_csv("skulls3.csv")
print(ab)
"""print("**********************")
print(ab.tail())
print("**********************")
print(ab.shape)
print("**********************")
print(ab.columns)
print("**********************")
print(ab[["face_height", "skull_length"]])
print("**********************")
print("average of face height:", ab["face_height"].mean())
print("**********************")
print(ab.info())
print("**********************")
print(ab.describe())"""

ab = pd.read_csv("skulls3.csv")

print("---- VERİ SETİ ----")
print(ab)

print()
print("Kayıt Sayısı:", len(ab))
print("Veri Boyutu", ab.shape)

print()
print("Kafatası Uzunluğu Ortalaması", ab["skull_length"].mean())
print("Kafatası Genişliği", ab["skull_width"].mean())
print("Yüz Yüksekliği", ab["face_height"].mean())
