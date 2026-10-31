import pandas as pd
ab = pd.read_csv("skulls3.csv")
print(ab)
print(ab["species"].unique())
print(ab["species"].value_counts())
sapiens = ab[ab["species"] == "Homo sapiens"]
print(sapiens)
print("*****")
print(sapiens["skull_length"].mean())
print(sapiens["skull_width"].mean())
print(sapiens["face_height"].mean())
print("*****")
neanderthal = ab[ab["species"] == "Neanderthal"]
print(neanderthal)
print(neanderthal["skull_length"].mean())
print(neanderthal["skull_width"].mean())
print(neanderthal["face_height"].mean())
print("*****")
erectus = ab[ab["species"] == "Homo erectus"]
print(erectus)
print(erectus["skull_length"].mean())
print(erectus["skull_width"].mean())
print(erectus["face_height"].mean())
print("*****")
print(ab.groupby("species")["skull_length"].mean())
print("*****")
print(ab.groupby("species")[["skull_length", "skull_width", "face_height"]].mean())
print("*****")
print(ab.groupby("species")[["skull_length", "skull_width", "face_height"]].count())
print("*****")
analiz = ab.groupby("species")[["skull_length", "skull_width", "face_height"]].agg(["mean", "min", "max", "sum", "count"])
print(analiz)
print("*****")
average = ab.groupby("species")["skull_length"].mean()
print(average.idxmax)





