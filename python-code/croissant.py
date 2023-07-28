import random

#BEACOUP CROISSANT DATA
BEACOUP_safe_croissants = {'Butter Croissant': '3.20', 'Pain au Chocolat': '4.00', 'Kouign Amann': '3.15'}
BEACOUP_savoury_croissants = {'Ham and Cheese Croissant': '7.35', 'Onion Bacon Scroll': '6.45'}
BEACOUP_sweet_croissants = {'Pain au Chocolat': '4.00', 'Cinnamon Scroll': '5.00'}
BEACOUP_adventurous_croissants = {'Valhorna Chocolate Chip Cookie': '3.79', 'Salted Chocolate Rosemary Cookie': '4.15'}

#ANGUS T CROISSANT DATA
ANGUST_safe_croissants = {'Butter Croissant': '2.79', 'Pain au Chocolat': '5.68', 'Kouign Amann': '2.15'}
ANGUST_sweet_croissants = {}
ANGUST_savoury_croissants = {}
ANGUST_adventurous_croissants = {}

#NEMESIS CROISSANT DATA
NEMESIS_safe_croissants = {}
NEMESIS_sweet_croissants = {}
NEMESIS_savoury_croissants = {}
NEMESIS_adventurous_croissants = {}

#--------------------------------------------------------Program Input--------------------------------------------------
user_name = input("What is your name? ")
bakery_input = input("Hello " + str(user_name) + "! Are we going to Beacoup, Angus T or Nemesis cafe today? ")
type_input = input("Are you feeling Safe, Sweet, Savoury or Adventurous today? ")
budget_input = input("Final question. What is your budget today?" )

#Program Variables
bakery = bakery_input
budget = budget_input
type = type_input

#-----------------------------------------------PROGRAM LOGIC--------------------------------------------------------------

#BEACOUP BAKERY CROISSANTS
while bakery == "Beacoup":

    #SAFE OPTIONS
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
    
    #SWEET OPTIONS
    elif type == "Sweet":
        for croissant_check, price_check in BEACOUP_sweet_croissants.items():
            if price_check > budget:
                print("Budget too low :(")
                break
            else:
                SWEET_affordable_croissants =  dict([(croissant, price) for croissant, price in BEACOUP_sweet_croissants.items() if price <= budget])
                todays_SWEET_choice = random.choice(list(SWEET_affordable_croissants.keys()))
                print(todays_SWEET_choice)
                break
    
    #SAVOURY OPTIONS
    elif type == "Savoury":
        for croissant_check, price_check in BEACOUP_savoury_croissants.items():
            if price_check > budget:
                print("Budget too low :(")
                break
            else:
                SAVOURY_affordable_croissants =  dict([(croissant, price) for croissant, price in BEACOUP_savoury_croissants.items() if price <= budget])
                todays_SAVOURY_choice = random.choice(list(SAVOURY_affordable_croissants.keys()))
                print(todays_SAVOURY_choice)
                break

    #ADVENTUROUS OPTIONS
    elif type == "Adventurous":
        for croissant_check, price_check in BEACOUP_adventurous_croissants.items():
            if price_check > budget:
                print("Budget too low :(")
                break
            else:
                ADVENTUROUS_affordable_croissants =  dict([(croissant, price) for croissant, price in BEACOUP_adventurous_croissants.items() if price <= budget])
                todays_ADVENTUROUS_choice = random.choice(list(ADVENTUROUS_affordable_croissants.keys()))
                print(todays_ADVENTUROUS_choice)
                break
    break

        


# Angus_T = {
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
