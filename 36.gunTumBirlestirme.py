import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)
bulanik = cv2.GaussianBlur(gri, (5, 5), 0)

kenarlar= cv2.Canny(bulanik, 50, 150)

konturlar, hiyerarsi = cv2.findContours(
    kenarlar,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("kontur sayisi: ", len(konturlar))

sonuc = gorsel.copy()

if konturlar:
    en_buyuk = max(konturlar, key=cv2.contourArea)
    
    alan = cv2.contourArea(en_buyuk)
    cevre = cv2.arcLength(en_buyuk, True)
    
    print("Alan: ", alan, "piksel kare")
    print("Cevre: " , cevre, "piksel")
    
    cv2.drawContours(
        sonuc,
        [en_buyuk],
        -1,
        (0, 255, 0),
        2
    )
    
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gri, cmap="gray")
plt.title("Gri goruntu")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(kenarlar, cmap="gray")
plt.title("Kenarlar")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(sonuc_rgb)
plt.title("Kontur")
plt.axis("off")

plt.tight_layout()
plt.show()