
import numpy as np

features = np.array([[2., 50.],
                     [4., 62.],
                     [6., 76.]])
scale = np.array([1.0, 0.1])
scaled = features * scale
print(scaled)
