import csv

monthly_data = {}

with open("data/energy_transactions_2024_2026.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        month = row["Month"]
        amount = float(row["Amount"])

        if month not in monthly_data:
            monthly_data[month] = {"charges": 0, "payments": 0}

        if amount < 0:
            monthly_data[month]["charges"] += amount
        else:
            monthly_data[month]["payments"] += amount

for month in sorted(monthly_data):
    values = monthly_data[month]
    print(month, 
          "Charges:", round(values["charges"], 2), 
          "Payments:", round(values["payments"], 2))
    
total_charges = sum(v["charges"] for v in monthly_data.values())
total_payments = sum(v["payments"] for v in monthly_data.values())

print("\nOverall Totals")
print("Charges:", round(total_charges, 2))
print("Payments:", round(total_payments, 2))

with open("monthly_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Charges", "Payments"])

    for month in sorted(monthly_data):
        values = monthly_data[month]
        writer.writerow([
            month,
            round(values["charges"], 2),
            round(values["payments"], 2)
        ])