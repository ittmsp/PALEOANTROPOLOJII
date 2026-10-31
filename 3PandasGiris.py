import pandas as pd

data = {"species": ["Homo Neanderthalensis",
            "Homo Neanderthalensis",
            "Homo Sapiens",
            "Homo Sapiens"
],

"skull_length": [
    185,
    188,
    192,
    190
],

"skull_width": [
    150,
    152,
    153,
    154
],

"face_height": [
    120,
    118,
    121,
    119
]
        }

df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df[["species", "skull_length"]])
print("ortalama", df["skull_length"].mean())
print(df[["species", "skull_width"]])
print("ortalama", df["skull_width"].mean())
print(df[["species", "face_height"]])
print("ortalama", df["face_height"].mean())