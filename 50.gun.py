import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold, cross_val_score

veri = pd.read_csv("skulls3.csv")

x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

katlar = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42,
)

model = DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

sonuclar = cross_val_score(
    model,
    x,
    y,
    cv=katlar,
    scoring="neg_mean_absolute_error"
)

mae_degerleri = -sonuclar

print("her turun mae değeri")
print(mae_degerleri)

print("ortalama mae:", mae_degerleri.mean())
print("standart sapma: ", mae_degerleri.std())