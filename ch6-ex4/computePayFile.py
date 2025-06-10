# Author: Inky Ganbold
# CIS41A
# Chapter 6 Exercise 4
# Team: Python Enjoyers
# This module computes pay with overtime calculations

def computePay(theDict):
    """
    Function to compute pay including overtime
    If hours > 40, overtime hours are paid at 1.5x the regular rate
    Updates and returns the dictionary with calculated values
    """
    rate = theDict["rate"]
    hours = theDict["hours"]
    
    if hours > 40:
        # Calculate regular and overtime pay
        regular_hours = 40
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        
        regular_pay = regular_hours * rate
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay
        
        # Add calculated values to dictionary
        theDict["regular_hours"] = regular_hours
        theDict["overtime_hours"] = overtime_hours
        theDict["overtime_rate"] = overtime_rate
        theDict["regular_pay"] = regular_pay
        theDict["overtime_pay"] = overtime_pay
        theDict["total_pay"] = total_pay
    else:
        # No overtime
        regular_hours = hours
        overtime_hours = 0
        overtime_rate = 0
        regular_pay = hours * rate
        overtime_pay = 0
        total_pay = regular_pay
        
        # Add calculated values to dictionary
        theDict["regular_hours"] = regular_hours
        theDict["overtime_hours"] = overtime_hours
        theDict["overtime_rate"] = overtime_rate
        theDict["regular_pay"] = regular_pay
        theDict["overtime_pay"] = overtime_pay
        theDict["total_pay"] = total_pay
    
    return theDict 