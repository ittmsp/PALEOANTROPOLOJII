import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

if gorsel is None:
    raise FileNotFoundError("Goruntu dosyasi bulunamadi.")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)
bulanik = cv2.GaussianBlur(gri, (5, 5), 0)
canny = cv2.Canny(bulanik, 50, 150)

# Konturları bul
konturlar, hiyerarsi = cv2.findContours(
    canny,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Görüntünün kopyası üzerinde konturları çiz
sonuc = gorsel.copy()

if konturlar:
    en_buyuk = max(konturlar, key=cv2.contourArea)

    cv2.drawContours(
        sonuc,
        [en_buyuk],
        -1,
        (0, 255, 0),
        2
    )

# OpenCV BGR kullanır; Matplotlib için RGB'ye dönüştür
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.imshow(sonuc_rgb)
plt.title("En büyük kontur")
plt.axis("off")
plt.show()