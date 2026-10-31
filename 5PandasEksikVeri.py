import pandas as pd
ab = pd.read_csv("skulls3.csv")

ab.loc[1, "skull_length"] = None
print(ab.isnull().sum())
print(ab.describe())
print(ab["species"].unique())
print(ab["species"].value_counts())