from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

gorsel = Image.open("skullss.jpg")

print("Genişlik: ", gorsel.width)
print("Yükseklik: ", gorsel.height)
print("Renk modu: ", gorsel.mode)

gri_gorsel = gorsel.convert("L")
piksel_verileri = np.array(gri_gorsel)

print("Dizi boyutu: ", piksel_verileri.size)
print("Veri türü: ", piksel_verileri.dtype)
print("en küçük değer: ", piksel_verileri.min())
print("en büyük değer: ", piksel_verileri.max())

print("ilk piksel: ", piksel_verileri[0, 0])

plt.imshow(gri_gorsel, cmap="gray")
plt.axis("off")
plt.show()