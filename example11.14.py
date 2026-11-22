import numpy as np
import pandas as pd

students = pd.DataFrame({
    "hours": [2., 4., np.nan, 8.],
    "practice": [1., 2., 3., 4.],
    "score": [50., 62., 76., 88.]
})

print("Missing values before cleaning:")
print(students.isna().sum().to_string())

students["hours"] = students["hours"].fillna(
    students["hours"].median()
)
X = students[["hours", "practice"]].to_numpy()
y = students["score"].to_numpy()

print("X shape:", X.shape)
print("y shape:", y.shape)
print("First feature row:", X[0].tolist())
print("Targets:", y.tolist())

