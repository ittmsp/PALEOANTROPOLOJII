import pandas as pd
ab = pd.read_csv("skulls3.csv")
print(ab.head())

x = ab[["skull_length", "skull_width"]]
print(x)

y = ab["face_height"]
print(y)

print(x.shape)
print(y.shape)
