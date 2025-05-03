# List of friends' names
friends = ["Aditya", "Sneha", "Rohan", "Megha", "Kunal"]
name_lengths = [(name, len(name)) for name in friends] # tuples
print("Friends and Name Lengths")
for name, length in name_lengths:
    print(f"{name}: {length} characters")




# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nTotal Expenses")
print(f"Your total expenses: ₹{your_total}")
print(f"Partner's total expenses: ₹{partner_total}")

# Who spent more
if your_total > partner_total:
    print("You spent more overall.")
elif partner_total > your_total:
    print("Your partner spent more overall.")
else:
    print("Both spent the same amount.")

# Find the biggest difference in a category
max_diff = 0
category_with_max_diff = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        category_with_max_diff = category

print(f"\nBiggest spending difference is in '{category_with_max_diff}' with a difference of ₹{max_diff}")
