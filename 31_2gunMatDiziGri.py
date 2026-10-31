from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

gorsel = Image.open("skullss.jpg")
gri_gorsel = gorsel.convert("L")

plt.imshow(gri_gorsel, cmap="gray")
plt.axis("off")
plt.show()