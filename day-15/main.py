'''
Date: 2024-01-16 20:03:13
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-16 20:56:10
FilePath: \100days-of-python\day-15\main.py
'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource(water,milk,coffee):
    if resources['water'] < water:
        print("Sorry, there is not enought water!")
        return False
    if resources['milk'] < milk:
        print("Sorry, there is not enough milk!")
        return False 
    if resources["coffee"] < coffee:
        print("Sorry, there is not enought coffee!")
        return False
    return True

def process_coins():
    """quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01,return $"""
    quarters = int(input("How many quaters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    return 0.25 * quarters + dimes * 0.1 + nickles + 0.05 + pennies * 0.01

def print_report(money):
    """"pass in the money, and print the report"""
    print(f"Water:{resources['water']}ml\nMilk:${resources['milk']}ml\nCoffee:${resources['coffee']}ml\nMoney:${money}")

def make_coffee(user_input):
    if user_input in MENU:
        coffee = MENU[user_input]
        ingredients = coffee.ingredients
        cost = coffee.cost
        resources_flag = check_resource(water=ingredients.water,milk=ingredients.milk,coffee=ingredients.coffee)
        if not resources_flag:
            return False
        else:
            user_moneny = process_coins()
            if user_moneny > cost:
                change_money = user_moneny - cost
                print(f'Here is your {user_input}, and some change ${change_money}')
                return True
            else:
                print("Sorry! You don't enter enough coins, money refunded!")
                return False
    else:
        print("Sorry,We don't have that.")
    return True

is_on = True
money = 0
while is_on:
    user_input = input('What would you like? (espresso/latte/cappuccino):')
    if user_input == 'off':
        print("Good Bye!")
        is_on = False
    elif user_input == 'report':
        print_report(money=money)
    else:
        is_on = make_coffee(user_input)
        