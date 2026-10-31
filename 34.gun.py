import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

if gorsel is None:
    raise FileNotFoundError("Görüntü dosyası bulunamadı")

sonuc = gorsel.copy()

x = 200
y = 150

cv2.circle(
    sonuc,
    (x, y),
    5,
    (0, 0, 255),
    -1
)

sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.imshow(sonuc_rgb)
plt.title("işaretlenen nokta")
plt.axis("off")
plt.show()