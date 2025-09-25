"""
Electricity Bill Estimator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# print("Electricity bill estimator 1.0")
# price_per_kwh = float(input("Price per kWh (cents): "))
# daily_use_kwh = float(input("Daily use in kWh: "))
# days_in_billing_period = int(input("Number of billing days: "))
#
# estimated_bill =  (price_per_kwh/100) * daily_use_kwh * days_in_billing_period
# print(f"Estimated_bill: ${estimated_bill:.2f}")

print("Electricity bill estimator 2.0")
tarrif = input("Which tarrif? (11 or 31): ")
daily_use_kWh = float(input("Daily use in kWh: "))
days_in_billing_period = int(input("Number of billing days: "))
if tarrif == '11':
    price_per_kwh = TARIFF_11
else:
    price_per_kwh = TARIFF_31
estimated_bill = price_per_kwh * daily_use_kWh * days_in_billing_period
print(f"Estimated_bill: ${estimated_bill:.2f}")
