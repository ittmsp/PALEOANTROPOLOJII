import pandas as pd
import matplotlib.pyplot as plt
ab = pd.read_csv("skulls3.csv")
average = ab.groupby("species")["skull_length"].mean()
print(average)
plt.bar(average.index, average.values)
plt.title("Türlere göre ortalama kafatası uzunluğu")
plt.xlabel("insan türü")
plt.ylabel("ortalama kafatası uzunluğu")
for i, value in enumerate(average.values):
    plt.text(i, value, round(value, 2), ha="center")
plt.show()
