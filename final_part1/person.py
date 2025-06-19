# Author: Inky Ganbold
# CIS41A
# Final part1
# Team: Python Enjoyers
# Person classes with inheritance for tax calculation

"""
Person module containing Person superclass and Student/Staff subclasses.
Handles different tax rates for different types of customers.
"""


class Person:
    """
    Superclass for all person types.
    Provides base functionality for tax calculation.
    """
    
    def __init__(self, name="Customer"):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
        """
        self._name = name
        self._tax_rate = 0.09  # Default 9% tax rate
    
    def get_name(self):
        """
        Get the person's name.
        
        Returns:
            str: The person's name
        """
        return self._name
    
    def set_name(self, name):
        """
        Set the person's name.
        
        Args:
            name (str): The new name
        """
        self._name = name.strip()
    
    def calculate_tax(self, subtotal):
        """
        Calculate tax based on subtotal.
        
        Args:
            subtotal (float): The subtotal amount
            
        Returns:
            float: The tax amount
        """
        return subtotal * self._tax_rate
    
    def get_tax_rate(self):
        """
        Get the current tax rate.
        
        Returns:
            float: The tax rate as a decimal
        """
        return self._tax_rate
    
    def get_person_type(self):
        """
        Get the type of person.
        
        Returns:
            str: The person type
        """
        return "General Customer"


class Student(Person):
    """
    Student subclass with no tax (overrides tax calculation).
    """
    
    def __init__(self, name="Student"):
        """
        Initialize a Student object.
        
        Args:
            name (str): The student's name
        """
        super().__init__(name)
        self._tax_rate = 0.0  # Students pay no tax
    
    def calculate_tax(self, subtotal):
        """
        Override: Students pay no tax.
        
        Args:
            subtotal (float): The subtotal amount
            
        Returns:
            float: Always 0.0 for students
        """
        return 0.0
    
    def get_person_type(self):
        """
        Get the type of person.
        
        Returns:
            str: "Student"
        """
        return "Student"


class Staff(Person):
    """
    Staff subclass with standard tax rate.
    """
    
    def __init__(self, name="Staff"):
        """
        Initialize a Staff object.
        
        Args:
            name (str): The staff member's name
        """
        super().__init__(name)
        self._tax_rate = 0.09  # Standard 9% tax rate
    
    def get_person_type(self):
        """
        Get the type of person.
        
        Returns:
            str: "Staff"
        """
        return "Staff" 