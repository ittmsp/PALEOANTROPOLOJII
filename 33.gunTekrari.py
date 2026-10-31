import cv2
import matplotlib.pyplot as plt
import numpy as np

gorsel = cv2.imread("skullss.jpg")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(
    gri, cv2.CV_64F, 1, 0, ksize=3
)

sobel_y = cv2.Sobel(
    gri, cv2.CV_64F, 0, 1, ksize=3
)

kenarlar = np.sqrt(sobel_x**2 + sobel_y**2)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gri, cmap="gray")
plt.title("gri görüntü")
plt.axis("off")


plt.subplot(1, 3, 2)
plt.imshow(sobel_x, cmap="gray")
plt.title("Sobel X")
plt.axis("off")



plt.subplot(1, 3, 3)
plt.imshow(kenarlar, cmap="gray")
plt.title("kenar kuvveti")
plt.axis("off")

plt.tight_layout()
plt.show()"""

gorsel = cv2.imread("skullss.jpg")

if gorsel is None:
    raise FileNotFoundError("yok")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)
bulanik = cv2.GaussianBlur(gri, (5, 5), 0)
canny = cv2.Canny(bulanik, 50, 150)

"""plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gri, cmap="gray")
plt.title("orijinal görüntü")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(canny, cmap="gray")
plt.title("Canny kenarları")
plt.axis("off")

plt.tight_layout()
plt.show()
"""
konturlar, hiyerarsi = cv2.findContours(
    canny,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
    
)

sonuc = gorsel.copy()

if konturlar:
    en_buyuk = max(konturlar, key=cv2.contourArea)
    
    cv2.drawContours(
        sonuc,
        [en_buyuk],
        (0, 255, 0),
        2
    )
    
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2GRAY)
plt.imshow(sonuc_rgb)
plt.title("en buyuk kontur")
plt.axis("off")
plt.show()