from colorama import init, Fore, Style

init()

class Restaurant:
    def __init__(self):
        self.menu = {
            'pizza': 60,
            'Pasta': 40,
            'Chowmein': 50,
            'Chicken wings': 80,
            'Spring rolls': 60,
            'Shawarma': 70,
            'Dynamite Chicken': 80,
            'Burger': 60,
            'salad': 70,
            'coffee': 80,
        }
        self.order_total = 0
    
    def show_menu(self):
        print(Fore.YELLOW + Style.BRIGHT + "Welcome to Tasty Bytes Restaurant" + Style.RESET_ALL)
        for item, price in self.menu.items():
            print(f"{item}: {price} Rs")
    
    def take_order(self):
        while True:
            item = input("Enter the item you want to order: ")
            if item in self.menu:
                self.order_total += self.menu[item]
                print(f"Your item {item} has been added to your order")
            else:
                print("Sorry, we don't have that item on the menu")
            
            another_order = input("Do you want to add another item? (yes/no): ")
            if another_order.lower() != 'yes':
                break
    
    def show_total(self):
        print(f"The total amount to pay is {self.order_total} Rs")

restaurant = Restaurant()
restaurant.show_menu()
restaurant.take_order()
restaurant.show_total()
