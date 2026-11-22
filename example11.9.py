import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 103],
    "amount": ["12.50", "19.00", "bad", "bad"]
})

orders["amount"] = pd.to_numeric(
    orders["amount"], errors="coerce"
)
print("Duplicate IDs:",
      orders["order_id"].duplicated().sum())
print("Invalid amounts:", orders["amount"].isna().sum())
print(orders.to_string(index=False))

