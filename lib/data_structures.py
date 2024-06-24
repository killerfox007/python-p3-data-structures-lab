spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    hottest_food = [food for food in spicy_foods if food["heat_level"] > 5]
    return hottest_food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {emoji}")

        

def get_average_heat_level(spicy_foods):
    total_heat = 0
    number_of_foods = len(spicy_foods)
    for food in spicy_foods:
        total_heat += food["heat_level"]

    return total_heat // number_of_foods


def create_spicy_food(spicy_foods, spicy_food):
     new_spicy_food = spicy_foods[:]
     new_spicy_food.append(spicy_food)
     return new_spicy_food
