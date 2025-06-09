import pandas as pd

# Load delivery data
deliveries = pd.read_csv('../data/deliveries_raw.csv')

# Show the first few rows
print("=== Deliveries Sample ===")
print(deliveries.head())

# Load customer feedback
feedback = pd.read_csv('../data/customer_feedback.csv')

print("\n=== Customer Feedback Sample ===")
print(feedback.head())
