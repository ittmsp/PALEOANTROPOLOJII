import numpy as np
"""skull_lengths = np.array([185, 190, 195, 188, 192])
print(skull_lengths)
print(np.mean(skull_lengths))
print(np.min(skull_lengths))
print(np.max(skull_lengths))
print(np.median(skull_lengths))
print(np.std(skull_lengths))"""

"""data = np.array([[185, 150, 120],
                 [190, 152, 118],
                 [192, 121, 149],
                 [188, 151, 119],
                 [195, 153, 122]])

print(data)
print(data.shape)
print("*****************")
print(data[:, 0])
print(data[:, 1])
print(data[:, 2])
print(np.mean(data[:, 0]))
print(np.mean(data[:, 1]))
print(np.mean(data[:, 2]))"""

data = np.array([[200, 140, 115],
                 [210, 150, 125],
                 [220, 160, 130]])

print("NEANDERTHALENSİS")
print("ortalama kafatasi uzunlugu", np.mean(data[:, 0]))
print("ortalama kafatasi genisligi", np.mean(data[:, 1]))
print("ortalama yuz yuksekligi", np.mean(data[:, 2]))
print("en uzun kafatasi", np.max(data[:, 0]))
print("en kisa kafatasi", np.min(data[:, 0]))