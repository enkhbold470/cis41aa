# De Anza Food Court Ordering System - Final Part 1

**Author:** Inky Ganbold  
**Course:** CIS41A  
**Team:** Python Enjoyers  

## Project Overview

This project is a complete rewrite of the midterm part 1 using object-oriented programming principles. It implements a food court ordering system for De Anza College with inheritance, CRUD operations, and proper code organization.

## Features

### Object-Oriented Design
- **Inheritance Hierarchy**: Superclasses (`Person`, `Burger`) with subclasses
- **Encapsulation**: Private variables with getter/setter methods
- **Polymorphism**: Method overriding in subclasses
- **Abstraction**: Clean interfaces for all classes

### CRUD Operations
- **Create**: Add items to order
- **Read**: Display current order
- **Update**: Modify item quantities
- **Delete**: Remove items from order

### Additional Features
- Tax calculation based on customer type (Student: 0%, Staff: 9%)
- Timestamped receipt files
- Input validation and error handling
- Comprehensive unit testing
- PEP 8 compliant code style

## File Structure

```
final_part1/
├── person.py           # Person superclass and Student/Staff subclasses
├── food_items.py       # Burger superclass and burger type subclasses
├── order.py            # Main Order class with CRUD operations
├── main.py             # Main program runner
├── test_order_system.py # Unit tests for all classes
├── README.md           # This documentation file
└── *.txt              # Generated receipt files (timestamped)
```

## Class Hierarchy

### Person Classes (person.py)
- `Person` (Superclass)
  - `Student` (Subclass - 0% tax)
  - `Staff` (Subclass - 9% tax)

### Food Item Classes (food_items.py)
- `Burger` (Superclass)
  - `DeAnzaBurger` ($5.25)
  - `BaconCheese` ($5.75)
  - `MushroomSwiss` ($5.95)
  - `WesternBurger` ($5.95)
  - `DonCaliBurger` ($5.95)

### Order Management (order.py)
- `Order` class with comprehensive order management
- CRUD operations for order items
- File I/O for receipt generation
- Tax calculation integration

## How to Run

### Main Program
```bash
cd final_part1
python main.py
```

### Unit Tests
```bash
cd final_part1
python test_order_system.py
```

## Usage Instructions

1. **Menu Display**: The system shows available burger options with prices
2. **Order Selection**: Choose items by number (1-5) and specify quantities
3. **Customer Type**: Identify as student (no tax) or staff (9% tax)
4. **Bill Generation**: View formatted bill and save to timestamped file
5. **CRUD Demo**: System demonstrates Create, Read, Update, Delete operations

## Sample Interactions

### Student Order Example
```
Select item (1-6): 1
Quantity for De Anza Burger: 2
Select item (1-6): 6
Are you a student or staff member? student

YOUR BILL
Customer Type: Student
De Anza Burger    Qty: 2    Price: $5.25    Total: $10.50
Price before tax: $10.50
Tax (0%): $0.00
Price after tax: $10.50
```

### Staff Order Example
```
Select item (1-6): 2
Quantity for Bacon Cheese: 1
Select item (1-6): 6
Are you a student or staff member? staff

YOUR BILL
Customer Type: Staff
Bacon Cheese      Qty: 1    Price: $5.75    Total: $5.75
Price before tax: $5.75
Tax (9%): $0.52
Price after tax: $6.27
```

## Technical Implementation

### Design Patterns Used
- **Template Method Pattern**: Base classes define structure, subclasses provide specifics
- **Factory Pattern**: Order class creates appropriate Person and Burger objects
- **Strategy Pattern**: Different tax calculation strategies for different person types

### Data Structures
- **Dictionaries**: Used for menu items, prices, and order tracking
- **Objects**: Encapsulate related data and behavior
- **Lists**: Menu item management and iteration

### Error Handling
- Input validation for menu selections
- Quantity validation (positive numbers only)
- File I/O error handling
- Graceful handling of invalid operations

### Testing Strategy
- **Unit Tests**: Individual class and method testing
- **Integration Tests**: Complete workflow testing
- **Edge Cases**: Invalid inputs and boundary conditions
- **Mock Data**: Controlled test scenarios

## File Output

Receipt files are automatically generated with timestamps:
- Format: `YYYY-MM-DD HH-MM-SS.txt`
- Location: Same directory as program
- Content: Complete order details and totals

## Code Quality

- **PEP 8 Compliance**: Proper naming, spacing, and structure
- **Documentation**: Comprehensive docstrings for all classes and methods
- **Type Safety**: Proper parameter validation
- **Maintainability**: Modular design with clear separation of concerns

## UML Class Diagram

The project includes a UML class diagram showing the inheritance relationships and class structure. The diagram illustrates:
- Inheritance relationships between superclasses and subclasses
- Method overriding in subclasses
- Composition relationships between Order and other classes
- Private attributes and public methods

## Questions and Answers

### Why use "_" before variable names?
The underscore prefix indicates private variables in Python, implementing encapsulation principles.

### OOP vs Functional Programming?
OOP organizes code around objects and classes, while functional programming focuses on functions and data transformations.

### What is "self"?
"self" refers to the current instance of a class, allowing access to instance variables and methods.

### Dictionaries vs Lists/Tuples?
Dictionaries provide key-value mapping for fast lookups, while lists are ordered sequences and tuples are immutable sequences.

### Why use dictionaries here?
Dictionaries efficiently map menu items to prices and track order quantities with item names as keys.

### What is encapsulation?
Encapsulation hides internal implementation details and controls access to data through public methods.

## Future Enhancements

- Database integration for persistent storage
- Web interface for remote ordering
- Payment processing integration
- Inventory management system
- Customer loyalty program
- Multi-location support 