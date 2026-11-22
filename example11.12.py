import numpy as np

training = np.array([6., 8., 10., 12., 14.])
mean = training.mean()
std = training.std()
standardized = (training - mean) / std
new_value = 14.

print(f"Training mean: {mean:.1f}")
print(f"Training SD: {std:.3f}")
print("Standardized values:",
      np.round(standardized, 2))
print(f"New value z-score: {(new_value-mean)/std:.2f}")

