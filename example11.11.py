import pandas as pd

items = pd.DataFrame({
    "type": ["Book", "Pen", "Book"],
    "price": [20, 3, 25]
})
encoded = pd.get_dummies(items, columns=["type"], dtype=int)
print(encoded.to_string(index=False))

