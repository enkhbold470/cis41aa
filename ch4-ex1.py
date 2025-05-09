

# %%
# Inky Ganbold
# CIS41A
# Chapter 4 Exercise 1
# Team: Python Enjoyers
# This program calculates the gross pay for an employee, considering overtime pay (1.5 times the hourly rate for hours worked above 40).
# Also handles error

# %%

user_input = input("Please enter your email: ") # gets input 

pos1 = user_input.find("@") # get @ index
pos2 = user_input.find(".") # get . index
if pos1 != -1 or pos2 != -1: # checks if it is valid input, if it is not valid pos1 or pos1 became -1
    print("valid")           # tell it is valid email   
    print(user_input[pos1+1:pos2]) # print the domain name
else:
    print("invalid")        # print the invalid

# %%
"""
input: inky
output: invalid


input: inky@enk.icu
output: valid
output: enk

"""


