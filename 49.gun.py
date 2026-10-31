import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

veri = pd.read_csv("skulls3.csv")

x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=42, test_size=0.2
)

derinlikler = [1, 2, 3, 5, 10]

egitim_hatalari = []
test_hatalari = []

for derinlik in derinlikler:
    model=DecisionTreeRegressor(
        max_depth = derinlik,
        random_state=42
    )
    
    model.fit(x_train, y_train)
    
    egitim_tahminleri = model.predict(x_train)
    test_tahminleri = model.predict(x_test)
    
    egitim_mae = mean_absolute_error(
        y_train, egitim_tahminleri
    )
    test_mae = mean_absolute_error(
        y_test, test_tahminleri
    )
    
    egitim_hatalari.append(egitim_mae)
    test_hatalari.append(test_mae)
    
    print("derinlik: ", derinlik)
    print("eğitim mae: ", round(egitim_mae, 2))
    print("test mae:", round(test_mae, 2))
    print("**************************************")
    
plt.plot(
    derinlikler,
    egitim_hatalari,
    marker = "o",
    label="eğitim mae"
)

plt.plot(
    derinlikler,
    test_hatalari,
    marker="o",
    label="test mae"
)

plt.xlabel("karar ağacı derinliği")
plt.ylabel("mae")
plt.title("derinliğe göre model hataları")
plt.legend()
plt.grid(True)
plt.show()