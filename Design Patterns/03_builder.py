# Product: Meal
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name}, Packing: {item.packing}, Price: {item.price}")

# Abstract Builder: ItemBuilder
class ItemBuilder:
    def build_burger(self):
        pass

    def build_fries(self):
        pass

    def build_drink(self):
        pass

# Concrete Builder: VegMealBuilder
class VegMealBuilder(ItemBuilder):
    def __init__(self):
        self.meal = Meal()

    def build_burger(self):
        burger = Item("Veg Burger", "Wrapper", 2.5)
        self.meal.add_item(burger)

    def build_fries(self):
        fries = Item("French Fries", "Bag", 1.5)
        self.meal.add_item(fries)

    def build_drink(self):
        drink = Item("Coke", "Bottle", 1.0)
        self.meal.add_item(drink)

    def get_meal(self):
        return self.meal

# Product: Item
class Item:
    def __init__(self, name, packing, price):
        self.name = name
        self.packing = packing
        self.price = price

# Director: Waiter
class Waiter:
    def __init__(self, builder):
        self.builder = builder

    def construct_meal(self):
        self.builder.build_burger()
        self.builder.build_fries()
        self.builder.build_drink()

# Client code
if __name__ == "__main__":
    # Creating a VegMeal using the VegMealBuilder
    veg_meal_builder = VegMealBuilder()
    waiter = Waiter(veg_meal_builder)

    waiter.construct_meal()
    veg_meal = veg_meal_builder.get_meal()

    # Displaying the items in the VegMeal
    print("Veg Meal:")
    veg_meal.show_items()
