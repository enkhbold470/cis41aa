# Author: Inky Ganbold
# CIS41A
# Final part1
# Team: Python Enjoyers
# Main Order class with CRUD operations and bill management

"""
Order module containing the main Order class.
Handles menu display, order management, calculations, and file operations.
Implements CRUD operations for order management.
"""

import time
import datetime
from food_items import DeAnzaBurger, BaconCheese, MushroomSwiss, WesternBurger, DonCaliBurger
from person import Person, Student, Staff


class Order:
    """
    Main Order class for managing food court orders.
    Implements CRUD operations and handles all order-related functionality.
    """
    
    def __init__(self):
        """
        Initialize an Order object with menu items and empty order.
        """
        # Initialize burger objects for menu
        self._burgers = {
            1: DeAnzaBurger(),
            2: BaconCheese(),
            3: MushroomSwiss(),
            4: WesternBurger(),
            5: DonCaliBurger()
        }
        
        # Price dictionary for easy access
        self._price_dict = {}
        for key, burger in self._burgers.items():
            self._price_dict[burger.get_name()] = burger.get_price()
        
        # Order dictionary to track quantities
        self._order_dict = {}
        for burger in self._burgers.values():
            self._order_dict[burger.get_name()] = 0
        
        # Order totals
        self._price_before_tax = 0.0
        self._price_after_tax = 0.0
        self._tax = 0.0
        self._customer = None
    
    def display_menu(self):
        """
        Display the food court menu with prices.
        """
        print("\n----------- De Anza Food Court -----------")
        number = 1
        for key, burger in self._burgers.items():
            print(f"{number}. {burger.get_name():15s} ${burger.get_price():8.2f}")
            number += 1
        print("6. Exit")
    
    def get_inputs(self):
        """
        Get order inputs from user and fill the order dictionary.
        Implements input validation and error handling.
        """
        print("\nEnter your order (select items 1-5, or 6 to finish):")
        
        while True:
            try:
                choice = input("\nSelect item (1-6): ").strip()
                choice_num = int(choice)
                
                if choice_num == 6:
                    break
                elif choice_num in self._burgers:
                    burger = self._burgers[choice_num]
                    while True:
                        try:
                            qty = input(f"Quantity for {burger.get_name()}: ").strip()
                            qty_num = int(qty)
                            if qty_num > 0:
                                self._order_dict[burger.get_name()] += qty_num
                                print(f"Added {qty_num} {burger.get_name()}(s) to order")
                                break
                            else:
                                print("Please enter a positive number")
                        except ValueError:
                            print("Please enter a valid number")
                else:
                    print("Please select a valid menu item (1-6)")
            except ValueError:
                print("Please enter a valid number (1-6)")
        
        # Get customer type for tax calculation
        self._get_customer_type()
    
    def _get_customer_type(self):
        """
        Private method to get customer type for tax calculation.
        """
        while True:
            customer_type = input("\nAre you a student or staff member? (student/staff): ").strip().lower()
            if customer_type == "student":
                self._customer = Student()
                break
            elif customer_type == "staff":
                self._customer = Staff()
                break
            else:
                print("Please enter 'student' or 'staff'")
    
    def calculate(self):
        """
        Calculate the price before tax, tax amount, and total price.
        """
        self._price_before_tax = 0.0
        for item_name, quantity in self._order_dict.items():
            self._price_before_tax += quantity * self._price_dict[item_name]
        
        self._tax = self._customer.calculate_tax(self._price_before_tax)
        self._price_after_tax = self._price_before_tax + self._tax
    
    def print_bill(self):
        """
        Print the bill on the console with formatted output.
        """
        if self._price_before_tax == 0:
            print("\nNo items ordered. Thank you for visiting!")
            return
        
        print("\n" + "="*50)
        print("YOUR BILL")
        print("="*50)
        print(f"Customer Type: {self._customer.get_person_type()}")
        print("-"*50)
        
        for item_name, quantity in self._order_dict.items():
            if quantity > 0:
                item_total = quantity * self._price_dict[item_name]
                print(f" {item_name:20s} Qty: {quantity:<10d} Price: ${self._price_dict[item_name]:<10.2f} Total: ${item_total:<10.2f}")
        
        print("-"*50)
        print(f"Price before tax: ${self._price_before_tax:.2f}")
        print(f"Tax ({self._customer.get_tax_rate()*100:.0f}%): ${self._tax:.2f}")
        print(f"Price after tax: ${self._price_after_tax:.2f}")
        print("="*50)
        print("Thank you for your order!")
    
    def save_to_file(self):
        """
        Save the bill to a timestamped file.
        """
        if self._price_before_tax == 0:
            return  # Don't save empty orders
        
        # Generate timestamp filename
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
        filename = order_time_stamp + '.txt'
        
        try:
            with open(filename, 'w') as file_handle:
                file_handle.write("De Anza Food Court - Order Receipt\n")
                file_handle.write("="*50 + "\n")
                file_handle.write(f"Order Date: {order_time_stamp}\n")
                file_handle.write(f"Customer Type: {self._customer.get_person_type()}\n")
                file_handle.write("-"*50 + "\n")
                
                for item_name, quantity in self._order_dict.items():
                    if quantity > 0:
                        item_total = quantity * self._price_dict[item_name]
                        file_handle.write(f" {item_name:20s} Qty: {quantity:<10d} Price: ${self._price_dict[item_name]:<10.2f} Total: ${item_total:<10.2f}\n")
                
                file_handle.write("-"*50 + "\n")
                file_handle.write(f"Price before tax: ${self._price_before_tax:.2f}\n")
                file_handle.write(f"Tax ({self._customer.get_tax_rate()*100:.0f}%): ${self._tax:.2f}\n")
                file_handle.write(f"Price after tax: ${self._price_after_tax:.2f}\n")
                file_handle.write("="*50 + "\n")
                file_handle.write("Thank you for your order!\n")
            
            print(f"\nReceipt saved to: {filename}")
        except Exception as e:
            print(f"Error saving receipt: {e}")
    
    # CRUD Operations
    def create_order_item(self, item_name, quantity):
        """
        Create/Add items to order (CRUD - Create).
        
        Args:
            item_name (str): Name of the item
            quantity (int): Quantity to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        if item_name in self._order_dict and quantity > 0:
            self._order_dict[item_name] += quantity
            print(f"Added {quantity} {item_name}(s) to order")
            return True
        return False
    
    def read_order(self):
        """
        Read/Display current order (CRUD - Read).
        """
        print("\nCurrent Order:")
        print("-"*30)
        has_items = False
        for item_name, quantity in self._order_dict.items():
            if quantity > 0:
                print(f"{item_name}: {quantity}")
                has_items = True
        if not has_items:
            print("No items in order")
    
    def update_order_item(self, item_name, new_quantity):
        """
        Update item quantity in order (CRUD - Update).
        
        Args:
            item_name (str): Name of the item
            new_quantity (int): New quantity
            
        Returns:
            bool: True if successful, False otherwise
        """
        if item_name in self._order_dict and new_quantity >= 0:
            old_quantity = self._order_dict[item_name]
            self._order_dict[item_name] = new_quantity
            print(f"Updated {item_name} quantity from {old_quantity} to {new_quantity}")
            return True
        return False
    
    def delete_order_item(self, item_name):
        """
        Delete item from order (CRUD - Delete).
        
        Args:
            item_name (str): Name of the item to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        if item_name in self._order_dict and self._order_dict[item_name] > 0:
            self._order_dict[item_name] = 0
            print(f"Removed {item_name} from order")
            return True
        return False
    
    def get_menu_items(self):
        """
        Get list of available menu items.
        
        Returns:
            list: List of menu item names
        """
        return list(self._price_dict.keys())
    
    def get_order_total(self):
        """
        Get the current order total.
        
        Returns:
            float: Total price after tax
        """
        return self._price_after_tax 