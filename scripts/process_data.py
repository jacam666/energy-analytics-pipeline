import pandas as pd

# Load the CSV file
df = pd.read_csv("data/energy_transactions_2024_2026.csv")

print("Original data preview:")
print(df.head())

# Clean column names (remove spaces, make lowercase)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# Create transaction category (Charge or Payment)
def classify_transaction(amount):
    if amount < 0:
        return "Charge"
    else:
        return "Payment"

df["transaction_category"] = df["amount"].apply(classify_transaction)


# Convert date column to proper datetime format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Extract month (useful for analysis later)
df["month"] = df["date"].dt.to_period("M")


# Save cleaned data to a new file
df.to_csv("data/processed_energy.csv", index=False)

print("Processed file saved successfully!")

charges_summary = df.groupby("transaction_category")["amount"].sum().reset_index()

print("\nCharges vs Payments:")
print(charges_summary)

monthly_summary = df.groupby("month")["amount"].sum().reset_index()

print("\nMonthly totals:")
print(monthly_summary)

energy_summary = df.groupby("fueltype")["amount"].sum().reset_index()

print("\nEnergy type totals:")
print(energy_summary)


charges_summary.to_csv("data/charges_summary.csv", index=False)
monthly_summary.to_csv("data/monthly_summary.csv", index=False)
energy_summary.to_csv("data/energy_summary.csv", index=False)

print("\nSummary files saved!")