import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

if gorsel is None:
    raise FileNotFoundError("Görsel namına hiçbir şey yok")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

bulanik = cv2.GaussianBlur(gri, (5, 5), 0)

canny = cv2.Canny(bulanik, 50, 150)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gri ,cmap="gray")
plt.title("Orijinal Görüntü")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(canny, cmap="gray")
plt.title("Canny kenarları")
plt.axis("off")

plt.tight_layout()
plt.show()