import pandas as pd
import matplotlib.pyplot as plt

ab = pd.read_csv("skulls3.csv")
print(ab.head())

average = ab.groupby("species")[["skull_length", "skull_width", "face_height"]].mean()
print(average)
length = average["skull_length"]
plt.bar(length.index, length.values)
plt.title("türlere göre ortalama kafatası uzunluğu")
plt.xlabel("tür")
plt.ylabel("kafatası uzunluğu")
plt.plot(average.index, average["skull_length"], marker="o", label="kafatası uzunluğu")
plt.show()

width = average["skull_width"]

plt.bar(width.index, width.values)
plt.title("türlere göre ortalama kafatası genişliği")
plt.xlabel("tür")
plt.ylabel("kafatası genişliği")
plt.plot(average.index, average["skull_width"], marker="o", label="kafatası genişliği")


plt.legend()



plt.show()