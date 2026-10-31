import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2RGB)

bulanik = cv2.GaussianBlur(gri, (5, 5), 0)

plt.imshow(bulanik, cmap="gray")
plt.title("hazirlanan goruntu")
plt.axis("off")
plt.show()

kenarlar = cv2.Canny(bulanik, 50, 150)

plt.imshow(kenarlar, cmap="gray")
plt.title("Canny kenarlari")
plt.axis("off")
plt.show()

konturlar, hiyerarsi = cv2.findContours(
    kenarlar,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print("bulunan kontur sayisi:", len(konturlar))

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
    
sonuc_rgb = cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB)

plt.imshow(sonuc_rgb)
plt.title("En buyuk kontur")
plt.axis("off")
plt.show()

print("****************************")

if konturlar:
    en_buyuk = max(konturlar, key=cv2.contourArea)
    
    alan = cv2.contourArea(en_buyuk)
    cevre = cv2.arcLength(en_buyuk, True)
    
    print("kontur alan: ", alan, "piksel kare")
    print("kontur cevresi: ", cevre, "piksel")