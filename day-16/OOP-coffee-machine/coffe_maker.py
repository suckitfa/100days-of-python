'''
Date: 2024-01-20 12:00:21
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-28 12:52:32
FilePath: \100days-of-python\day-16\OOP-coffee-machine\coffe_maker.py
'''
class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water":300,
            "milk":200,
            "coffee":100,
        }
    
    def report(self):
        """Prints a report of all resources"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        
    def is_resource_sufficient(self,drink):
        """Returns True when order can be made,False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there isn't enough {item}")
                can_make = False
        return can_make

    def make_coffee(self,order):
        """Deducts the required ingredients from the resources and returns a report"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {  order.name }")