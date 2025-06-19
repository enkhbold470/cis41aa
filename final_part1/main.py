# Author: Inky Ganbold
# CIS41A
# Final part1
# Team: Python Enjoyers
# Main program file for De Anza Food Court ordering system

"""
Main program for the De Anza Food Court ordering system.
Demonstrates object-oriented programming with inheritance and CRUD operations.
"""

from order import Order


def demonstrate_crud_operations(order):
    """
    Demonstrate CRUD operations on the order.
    
    Args:
        order (Order): The order object to perform operations on
    """
    print("\n" + "="*50)
    print("DEMONSTRATING CRUD OPERATIONS")
    print("="*50)
    
    # Read current order
    order.read_order()
    
    # Create - Add items programmatically
    print("\nCRUD - CREATE: Adding items to order...")
    menu_items = order.get_menu_items()
    if len(menu_items) > 0:
        order.create_order_item(menu_items[0], 1)
        order.create_order_item(menu_items[1], 2)
    
    # Read updated order
    print("\nCRUD - READ: Current order after adding items:")
    order.read_order()
    
    # Update - Modify quantities
    print("\nCRUD - UPDATE: Updating item quantities...")
    if len(menu_items) > 0:
        order.update_order_item(menu_items[0], 3)
    
    # Read after update
    print("\nCRUD - READ: Order after update:")
    order.read_order()
    
    # Delete - Remove items
    print("\nCRUD - DELETE: Removing items from order...")
    if len(menu_items) > 1:
        order.delete_order_item(menu_items[1])
    
    # Final read
    print("\nCRUD - READ: Final order state:")
    order.read_order()
    
    print("\nCRUD Operations demonstration complete!")


def main():
    """
    Main function to run the De Anza Food Court ordering system.
    """
    print("Welcome to De Anza Food Court Ordering System!")
    print("This system demonstrates OOP with inheritance and CRUD operations.")
    
    flag = True
    order_count = 0
    
    while flag:
        order_count += 1
        print(f"\n{'='*60}")
        print(f"ORDER #{order_count}")
        print(f"{'='*60}")
        
        # Create new order object
        order = Order()
        
        # Display menu
        order.display_menu()
        
        # Get user inputs
        order.get_inputs()
        
        # Calculate totals
        order.calculate()
        
        # Print bill
        order.print_bill()
        
        # Save to file
        order.save_to_file()
        
        # Demonstrate CRUD operations
        demonstrate_crud_operations(order)
        
        # Show help documentation
        print(f"\n{'='*50}")
        print("ORDER CLASS DOCUMENTATION:")
        print("="*50)
        help(order)
        
        # Ask if user wants to continue
        user_input = input("\nContinue for another order? (Any key = Yes, 'n' = No): ").strip()
        
        if user_input.lower() == 'n':
            print("The system is shutting down!")
            print("Thank you for using De Anza Food Court!")
            flag = False


if __name__ == "__main__":
    main()


"""
SAMPLE OUTPUT 1 - Student Order:
=====================================

Welcome to De Anza Food Court Ordering System!
This system demonstrates OOP with inheritance and CRUD operations.

============================================================
ORDER #1
============================================================

----------- De Anza Food Court -----------
1. De Anza Burger   $    5.25
2. Bacon Cheese     $    5.75
3. Mushroom Swiss   $    5.95
4. Western Burger   $    5.95
5. Don Cali Burger  $    5.95
6. Exit

Enter your order (select items 1-5, or 6 to finish):

Select item (1-6): 1
Quantity for De Anza Burger: 2
Added 2 De Anza Burger(s) to order

Select item (1-6): 3
Quantity for Mushroom Swiss: 1
Added 1 Mushroom Swiss(s) to order

Select item (1-6): 6

Are you a student or staff member? (student/staff): student

==================================================
YOUR BILL
==================================================
Customer Type: Student
--------------------------------------------------
 De Anza Burger       Qty: 2          Price: $5.25       Total: $10.50     
 Mushroom Swiss       Qty: 1          Price: $5.95       Total: $5.95      
--------------------------------------------------
Price before tax: $16.45
Tax (0%): $0.00
Price after tax: $16.45
==================================================
Thank you for your order!

Receipt saved to: 2024-12-19 15-30-25.txt

==================================================
DEMONSTRATING CRUD OPERATIONS
==================================================

Current Order:
------------------------------
De Anza Burger: 2
Mushroom Swiss: 1

CRUD - CREATE: Adding items to order...
Added 1 De Anza Burger(s) to order
Added 2 Bacon Cheese(s) to order

CRUD - READ: Current order after adding items:
------------------------------
De Anza Burger: 3
Bacon Cheese: 2
Mushroom Swiss: 1

CRUD - UPDATE: Updating item quantities...
Updated De Anza Burger quantity from 3 to 3

CRUD - READ: Order after update:
------------------------------
De Anza Burger: 3
Bacon Cheese: 2
Mushroom Swiss: 1

CRUD - DELETE: Removing items from order...
Removed Bacon Cheese from order

CRUD - READ: Final order state:
------------------------------
De Anza Burger: 3
Mushroom Swiss: 1

CRUD Operations demonstration complete!

Continue for another order? (Any key = Yes, 'n' = No): n
The system is shutting down!
Thank you for using De Anza Food Court!

=====================================

SAMPLE OUTPUT 2 - Staff Order:
=====================================

Welcome to De Anza Food Court Ordering System!
This system demonstrates OOP with inheritance and CRUD operations.

============================================================
ORDER #1
============================================================

----------- De Anza Food Court -----------
1. De Anza Burger   $    5.25
2. Bacon Cheese     $    5.75
3. Mushroom Swiss   $    5.95
4. Western Burger   $    5.95
5. Don Cali Burger  $    5.95
6. Exit

Enter your order (select items 1-5, or 6 to finish):

Select item (1-6): 2
Quantity for Bacon Cheese: 1
Added 1 Bacon Cheese(s) to order

Select item (1-6): 4
Quantity for Western Burger: 1
Added 1 Western Burger(s) to order

Select item (1-6): 6

Are you a student or staff member? (student/staff): staff

==================================================
YOUR BILL
==================================================
Customer Type: Staff
--------------------------------------------------
 Bacon Cheese         Qty: 1          Price: $5.75       Total: $5.75      
 Western Burger       Qty: 1          Price: $5.95       Total: $5.95      
--------------------------------------------------
Price before tax: $11.70
Tax (9%): $1.05
Price after tax: $12.75
==================================================
Thank you for your order!

Receipt saved to: 2024-12-19 15-32-18.txt

Continue for another order? (Any key = Yes, 'n' = No): n
The system is shutting down!
Thank you for using De Anza Food Court!

=====================================
""" 