import cv2
import math
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

sonuc = gorsel.copy()

noktalar = {
    "ust": (200, 50),
    "alt": (200, 400),
    "sol": (80, 220),
    "sag": (320, 220)
}

for isim, (x, y) in noktalar.items():
    cv2.circle(sonuc, (x, y), 5, (0, 0, 255), -1)
    
    cv2.putText(
        sonuc,
        isim,
        (x + 8, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        1
    )
x1, y1 = noktalar["ust"]
x2, y2 = noktalar["alt"]

yukseklik = math.dist((x1, y1), (x2, y2))

print("Yukseklik: ", yukseklik, "piksel")

genislik = math.dist((x1, y1), (x2, y2))

print("Genislik: ", genislik, "piksel")

sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.imshow(sonuc_rgb)
plt.title("Kafatsı üzerindeki örnek ölçümler")
plt.axis("off")
plt.show()