# Author: Inky Ganbold
# CIS41A
# Chapter 6 Exercise 4
# Team: Python Enjoyers
# This program validates company names, calculates pay with overtime, and prints a formatted pay stub

from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

def payProcess():
    '''
    This function is to process all other functions to get inputs,
    calculate and print the pay stub
    '''
    theDict = getInputs()
    theDict = computePay(theDict)
    printPay(theDict)

if __name__ == '__main__':
    payProcess()

"""
Sample Output 1:
================
Enter your company name: Microsoft
Invalid company name. Attempt 1 of 2.
Enter your company name: InvalidCompany
Invalid company name. Attempt 2 of 2.

Available companies in database:
- Amazon
- Apple
- Facebook
- Google
- Uber

Enter your company name: Google
Enter your hourly rate: $25.50
Enter hours worked: 45

==================================================
                   PAY STUB
==================================================
Company: Google
--------------------------------------------------
Hourly Rate:        $25.50
Regular Hours:      40.0
Regular Pay:        $1020.00
Overtime Hours:     5.0
Overtime Rate:      $38.25
Overtime Pay:       $191.25
--------------------------------------------------
Total Hours:        45.0
TOTAL PAY:          $1211.25
==================================================

Sample Output 2:
================
Enter your company name: apple
Enter your hourly rate: $30.00
Enter hours worked: 35

==================================================
                   PAY STUB
==================================================
Company: Apple
--------------------------------------------------
Hourly Rate:        $30.00
Regular Hours:      35.0
Regular Pay:        $1050.00
--------------------------------------------------
Total Hours:        35.0
TOTAL PAY:          $1050.00
==================================================
"""
