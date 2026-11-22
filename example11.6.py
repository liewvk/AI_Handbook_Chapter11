import pandas as pd

students = pd.DataFrame({
    "name": ["Aisha", "Ben", "Chen", "Devi"],
    "study_hours": [2, 4, 6, 8],
    "score": [50, 62, 76, 88]
})

print(students.to_string(index=False))
print("Average score:", students["score"].mean())
print("Rows and columns:", students.shape)

