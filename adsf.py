# %% [markdown]
# Rewrite your pay computation program and use the following functions (get_input, compute_pay, print_output)
# 
# Don't forget to calculate overtime.
# 
# Enter Hours: 45
# 
# Enter Rate: 10
# 
# Pay: 475.0
# 
#  
# 
# YOU NEED THREE FUNCTIONS:
# the_hours, the_rate = get_input()
# 
# the_pay = compute_pay(the_hours, the_rate)
# 
# print_output(the_pay)
# 
#  
# 
# Call the functions and pass the arguments in the "main" function.
# 
# Example:
# 
# def main():
# 
#      the_hours, the_rate = get_input()
# 
#      the_pay = compute_pay(the_hours, the_rate)
# 
#      print_output(the_pay)
# 
#  
# 
# main()
# 
#  
# 
#  
# 
# Submit your code here.
# 
# 

# %%
# Inky Ganbold
# CIS41A
# Chapter 5 Exercise 1


# %%
def print_out(a):
    print({a})
print_out("hi")

# %%
def compute_pay(hours, rate):
    hours = hours * rate
    return hours
compute_pay(123,123)

# %%
def get_input():
    the_hours = int(input("Enter your hours you're working for…'"))
    the_rate = int(input("Enter your rate you work for by dollar, of course'"))
    return the_hours, the_rate

# %%

def main():
    the_hours, the_rate = get_input()
    the_pay = compute_pay(the_hours, the_rate)
    print_out(the_pay)
main()



