import matplotlib.pyplot as plt
turler = ["Homo sapiens", "Neanderthal", "Homo erectus"]
uzunluklar = [176, 185, 190]
plt.bar(turler, uzunluklar)
plt.title("İnsan türlerine göre kafatası uzunluğu")
plt.xlabel("İnsan Türü")
plt.ylabel("Kafatası uzunluğu")
plt.show()