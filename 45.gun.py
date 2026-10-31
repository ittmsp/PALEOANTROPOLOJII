import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

veri = pd.read_csv("skulls3.csv")

X = veri[["skull_length", "skull_width"]]
y = veri["face_height"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42    
)

modeller = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(
        max_depth=3,
        random_state=42
    )
}

for ad, model in modeller.items():
    model.fit(X_train, y_train)
    tahminler = model.predict(X_test)
    mae = mean_absolute_error(y_test, tahminler)
    mse = mean_squared_error(y_test, tahminler)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, tahminler)
    
    print("/nModel:", ad)
    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R2:", r2)
