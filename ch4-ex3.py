# %%
# Inky Ganbold
# CIS41A
# Chapter 4 Exercise 3
# Team: Python Enjoyers
# This program calculates the sum of digits of an input number.
# It validates the input to ensure it's numeric and handles the calculation.

# %%

# Get user input
user_input = input("Please enter an integer number: ")

# Check if input is numeric
if user_input.isdigit():
    # Convert to integer
    number = int(user_input)
    
    # Initialize sum
    digit_sum = 0
    
    # Calculate sum of digits
    for digit in user_input:
        digit_sum += int(digit)
    
    # Print result
    print(f"The sum of digits in {number} is: {digit_sum}")
else:
    print("Invalid input. Please enter a valid integer number.")

# %%
"""
input: 1729
output: The sum of digits in 1729 is: 19

input: 12345
output: The sum of digits in 12345 is: 15
"""
