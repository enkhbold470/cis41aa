# Author: Inky Ganbold
# CIS41A
# Final part1
# Team: Python Enjoyers
# Food item classes with inheritance for different burger types

"""
Food items module containing Burger superclass and specific burger subclasses.
Each burger type has its own price and name overrides.
"""


class Burger:
    """
    Superclass for all burger types.
    Provides base functionality for burger items.
    """
    
    def __init__(self, name="Basic Burger", price=5.00):
        """
        Initialize a Burger object.
        
        Args:
            name (str): The burger name
            price (float): The burger price
        """
        self._name = name
        self._price = price
    
    def get_name(self):
        """
        Get the burger name.
        
        Returns:
            str: The burger name
        """
        return self._name
    
    def get_price(self):
        """
        Get the burger price.
        
        Returns:
            float: The burger price
        """
        return self._price
    
    def set_price(self, price):
        """
        Set the burger price.
        
        Args:
            price (float): The new price
        """
        if price > 0:
            self._price = price
    
    def calculate_total(self, quantity):
        """
        Calculate total price for given quantity.
        
        Args:
            quantity (int): Number of burgers
            
        Returns:
            float: Total price
        """
        return self._price * quantity
    
    def __str__(self):
        """
        String representation of the burger.
        
        Returns:
            str: Formatted burger info
        """
        return f"{self._name} - ${self._price:.2f}"


class DeAnzaBurger(Burger):
    """
    De Anza Burger subclass with specific price.
    """
    
    def __init__(self):
        """Initialize De Anza Burger with specific name and price."""
        super().__init__("De Anza Burger", 5.25)


class BaconCheese(Burger):
    """
    Bacon Cheese Burger subclass with specific price.
    """
    
    def __init__(self):
        """Initialize Bacon Cheese Burger with specific name and price."""
        super().__init__("Bacon Cheese", 5.75)


class MushroomSwiss(Burger):
    """
    Mushroom Swiss Burger subclass with specific price.
    """
    
    def __init__(self):
        """Initialize Mushroom Swiss Burger with specific name and price."""
        super().__init__("Mushroom Swiss", 5.95)


class WesternBurger(Burger):
    """
    Western Burger subclass with specific price.
    """
    
    def __init__(self):
        """Initialize Western Burger with specific name and price."""
        super().__init__("Western Burger", 5.95)


class DonCaliBurger(Burger):
    """
    Don Cali Burger subclass with specific price.
    """
    
    def __init__(self):
        """Initialize Don Cali Burger with specific name and price."""
        super().__init__("Don Cali Burger", 5.95) 