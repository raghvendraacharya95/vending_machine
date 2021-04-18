from inventory import Inventory
from exceptions import InadequateIngridientsException

class VendingMachine:
    __instance = None
    beverages = list()

    @staticmethod
    def get_instance(outlets):
        if VendingMachine.__instance == None:
            VendingMachine.outlets = outlets
            VendingMachine()
        return VendingMachine.__instance

    def __init__(self):
        if VendingMachine.__instance != None:
            raise Exception("This is a singleton class")
        else:
            VendingMachine.__instance = self

    def __set_outlets(self, outlets):
        VendingMachine.outlets = outlets

    def add_new_beverage(self, beverage):
        VendingMachine.beverages.append(beverage)

    def make_beverage(self, beverage):
        can_make, inadequate_ingridients = self.can_make_beverage(beverage)
        inv = Inventory.get_instance()
        if can_make:
            for ingredient in beverage.ingredients:
                inv.deduct_ingredient_from_inventory(ingredient.ingredient_type, ingredient.quantity)
            print(beverage.beverages_type+" is prepared !!")
        else:
            raise InadequateIngridientsException(
                "Can not make "+ beverage.beverages_type +" becasue inadequate ingridient "+
                str(inadequate_ingridients),
            )

    def can_make_beverage(self, beverage):
        inadequate_ingridients = list()
        inv = Inventory.get_instance()
        for ingredient in beverage.ingredients:
            if not inv.is_sufficient_ingredient_available(ingredient.ingredient_type, ingredient.quantity):
                inadequate_ingridients.append(ingredient.ingredient_type)
        if len(inadequate_ingridients) > 0:
            return False, inadequate_ingridients
        return True, inadequate_ingridients
    