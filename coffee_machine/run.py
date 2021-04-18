from inventory import Inventory
from ingredients import IngredientsType, Ingredient
from sample_input import sample_input
from vending_machine import VendingMachine
from beverage import Beverage
# from exceptions import InadequateIngridientsException

def main():
    # Prepare Inventory
    obj_inventory = Inventory.get_instance()
    all_item_with_qty = get_total_items_qty()
    for item,qty in all_item_with_qty.items():
        obj_inventory.add_ingredient_to_inventory(item, qty)
    all_beverages = get_all_beverages()
    beverages = list()
    outlets = get_total_outlets()
    vending_machine = VendingMachine.get_instance(outlets)
    for beverage,ingredient_with_qty in all_beverages.items():
        ingredients = list()
        for ingredient,qty in ingredient_with_qty.items():
            obj_ingredient = Ingredient(ingredient, qty)
            ingredients.append(obj_ingredient)
        beverage = Beverage(beverage, ingredients)
        vending_machine.add_new_beverage(beverage)
        beverages.append(beverage)
    for beverage in beverages:
        try:
            vending_machine.make_beverage(beverage)
        except Exception as e:
            print(e)

def get_total_outlets():
    return sample_input["machine"]["outlets"]["count_n"]

def get_total_items_qty():
    return sample_input["machine"]["total_items_quantity"]

def get_all_beverages():
    return sample_input["machine"]["beverages"]

def available_beverages():
    return [beverage for beverage in sample_input["machine"]["beverages"]]

if __name__ == '__main__':
    main()