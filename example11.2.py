import numpy as np

hours = np.array([2, 4, 6, 8], dtype=float)
scores = np.array([50, 62, 76, 88])

print("Hours:", hours)
print("Shape:", hours.shape)
print("Dimensions:", hours.ndim)
print("Scaled hours:", hours * 1.5)
print("Score increase:", scores + 5)

