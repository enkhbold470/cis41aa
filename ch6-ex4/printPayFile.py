# Author: Inky Ganbold
# CIS41A
# Chapter 6 Exercise 4
# Team: Python Enjoyers
# This module prints a formatted pay stub with all pay details.

def printPay(theDict):
    """
    Function to print a formatted pay stub with all pay details
    """
    print("\n" + "="*50)
    print("                   PAY STUB")
    print("="*50)
    print(f"Company: {theDict['company_name']}")
    print("-"*50)
    print(f"Hourly Rate:        ${theDict['rate']:.2f}")
    print(f"Regular Hours:      {theDict['regular_hours']:.1f}")
    print(f"Regular Pay:        ${theDict['regular_pay']:.2f}")
    
    if theDict['overtime_hours'] > 0:
        print(f"Overtime Hours:     {theDict['overtime_hours']:.1f}")
        print(f"Overtime Rate:      ${theDict['overtime_rate']:.2f}")
        print(f"Overtime Pay:       ${theDict['overtime_pay']:.2f}")
    
    print("-"*50)
    print(f"Total Hours:        {theDict['hours']:.1f}")
    print(f"TOTAL PAY:          ${theDict['total_pay']:.2f}")
    print("="*50) 