import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold, cross_val_score

veri = pd.read_csv("skulls3.csv")

x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

katlar = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

derinlikler = [1, 2, 3, 5, 10]

sonuclar = []

for derinlik in derinlikler:
    model = DecisionTreeRegressor(
        max_depth=derinlik,
        random_state=42
    )
    
    skorlar = cross_val_score(
        model,
        x,
        y,
        cv_katlar,
        scoring="neg_mean_absolute_error"
        
        mae_degerleri = -skorlar
        ortalama_mae = mae_degerleri.mean()
        sonuclar.append({
                "Derinlik": derinlik,
                "Ortalama": ortalama_mae,
                "Standart sapma": mae_degerleri.std()
                })
    )
sonuc_tablosu = pd.DataFrame(sonuclar)

sonuc_tablosu = sonuc_tablosu.sort_values(
    by="ortalama_mae"
)

print(sonuc_tablosu.round(3))

en_iyi = sonuc_tablosu.iloc[0]

print("\nEn iyi aday derinlik:", en_iyi["Derinlik"])
print("ortalama mae:", round(en_iyi["Ortalama_MAE"], 3))