import cv2
import matplotlib.pyplot as plt
import numpy as np

gorsel = cv2.imread("skullss.jpg")

if gorsel is None:
    raise FileNotFoundError(
        "kafatasi.jpg bulunuamadi"
    )
    
gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(
    gri, cv2.CV_64F, 1, 0, ksize=3
)

sobel_y = cv2.Sobel(
    gri, cv2.CV_64F, 1, 0, ksize=3
)

kenarlar = np.sqrt(sobel_x**2 + sobel_y**2)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gri, cmap="gray")
plt.title("Gri görüntü")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(sobel_x, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(kenarlar, cmap="gray")
plt.title("Kenar kuvveti")
plt.axis("off")

plt.tight_layout()
plt.show()