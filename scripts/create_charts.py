import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it does not already exist
os.makedirs("charts", exist_ok=True)

# Load summary files
monthly_summary = pd.read_csv("data/monthly_summary.csv")
charges_summary = pd.read_csv("data/charges_summary.csv")
energy_summary = pd.read_csv("data/energy_summary.csv")


# 1. Monthly totals chart
plt.figure(figsize=(10, 5))
plt.plot(monthly_summary["month"], monthly_summary["amount"], marker="o")
plt.title("Monthly Energy Transaction Totals")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_totals.png")
plt.close()


# 2. Charges vs Payments chart
plt.figure(figsize=(6, 4))
plt.bar(charges_summary["transaction_category"], charges_summary["amount"])
plt.title("Charges vs Payments")
plt.xlabel("Transaction Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("charts/charges_vs_payments.png")
plt.close()


# 3. Energy type totals chart
plt.figure(figsize=(6, 4))
plt.bar(energy_summary["fueltype"], energy_summary["amount"])
plt.title("Energy Type Totals")
plt.xlabel("Fuel Type")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("charts/energy_type_totals.png")
plt.close()

print("Charts created successfully!")