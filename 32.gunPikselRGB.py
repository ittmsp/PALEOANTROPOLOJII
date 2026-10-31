from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

gorsel = Image.open("skullss.jpg")
gri_gorsel = gorsel.convert("L")
piksel_verileri = np.array(gri_gorsel)
print(piksel_verileri.shape)

print("Görüntü boyutu: ", gorsel.size)
print("Genişliği: ", gorsel.width)
print("Yüksekliği: ", gorsel.height)

print("Dizi boyutu: ", piksel_verileri.shape)
print("Veri Türü: ", piksel_verileri.dtype)
print("En küçük piksel: ", piksel_verileri.min())
print("En büyük piksel: ", piksel_verileri.max())

print(piksel_verileri[0, 0])
print(piksel_verileri[100, 200])

"""gorsel = Image.open("skullss.jpg").convert("RGB")
renkli_dizi = np.array(gorsel)
print("Görüntü boyutu: ", renkli_dizi.shape)
print("RGB değerleri: ", renkli_dizi[0,0])"""

gorsel = Image.open("skullss.jpg")
kucuk_gorsel = gorsel.resize((100, 100))
plt.imshow(kucuk_gorsel)
plt.axis("off")
plt.show()

print("Yeni boyut: ", kucuk_gorsel.size)

print("******************************************")

yeni_genislik = 700
oran = yeni_genislik / gorsel.width
yeni_yukseklik = int(gorsel.height * oran)

kucuk_gorsel = gorsel.size(
    (yeni_genislik, yeni_yukseklik)
)

print(kucuk_gorsel.size)