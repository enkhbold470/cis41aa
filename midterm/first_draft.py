items = {
    "De Anza Burger" :5.25,
    "Bacon Cheese " : 5.25,
    "Mushroom Swiss" :5.95,
    "Western Burger" : 5.95,
    "Done Cali Burger":5.95}

quantities = {
    "De Anza Burger" :0,
    "Bacon Cheese " : 0,
    "Mushroom Swiss" :0,
    "Western Burger" : 0,
    "Done Cali Burger":0
}

def show_menu():
    for key in items:
        print(key, "\t", items[key])

def gets_input():
    user_choice = int(input("what do you want?"))
    quantity = int(input("How many"))
    return user_choice, quantity

# def compute_bill(user_input):
#     quantities["De Anza Burger"] = user_input
#     return quantities

def main():
     show_menu()
     gets_input()
    #  value = gets_input()
    #  computed = compute_bill(value)
    #  print(computed)
     
     
    #  print(compute_bill(gets_input))
    
     
 

  
if __name__ == "__main__":
    main()

