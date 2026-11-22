from pathlib import Path
import pandas as pd

path = Path("clean_students.csv")
source = pd.DataFrame({
    "hours": [2, 4, 6],
    "score": [50, 62, 76]
})
source.to_csv(path, index=False)
loaded = pd.read_csv(path)

print("Saved:", path.name)
print(loaded.to_string(index=False))

