import os
import sys
sys.path.append('/Users/raghvendra/Desktop/assignment/dunzo_assignment/vending_machine/coffee_machine')
import unittest
from inventory import Inventory
from ingredients import IngredientsType, Ingredient
from vending_machine import VendingMachine
from beverage import Beverage
from beverages_type import BeveragesType

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.outlets = 3
        self.inventory = Inventory.get_instance(self.outlets)
        self.vending_machine = VendingMachine.get_instance()
    
    def test_add_new_beverage(self):
        ingredients = list()
        ingredient = "hot_water"
        qty = 5
        obj_ingredient = Ingredient(ingredient, qty)
        ingredients.append(obj_ingredient)
        beverage = Beverage("black_coffee",ingredients)
        self.vending_machine.add_new_beverage(beverage)
    
    def test_make_beverage_with_adequate_ingredients(self):
        pass

if __name__ == '__main__':
    unittest.main()