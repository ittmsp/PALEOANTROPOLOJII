import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import ( mean_absolute_error, mean_squared_error, r2_score)

veri = pd.read_csv("skulls3.csv")

x = veri [["skull_length", "skull_width"]]
y = veri ["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

tahminler = model.predict(x_test)

mae = mean_absolute_error

mse = mean_squared_error 

rmse  = mse ** 0.5

r2 = r2_score(y_test, tahminler)

print("mae: ", mae)
print("mse: ", mse)
print("rmse: ", rmse)
print("r2: ", r2)