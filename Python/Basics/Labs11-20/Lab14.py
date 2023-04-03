income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if income < 85528:
    tax = ((18 * income) / 100) - 556.2
elif income > 85528:
    tax = 14839.2 + ((32 * (income - 85528)) / 100)

if tax <= 0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
