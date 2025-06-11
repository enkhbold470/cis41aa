# Author: Inky Ganbold
# CIS41A
# Chapter 6 Exercise 4
# Team: Python Enjoyers
# This module gets and validates user inputs for payroll processing

def getInputs():
    """
    Function to get and validate user inputs for company name, rate, and hours
    Returns a dictionary with validated inputs
    """
    # Company database list
    COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]
    
    # Get and validate company name
    company_name = getValidCompany(COMPANYLIST)
    
    # Get and validate rate
    rate = getValidRate()
    
    # Get and validate hours
    hours = getValidHours()
    
    # Return dictionary with all inputs
    return {"rate": rate, "hours": hours, "company_name": company_name}

def getValidCompany(companyList):
    """
    Get and validate company name from user input
    Shows company list after 2 invalid attempts
    """
    attempts = 0
    while True:
        company = input("Enter your company name: ").strip()
        
        # Check if company is in the list (case-insensitive)
        for valid_company in companyList:
            if company.lower() == valid_company.lower():
                return valid_company  # Return the properly capitalized version
        
        attempts += 1
        print(f"Invalid company name. Attempt {attempts} of 2.")
        
        if attempts >= 2:
            print("\nAvailable companies in database:")
            for company in companyList:
                print(f"- {company}")
            print()
        
        if attempts >= 3:
            print("Too many invalid attempts. Please select from the list above.")

def getValidRate():
    """
    Get and validate hourly rate (must be numeric and positive)
    """
    while True:
        try:
            rate = float(input("Enter your hourly rate: $"))
            if rate > 0:
                return rate
            else:
                print("Rate must be a positive number. Please try again.")
        except ValueError:
            print("Please enter a valid numeric value for rate.")

def getValidHours():
    """
    Get and validate hours worked (must be numeric and positive)
    """
    while True:
        try:
            hours = float(input("Enter hours worked: "))
            if hours > 0:
                return hours
            else:
                print("Hours must be a positive number. Please try again.")
        except ValueError:
            print("Please enter a valid numeric value for hours.") 