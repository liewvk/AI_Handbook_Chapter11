import numpy as np

data = np.array([
    [2, 50],
    [4, 62],
    [6, 76],
    [8, 88]
])

print("Matrix shape:", data.shape)
print("First row:", data[0])
print("All scores:", data[:, 1])
print("Last two rows:\n", data[-2:])

