import csv
import datetime

class Pizza():
    def get_description(self):
        pass
    
    def get_cost(self):
        pass

class Classic(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 10.0
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 12.0
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class TurkishPizza(Pizza):
    def __init__(self):
        self.description = "Turkish Pizza"
        self.cost = 14.0
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza
    
    def get_description(self):
        return self.pizza.get_description()
    
    def get_cost(self):
        return self.pizza.get_cost()

class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Olive"
        self.cost = 2.0
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mushroom"
        self.cost = 1.5
    
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Goat Cheese"
        self.cost = 3.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Meat"
        self.cost = 4.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Onion"
        self.cost = 1.0

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Corn"
        self.cost = 3.5

    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.cost

def print_menu():
    with open("Menu.txt", "r") as f:
        menu_text = f.read()
        print(menu_text)

def order_save(name, id_number, card_number, card_password, order_number):
    
    date = datetime.datetime.now()
    orders = {}

    csv_columns = ['order_details', 'order_date', 'name', 'id_number', 'card_number', 'card_password']
    orders.update({
        order_number: {
            'order_details': 'This is ' + str(order_number) + '. order',
            'order_date': date,
            'name': name, 
            'id_number': id_number, 
            'card_number': card_number, 
            'card_password': card_password
        }
        })

    with open("Orders_Database.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
        writer.writeheader()
        writer.writerow(orders[order_number])

def main():
    system = int(input('Start(1/0): '))
    order_number = 0
    while system == 1:

        print_menu()

        pizza_choice = int(input("Please enter the what kind of pizza you would like: "))

        if pizza_choice == 1:
            pizza = Classic()

        elif pizza_choice == 2:
            pizza = Margherita()

        elif pizza_choice == 3:
            pizza = TurkishPizza()

        elif pizza_choice == 0:
            print("Call it a day! Have a nice rest")
            return
        
        else:
            print("Invalid pizza choice!")
            return

        sauce_choices = []
        while len(sauce_choices) < 3:
            sauce_choice = int(input("Please enter the number of sauce {} that you would like: ".format(len(sauce_choices)+1)))
            if sauce_choice in [11, 12, 13, 14, 15, 16]:
                sauce_choices.append(sauce_choice)
            else:
                print("Invalid sauce choice!")

        sauce_cost = 0
        s = []

        for sauce_choice in sauce_choices:
            if sauce_choice == 11:
                sauce = Olive(pizza)

            elif sauce_choice == 12:
                sauce = Mushroom(pizza)

            elif sauce_choice == 13:
                sauce = GoatCheese(pizza)

            elif sauce_choice == 14:
                sauce = Meat(pizza)

            elif sauce_choice == 15:
                sauce = Onion(pizza)

            elif sauce_choice == 16:
                sauce = Corn(pizza)

            sauce_cost += sauce.get_cost()
            s.append(sauce.get_description())
            
        print("You have ordered a {} with the following toppings:".format(pizza.get_description()))
        print(f"- {s}")
        
        p1 = Decorator(pizza)

        pay = input("And It will cost {} $.\nDo you want to confirm payment? (yes/no)\n".format(p1.get_cost()+sauce_cost))
        
        if pay == 'yes':
            order_number += 1
            uname = str(input('Name: ').split(' '))
            uid_number = int(input('ID Number: '))
            ucard_number = int(input('Card Number: '))
            ucard_password = int(input('Card Password: '))
            order_save(uname, uid_number, ucard_number, ucard_password)
            
        
        elif pay == 'no':
            print("Coming soon")

        else:
            print("Invalid choice!")

main()