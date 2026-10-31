import cv2
import matplotlib.pyplot as plt

gorsel = cv2.imread("skullss.jpg")

gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2RGB)

bulanik = cv2.GaussianBlur(gri, (5, 5), 0)

plt.imshow(bulanik, cmap="gray")
plt.title("hazirlanan goruntu")
plt.axis("off")
plt.show()

