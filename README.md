🍽️ Restaurant Billing System

Welcome to the Restaurant Billing System! This Python-based program allows users to order food from a menu, calculate the total bill, and display customer details efficiently. 🍜

📌 Features

✅ Interactive Menu - Users can view and select items easily.
✅ Multiple Orders - Users can order multiple items and quantities.
✅ Error Handling - Handles invalid inputs gracefully.
✅ Customer Name Entry - Collects and displays the customer's name on the bill.
✅ Total Bill Calculation - Displays the final amount at the end.

📝 How It Works

1️⃣ The program welcomes the customer.
2️⃣ The user enters their name.
3️⃣ The menu is displayed in a numbered format.
4️⃣ The user selects an item number and enters the quantity.
5️⃣ The program calculates the total and asks if they want to order more or get the bill.
6️⃣ Once done, the total bill is displayed along with the customer's name.

📜 Menu (Example)

No.         Item        Price (₹)

1️⃣          Maggi        89

2️⃣          Pasta        70

3️⃣          Momo         50

4️⃣          Tea          20

5️⃣          Coffee       100

🛠️ Installation & Usage

1️⃣ Install Python (if not already installed).
2️⃣ Copy the code and save it as restaurant_billing.py.
3️⃣ Run the script using:

python restaurant_billing.py

4️⃣ Follow the on-screen instructions to place your order. 🍕

🖥️ Code Implementation

menu = {
    "1": ("Maggi", 89),
    "2": ("Pasta", 70),
    "3": ("Momo", 50),
    "4": ("Tea", 20),
    "5": ("Coffee", 100)
}

print(" WELCOME TO OUR RESTAURANT ")

totalbill = {"tb": 0, "name": "", "orders": []}  

def display_menu():
    
    print("\nMenu:")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ₹{price}")

def again():
   
    while True:
        print("\nWould you like to order more?")
        print("1️ Order more")
        print("2️ Get the bill")
        
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            take_order()
            break
        elif choice == "2":
            generate_bill()
            break
        else:
            print(" Invalid input! Please enter 1 or 2.")

def take_order():
   
    display_menu()
    
    while True:
        item_no = input("\nEnter item number: ").strip()
        
        if item_no in menu:
            try:
                qty = int(input("Enter quantity: "))
                item, price = menu[item_no]
                total_cost = price * qty
                totalbill["tb"] += total_cost
                totalbill["orders"].append((item, qty, total_cost))
                print(f"{qty} {item}(s) added. Total so far: ₹{totalbill['tb']}")
                again()
                break
            except ValueError:
                print("Invalid quantity! Please enter a number.")
        else:
            print("Invalid item number! Please try again.")

def generate_bill():
   
    print("\n----- BILL SUMMARY -----")
    print(f"Customer Name: {totalbill['name']}")
    print("\nOrdered Items:")
    for item, qty, cost in totalbill["orders"]:
        print(f"{qty}x {item} - ₹{cost}")
    
    print("\nTotal Bill: ₹", totalbill["tb"])
    print("Thanks for visiting! Have a great day!")
    print("---------------------------")

def order():
    """Initialize order process"""
    totalbill["name"] = input("\nEnter your name: ").strip().title()
    take_order()

order()

🖥️ Sample Output

WELCOME TO OUR RESTAURANT
Enter your name: Adarsh

Menu:
1. Maggi - ₹89
2. Pasta - ₹70
3. Momo - ₹50
4. Tea - ₹20
5. Coffee - ₹100

Enter item number: 1
Enter quantity: 2
2 Maggi(s) added. Total so far: ₹178

Do you want to order more?
1. Order more
2. Get the bill

Customer Name: Adarsh
Your total bill is: ₹178
Thanks for visiting!

🎯 Future Improvements

🔹 Add discount coupons.
🔹 Implement a GUI version using Tkinter.
🔹 Enable saving order history in a file.
🔹 Add GST & service charge calculations.

📌 Author

👨‍💻 Developed by Adarsh
📅 Date: March 2025

Enjoy your meal! 🍔🍟🥤

