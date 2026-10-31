import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

veri = pd.read_csv("skulls3.csv")

X = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

X_train, X_test, y_train, y_test  = train_test_split(
     X, y, random_state=42, test_size=0.2
 )

modeller = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(max_depth=3, random_state=42)
}

for ad, model in modeller.items():
    model.fit(X_train, y_train)
    egitim_tahminleri = model.predict(X_train)
    test_tahminleri = model.predict(X_test)
    
    egitim_mae = mean_absolute_error(y_train, egitim_tahminleri)
    
    test_tahminleri = model.predict(X_test)
    
    egitim_mae = mean_absolute_error(y_train, egitim_tahminleri)
    
    test_mae = mean_absolute_error(y_test, test_tahminleri)
    
    print("\nModel:", ad)
    print("Eğitim MAE:", round(egitim_mae, 2))
    print("Test MAE:", round(test_mae, 2))