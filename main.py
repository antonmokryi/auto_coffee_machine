import time 
data = {
    "espresso": {
        "gramm": 20,
        "water": 15,
        "price": 20,
        "milk": 0
    },
    "americano": {
        "gramm": 20,
        "water": 100,
        "price": 20,
        "milk": 0

    },
    "capucino": {
        "gramm": 20,
        "water": 50,
        "price": 30,
        "milk": 100

    },
    "late": {
        "gramm": 20,
        "water": 50,
        "price": 35,
        "milk": 120

    },
    "flat white": {
        "gramm": 40,
        "water": 120,
        "price": 40,
        "milk": 80

    }
}
class auto_coffee_machine:
    def __init__(self):
        # скільки чого спочатку знаходиться в автоматі
        self.all_water = 500
        self.all_coffee = 500
        self.all_milk = 500
        self.__money = 0
    def buy_coffee(self, name_coffee):

        self.all_water -= data[name_coffee]["water"]
        self.all_milk -= data[name_coffee]["milk"]
        self.all_coffee -= data[name_coffee]["gramm"]
        self.__money += data[name_coffee]["price"]

        seconds = 15
        for second in range(seconds, 0, -1):
            print('Ваша кава буде готова через ' + str(second))
            time.sleep(0.1)
        if self.all_coffee < 300:
            print("Кавові зерна закінчуються")
        elif self.all_milk < 500:
            print("Закінчується молоко")
        elif self.all_water < 1000:
            print("Закінчується вода")
    def add_components(self, water, coffee, milk):
        self.all_water += water
        self.all_milk += milk
        self.all_coffee += coffee
    def action_with_money(self, add_money, put_out_money):
        print(self.__money)
        self.__money += add_money
        self.__money -= put_out_money



order = auto_coffee_machine()
# order.buy_coffee("espresso")
# order.buy_coffee("late")

