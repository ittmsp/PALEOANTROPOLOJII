import cv2
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
    cv2.circle(sonuc, (x, y), 5, (0, 0, 255, -1))
    
    cv2.putText(
        sonuc,
        isim,
        (x + 8, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        1
    )
    
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.imshow(sonuc_rgb)
plt.axis("off")
plt.show()