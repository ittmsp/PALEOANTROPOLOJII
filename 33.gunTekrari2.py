import cv2
import matplotlib.pyplot as plt

# 1. Görüntüyü oku
gorsel = cv2.imread("skullss.jpg")

# 2. Görüntünün okunup okunmadığını kontrol et
if gorsel is None:
    raise FileNotFoundError(
        "kafatasi.jpg bulunamadı. Dosya yolunu kontrol et."
    )

# 3. Görüntüyü gri tonlara dönüştür
gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

# 4. Görüntüyü bulanıklaştır
bulanik = cv2.GaussianBlur(gri, (5, 5), 0)

# 5. Kenarları tespit et
canny = cv2.Canny(bulanik, 50, 150)

# 6. Konturları bul
konturlar, hiyerarsi = cv2.findContours(
    canny,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 7. Orijinal görüntünün kopyasını oluştur
sonuc = gorsel.copy()

# 8. Kontur varsa en büyüğünü seç ve çiz
if len(konturlar) > 0:
    en_buyuk = max(konturlar, key=cv2.contourArea)

    cv2.drawContours(
        sonuc,
        [en_buyuk],
        -1,
        (0, 255, 0),
        2
    )

    print("En büyük kontur bulundu.")
    print("Kontur alanı:", cv2.contourArea(en_buyuk))

else:
    print("Görüntüde kontur bulunamadı.")

# 9. BGR renk düzenini RGB'ye dönüştür
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

# 10. Sonucu göster
plt.figure(figsize=(10, 7))
plt.imshow(sonuc_rgb)
plt.title("En büyük kontur")
plt.axis("off")
plt.tight_layout()
plt.show()