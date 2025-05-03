menu = {
    "1": ("Maggi", 89),
    "2": ("Pasta", 70),
    "3": ("Momo", 50),
    "4": ("Tea", 20),
    "5": ("Coffee", 100)
}

print("WELCOME TO OUR RESTAURANT")

totalbill = {"tb": 0, "name": ""}

def display_menu():
    print("\nMenu:")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ₹{price}")

def again():
    while True:
        print("\nDo you want to order more?")
        print("1. Order more")
        print("2. Get the bill")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_menu()
            item_no = input("Enter item number: ").strip()

            if item_no in menu:
                try:
                    qty = int(input("Enter quantity: "))
                    item, price = menu[item_no]
                    totalbill["tb"] += price * qty
                    print(f"{qty} {item}(s) added. Total so far: ₹{totalbill['tb']}")
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
                continue
            else:
                print("Invalid item number. Please try again.")
                continue

        elif choice == "2":
            print(f"\nCustomer Name: {totalbill['name']}")
            print(f"Your total bill is: ₹{totalbill['tb']}")
            print("Thanks for visiting!")
            break

        else:
            print("Invalid input, please enter 1 or 2.")

def order():
    totalbill["name"] = input("Enter your name: ").strip()
    display_menu()

    while True:
        item_no = input("Enter item number: ").strip()

        if item_no in menu:
            try:
                qty = int(input("Enter quantity: "))
                item, price = menu[item_no]
                totalbill["tb"] += price * qty
                print(f"{qty} {item}(s) added. Total so far: ₹{totalbill['tb']}")
                again()
                break
            except ValueError:
                print("Invalid quantity! Please enter a number.")
        else:
            print("Invalid item number. Please try again.")

order()





