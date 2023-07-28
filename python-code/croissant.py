import random

#CROISSANT DATA
BEACOUP_safe_croissants = {'Butter Croissant': '3.20', 'Pain au Chocolat': '4.00', 'Kouign Amann': '3.15'}

#Program Input
user_name = input("What is your name? ")
bakery_input = input("Hello " + str(user_name) + "! Are we going to Beacoup, Angus T or Nemesis cafe today? ")
type_input = input("Are you feeling Safe, Sweet, Savoury or Adventurous today? ")
budget_input = input("Final question. What is your budget today?" )

#Program Variables
bakery = bakery_input
budget = budget_input
type = type_input

#PROGRAM LOGIC

#BEACOUP BAKERY CROISSANTS
# def get_BEACOUP_croissant(bakery, type, budget):
while bakery == "Beacoup":

    if type == "Safe":
        for croissant_check, price_check in BEACOUP_safe_croissants.items():
            if price_check > budget:
                print("Budget too low :(")
                break
            else:
                SAFE_affordable_croissants =  dict([(croissant, price) for croissant, price in BEACOUP_safe_croissants.items() if price <= budget])
                todays_SAFE_choice = random.choice(list(SAFE_affordable_croissants.keys()))
                print(todays_SAFE_choice)
                break
    break

        


# Beacoup = {
    # 'Savoury': ['Ham and Cheese Scroll', 'Onion Bacon Scroll'],
    # 'Adventurous': ['Valrhona Chocolate Chip Cookie', 'Salted Chocolate Rosemary Cookie']
    # }

# Angus_T = {
    # 'Safe': ['Butter Croissant', 'Pain au Chocolat', 'Kouign Amann'], 
    # 'Sweet': ['Pain au Chocolat', 'Earl Grey Croissant', 'Green Tea Croissant', 'Dark Chocolate Raspberry Croissant'],
    # 'Savoury': ['Ham & Gruyere Croissant', 'Chicken & Tomato Croissant', 'Balsamic Onion Jam & Bacon Croissant', '3 Cheese Croissant'],
    # 'Adventurous': ['Earl Grey Croissant', 'Green Tea Croissant', 'Blueberry Croissant', 'Lemon Curd Croissant', 'Gianduja Mocha Croissant', 'Black Sesame Croissant']
    # }

# Nemesis = {
    # 'Safe': ['Butter Croissant', 'Pain au Chocolate', 'The Queen'], 
    # 'Sweet': ['Pain au Chocolat', 'Tiramisu Croissant', 'Banoffee Pie Cruffin', 'Pistachio Swirl'],
    # 'Savoury': ['Ham and Cheese Scroll', 'Onion Bacon Scroll'],
    # 'Adventurous': ['Raspberry & Rose Cruffin', 'Blueberry Pavlova Cruffin', 'Coconut, White chocolate & Cherry Croissant']
    # }
