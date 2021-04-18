class Inventory:
    inventory = dict()
    __instance = None

    @staticmethod
    def get_instance():
        if Inventory.__instance == None:
            Inventory()
        return Inventory.__instance

    def __init__(self):
        if Inventory.__instance != None:
            raise Exception("This is a singleton class")
        else:
            Inventory.__instance = self

    def add_ingredient_to_inventory(self, ingredient, quantity):
        Inventory.inventory[ingredient] = quantity

    def deduct_ingredient_from_inventory(self, ingredient, quantity):
        current_quantity = Inventory.inventory.get(ingredient)
        if current_quantity >= quantity:
            Inventory.inventory[ingredient] = current_quantity - quantity
        else:
            raise Exception("Can't udpate Inventory")

    def is_sufficient_ingredient_available(self, ingredient, required_quantity):
        current_quantity = Inventory.inventory.get(ingredient, 0)
        return current_quantity >= required_quantity

    def get_available_ingredients(self):
        return Inventory.inventory

    def get_ingredient_available_qty(self, ingredient):
        return Inventory.inventory.get(ingredient)
