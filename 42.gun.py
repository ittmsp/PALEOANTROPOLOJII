import pandas as pd
from sklearn.model_selection import train_test_split

veri = pd.read_csv("skulls3.csv")

x = veri[["skull_length", "skull_width"]]

y = veri["face_height"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("x_train: ", x_train.shape)
print("x_test: ", x_test.shape)
print("y_train: ", y_train.shape)
print("y_test: ", y_test.shape)
