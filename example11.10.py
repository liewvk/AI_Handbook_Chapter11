import pandas as pd

orders = pd.DataFrame({
    "product": ["Book", "Pen", "Bag"],
    "quantity": [3, 10, 2],
    "unit_price": [20.0, 2.5, 45.0]
})
orders["revenue"] = (
    orders["quantity"] * orders["unit_price"]
)
print(orders.to_string(index=False))
print("Total revenue:", orders["revenue"].sum())

