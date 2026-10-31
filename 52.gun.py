import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.metrics import mean_absolute_error

veri = pd.read_csv("skulls3.csv")
x = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

katlar = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model = DecisionTreeRegressor(random_state=42)

parametreler = {
    "max_depth": [1, 2, 3, 5, 10]
}

arama = GridSearchCV(
    estimator=model,
    param_grid=parametreler,
    cv=katlar,
    scoring="neg_mean_absolute_error"
)

arama.fit(x_train, y_train)
print("en iyi parametre: ", arama.best_params_)
print("en iyi mae: ", -arama.best_score_)

sonuclar = pd.DataFrame(arama.cv_results_)
sonuclar["ortalama_mae"] = -sonuclar["mean_test_score"]
sonuclar["standart_sapma"] = sonuclar["std_test_score"]

print("Tüm sonuçlar")
print(
    sonuclar[
        ["param_max_depth", "ortalama_mae", "standart_sapma"]
    ].sort_values(by="ortalama_mae")
)

en_iyi_model = arama.best_estimator_
tahminler = en_iyi_model.predict(x_test)
mae = mean_absolute_error(y_test, tahminler)
print("test mae:", mae)