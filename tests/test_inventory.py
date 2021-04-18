import os
import sys
sys.path.append('/Users/raghvendra/Desktop/assignment/dunzo_assignment/vending_machine/coffee_machine')
import unittest
from inventory import Inventory
from ingredients import IngredientsType, Ingredient

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory.get_instance()
    
    def test_add_ingredient_to_inventory(self):
        obj_ingredient = Ingredient(IngredientsType.CoffeSyrup, 50)
        self.inventory.add_ingredient_to_inventory(obj_ingredient.ingredient_type.value, obj_ingredient.quantity)
        obj_ingredient = Ingredient(IngredientsType.HotWater, 100)
        self.inventory.add_ingredient_to_inventory(obj_ingredient.ingredient_type.value, obj_ingredient.quantity)
        obj_ingredient = Ingredient(IngredientsType.ElaichiSyrup, 20)
        self.inventory.add_ingredient_to_inventory(obj_ingredient.ingredient_type.value, obj_ingredient.quantity)
        obj_ingredient = Ingredient(IngredientsType.HotMilk, 80)
        self.inventory.add_ingredient_to_inventory(obj_ingredient.ingredient_type.value, obj_ingredient.quantity)
        obj_ingredient = Ingredient(IngredientsType.GingerSyrup, 20)
        self.inventory.add_ingredient_to_inventory(obj_ingredient.ingredient_type.value, obj_ingredient.quantity)
        self.assertEquals(len(self.inventory.inventory), 5)
        
    def test_deduct_ingredient_from_inventory(self):
        hot_water = IngredientsType.HotWater.value
        current_hot_water_qty = self.inventory.get_ingredient_available_qty(hot_water)
        qty_to_deduct = 10
        self.inventory.deduct_ingredient_from_inventory(hot_water, qty_to_deduct)
        print(self.inventory.get_ingredient_available_qty(hot_water))
        self.assertEquals(self.inventory.get_ingredient_available_qty(hot_water), 90)
        
    def test_is_sufficient_ingredient_available(self):
        pass

if __name__ == '__main__':
    unittest.main()