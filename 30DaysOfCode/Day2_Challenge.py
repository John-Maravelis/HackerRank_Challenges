"""
Task: 
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer.
"""


def solve(meal_cost, tip_percent, tax_percent):
	print(round(meal_cost + tip_percent/100 * meal_cost + tax_percent/100 * meal_cost))

# This is needed for the program to pass the automated tests on HackerRank
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)


