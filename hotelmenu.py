menu ={
    'Pizza': 160,
    'Pasta': 100,
    'Burger': 80,
    'Salad': 85,
    'Coffee': 55,
    'Tea': 45,
}

#Greet
print("Welcome to our Cafe")
print("Pizza: Rs160\nPasta: Rs100\nBurger: Rs80\nSalad: Rs85\nCoffee: Rs55\nTea: Rs45")

order_total=0

item_1 =input("Enter the name of the item you want to order ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Price: Rs{menu[item_1]}")
else:
    print("Sory, We don't have that item on our menu.")



# Loop repeatedly for additional items
while True:
    another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
    
    if another_order == "yes":
        item = input("Enter the name of the item you want to order: ")
        if item in menu:
            order_total += menu[item]
            print(f"{item} added to your order. Price: Rs{menu[item]}")
        else:
            print("Sorry, we don't have that item on our menu.")
    elif another_order == "no":
        break
    else:
        print("Invalid input. Please enter Yes or No.")

print(f"Your total order amount is: Rs{order_total}")