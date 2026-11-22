import pandas as pd

sales = pd.DataFrame({
    "item": ["A", "B", "C", "D"],
    "units": [10, None, 14, 12]
})

print("Missing units:", sales["units"].isna().sum())
median_units = sales["units"].median()
sales["units_filled"] = sales["units"].fillna(median_units)
print("Median:", median_units)
print(sales[["item", "units_filled"]].to_string(index=False))

