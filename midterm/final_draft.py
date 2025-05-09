# Inky Ganbold - CIS 41 Midterm
# Team: Python Enjoyers
# De Anza Food Court Ordering Program
# Uses menu, inputs, billing & receipt flow based on diagram

# menu stored as a dict

menu_items = {
    1: ("De Anza Burger", 5.25),
    2: ("Bacon Cheese ",  5.25),
    3: ("Mushroom Swiss", 5.95),
    4: ("Western Burger", 5.95),
    5: ("Done Cali Burger",5.95)
    }

def show_menu():
    """Show the food options"""
    print(" de anza food court menu:")
    for num, (item, price) in menu_items.items():
        print(f"{num}. {item.lower()} - ${price}")
    print("6. exit")

def get_inputs():
    """Take user orders + ask for role (student/staff)"""
    orders = {k: 0 for k in menu_items}
    # role = ""
    while True:
        try:
            choice = int(input("\npick 1-5 or 6 to quit: "))
            if choice == 6:
                break
            if choice in menu_items:
                qty = int(input("qty? "))
                if qty > 0:
                    orders[choice] += qty
                else:
                    print("only + numbers pls")
            else:
                print("not on menu ")
            
        except:
            print("just type numbers thx") 
            
    return orders


def compute_bill(orders, role):
    #Calc totals
    # role = ""
    # if orders != None:
    #     while role not in ["student", "staff"]:
    #         role = input("u student or staff? ").lower()
    # else: 
    #     print("shit.. not workign")    
    sub = 0
    for num, qty in orders.items():
        sub += menu_items[num][1] * qty
    if role == "student":
        tax = 0
    else:
        tax = sub * 0.09  # integer math for 9% tax
    total = sub + tax
    return sub, tax, total

def print_bill(orders, sub, tax, total):
    
    if total != 0: # checks if the bill is 0 or not
    #print receipt
        print("\n receipt:")
        for num, qty in orders.items():
            if qty > 0:
                name, price = menu_items[num]
                print(f"{name.lower()} x{qty} = ${qty * price}")
        print(f"subtotal: ${sub:.2f}")
        print(f"tax: ${tax:.2f}")
        print(f"total: ${total:.2f}")
        print("Thank you, hope to see you again!")




def main():
    show_menu()
    role = ""
    orders = get_inputs()
    if sum(orders.values()) == 0:
        print("Thank you, hope to see you again!")
    else:
        while role not in ["student", "staff"]:
            role = input("u student or staff? ").lower()   
    
    sub, tax, total = compute_bill(orders, role)
    
    #test
    # get_inputs()
    # show_menu()
    # print(orders)
    print_bill(orders, sub, tax, total)

if __name__ == "__main__":
    main()

"""
Sample Run 1: 
(cis41aa) ➜  cis41aa /Users/inky/cis41aa/.venv/bin/python /Users/inky/cis41aa/midterm/final_draft.py 
 de anza food court menu:
1. de anza burger - $5.25
2. bacon cheese  - $5.25
3. mushroom swiss - $5.95
4. western burger - $5.95
5. done cali burger - $5.95
6. exit

pick 1-5 or 6 to quit: 6
Thank you, hope to see you again!

Sample Run 2:


(cis41aa) ➜  cis41aa /Users/inky/cis41aa/.venv/bin/python /Users/inky/cis41aa/midterm/final_draft.py 
 de anza food court menu:
1. de anza burger - $5.25
2. bacon cheese  - $5.25
3. mushroom swiss - $5.95
4. western burger - $5.95
5. done cali burger - $5.95
6. exit

pick 1-5 or 6 to quit: 2
qty? 2

pick 1-5 or 6 to quit: 6
u student or staff? staff

 receipt:
bacon cheese  x2 = $10.5
subtotal: $10.50
tax: $0.94
total: $11.45
Thank you, hope to see you again!
"""
