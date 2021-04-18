import enum
 
 
class IngredientsType(enum.Enum):
    HotWater = "hot_water"
    HotMilk = "hot_milk"
    TeaLeavesSyrup = "tea_leaves_syrup"
    GingerSyrup = "ginger_syrup"
    SugarSyrup = "sugar_syrup"
    ElaichiSyrup = "elaichi_syrup"
    CoffeSyrup = "coffe_syrup"

class Ingredient:
    def __init__(self, ingredient_type, quantity):
        self.ingredient_type = ingredient_type
        self.quantity = quantity