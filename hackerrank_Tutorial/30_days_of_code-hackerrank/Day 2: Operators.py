""" Task
Given the meal price (base cost of a meal),
tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal,

Find and print the meal's total cost. Round the result to the nearest integer.
Example
A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value and return from the function

Complete the 'solve' function below.

The function accepts following parameters:
 1. DOUBLE meal_cost
 2. INTEGER tip_percent
 3. INTEGER tax_percent
"""


def solve(meal_cost: float, tip_percent: int, tax_percent: int):
    tip_amount = (tip_percent * meal_cost)/100
    tax_amount = (tax_percent * meal_cost)/100
    total = round(meal_cost+tip_amount+tax_amount)
    print(f"\n{tip_percent}% Tip on {meal_cost} is: {tip_amount}")
    print(f"{tax_percent}% Tax on {meal_cost} is: {tax_amount}")
    print(f"Total bill amount is: {total}")


if __name__ == '__main__':
    meal_cost = float(input("Please enter meal cost: ").strip())
    tip_percent = int(input("Please enter tip percentage: ").strip())
    tax_percent = int(input("Please enter tax percentage: ").strip())
    solve(meal_cost, tip_percent, tax_percent)
