import numpy as np

scores = np.array([50, 62, 76, 88], dtype=float)
print(f"Mean: {np.mean(scores):.2f}")
print(f"Minimum: {np.min(scores):.0f}")
print(f"Maximum: {np.max(scores):.0f}")
print(f"Population SD: {np.std(scores):.2f}")
print(f"Sample SD: {np.std(scores, ddof=1):.2f}")

