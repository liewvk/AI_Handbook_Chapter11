import pandas as pd

students = pd.DataFrame({
    "name": ["Aisha", "Ben", "Chen", "Devi"],
    "hours": [2, 4, 6, 8],
    "score": [50, 62, 76, 88]
})

high_scores = students.loc[
    students["score"] >= 70, ["name", "score"]
]
print(high_scores.to_string(index=False))
print("First two hour values:",
      students.iloc[:2, 1].tolist())

