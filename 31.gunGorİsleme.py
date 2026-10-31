from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

gorsel = Image.open("skullss.jpg")

gri_gorsel = gorsel.convert("L")
plt.imshow(gri_gorsel, cmap="gray")
plt.axis("off"),
plt.show()

piksel_verileri = np.array(gri_gorsel)

print(piksel_verileri)
print("Dizi Boyutu: ", piksel_verileri.shape)
print("İlk piksel: ", piksel_verileri[0, 0])
 