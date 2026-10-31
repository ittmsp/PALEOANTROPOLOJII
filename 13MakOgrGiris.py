import pandas as pd
from sklearn.model_selection import train_test_split
ab = pd.read_csv("skulls3.csv")
x = ab[["skull_length", "skull_width"]]
y = ab["face_height"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("x:", x.shape)
print("y:", y.shape)

print()

print("x_train:", x_train.shape)
print("x_test:", x_test.shape)

print()

print("y_train", y_train.shape)
print("y_test", y_test.shape)