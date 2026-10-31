import pandas as pd
import matplotlib.pyplot as plt

ab = pd.read_csv("skulls3.csv")
"""print(ab.head())

plt.scatter(ab["skull_length"], [ab["face_height"]])
plt.xlabel("Kafatası uzunluğu")
plt.ylabel("Yüz Yüksekliği")

plt.title("Kafatası Uzunluğu ve Yüz Yüksekliği Arasındaki ilişki")
plt.show()"""

"""korelasyon = ab["skull_length"].corr(ab["face_height"])
print("Korelasyon", korelasyon)
print(ab.corr(numeric_only=True))"""

plt.scatter(ab["skull_length"], ab["face_height"])

plt.xlabel("Kafatası Uzunluğu")
plt.ylabel("Yüz Yüksekliği")
plt.title("Kafatası Yüksekliği")

plt.show()

korelasyon = ab["skull_length"].corr(ab["face_height"])

print("Korelasyon", korelasyon)
print()

print("-----KORELASYON MATRİSİ-----")
print(ab.corr(numeric_only=True))