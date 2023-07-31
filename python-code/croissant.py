import random

#BEACOUP CROISSANT DATA
BEACOUP_safe_croissants = {'Butter Croissant': '3.20', 'Pain au Chocolat': '4.00', 'Kouign Amann': '3.15'}
BEACOUP_savoury_croissants = {'Ham and Cheese Croissant': '7.35', 'Onion Bacon Scroll': '6.45'}
BEACOUP_sweet_croissants = {'Pain au Chocolat': '4.00', 'Cinnamon Scroll': '5.00'}
BEACOUP_adventurous_croissants = {'Valhorna Chocolate Chip Cookie': '3.79', 'Salted Chocolate Rosemary Cookie': '4.15'}

#ANGUS T CROISSANT DATA
ANGUST_safe_croissants = {'Butter Croissant': '2.79', 'Pain au Chocolat': '5.68', 'Kouign Amann': '2.15'}
ANGUST_sweet_croissants = {'Earl Grey Croissant': '5.81', 'Dark Chocolate Raspberry Croissant': '7.00'}
ANGUST_savoury_croissants = {'Ham & Gruyere Croissant': '4.76', '3 Cheese Croissant': '4.32'}
ANGUST_adventurous_croissants = {'Green Tea Croissant': '6.34', 'Gianduja Mocha Croissant': '7.34'}

#NEMESIS CROISSANT DATA 
NEMESIS_safe_croissants = {'Butter Croissant': '3.21', 'The Queen': '4.23'}
NEMESIS_sweet_croissants = {'Tiramisu Croissant': '8.22', 'Banoffee Pie Cruffin': '5.20'}
NEMESIS_savoury_croissants = {'Smoked Ham Croissant': '7.90', 'Mortadella Croissant': '6.34'}
NEMESIS_adventurous_croissants = {'Coconut White Chocolate': '6.75', 'Raspberry & Rose Cruffin': '7.50'}

#--------------------------------------------------------Program Input--------------------------------------------------
user_name = input("What is your name? ")

#BAKERY INPUT LOGIC-------------------------------------------------------------------------------------------

bakery_prompt = ""
def bakery_choice(bakery_prompt):

    while True:
        bakery_prompt = input("Hello " + str(user_name) + "! Are we going to Beacoup, Angus T or Nemesis cafe today? ")

        if bakery_prompt.lower() == "nemesis":
            break

        if bakery_prompt.lower() == "beacoup":
            break
    
        if bakery_prompt.lower() == "angus t":
            break

        else:
            print("Please choose a valid bakery! ")

bakery_input = bakery_choice(bakery_prompt) 

#TYPE INPUT LOGIC---------------------------------------------------------------------------------------------
type_input = input("Are you feeling Safe, Sweet, Savoury or Adventurous today? ")

if type_input == "Safe" or "Sweet" or "Savoury" or "Adventurous":
    pass
elif type_input != "Safe" or "Sweet" or "Savoury" or "Adventurous":
    print("Please input valid croissant type.")
    type_input = input("Are you feeling Safe, Sweet, Savoury or Adventurous today? ")

#BUDGET INPUT LOGIC--------------------------------------------------------------------------------------------
budget_input = input("Final question. What is your budget today?" )

if budget_input == None:
    print("Please input your budget!")
    budget_input = input("Final question. What is your budget today?" )
else:
    pass

#Program Variables-------------------------------------------------------------------------------------------------

bakery = bakery_input
budget = budget_input
type = type_input

#-----------------------------------------------PROGRAM LOGIC--------------------------------------------------------------

#BEACOUP BAKERY CROISSANTS
while bakery == "Beacoup":

    #SAFE OPTIONS
    if type == "Safe":

        #Get a random croissant choice
        SAFE_affordable_croissants = dict(BEACOUP_safe_croissants.items())
        todays_SAFE_choice = random.choice(list(SAFE_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = BEACOUP_safe_croissants.get(todays_SAFE_choice)
        if price_check <= budget:
            print(todays_SAFE_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SWEET OPTIONS
    elif type == "Sweet":
        
        #Get a random croissant choice
        SWEET_affordable_croissants = dict(BEACOUP_sweet_croissants.items())
        todays_SWEET_choice = random.choice(list(SWEET_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = BEACOUP_sweet_croissants.get(todays_SWEET_choice)
        if price_check <= budget:
            print(todays_SWEET_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SAVOURY OPTIONS
    elif type == "Savoury":

        #Get a random croissant choice
        SAVOURY_affordable_croissants = dict(BEACOUP_savoury_croissants.items())
        todays_SAVOURY_choice = random.choice(list(SAVOURY_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = BEACOUP_savoury_croissants.get(todays_SAVOURY_choice)
        if price_check <= budget:
            print(todays_SAVOURY_choice)
            break
        else:
            print("Budget too low :(")
            break

    #ADVENTUROUS OPTIONS
    elif type == "Adventurous":

        #Get a random croissant choice
        ADVENTUROUS_affordable_croissants = dict(BEACOUP_adventurous_croissants.items())
        todays_ADVENTUROUS_choice = random.choice(list(ADVENTUROUS_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = BEACOUP_adventurous_croissants.get(todays_ADVENTUROUS_choice)
        if price_check <= budget:
            print(todays_ADVENTUROUS_choice)
            break
        else:
            print("Budget too low :(")
            break
    break

#ANGUST BAKERY CROISSANTS------------------------------------------------------------------------
while bakery == "Angus T":

    #SAFE OPTIONS
    if type == "Safe":
        
        #Get a random croissant choice
        SAFE_affordable_croissants = dict(ANGUST_safe_croissants.items())
        todays_SAFE_choice = random.choice(list(SAFE_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = ANGUST_safe_croissants.get(todays_SAFE_choice)
        if price_check <= budget:
            print(todays_SAFE_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SWEET OPTIONS
    elif type == "Sweet":
       
       #Get a random croissant choice
        SWEET_affordable_croissants = dict(ANGUST_sweet_croissants.items())
        todays_SWEET_choice = random.choice(list(SWEET_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = ANGUST_sweet_croissants.get(todays_SWEET_choice)
        if price_check <= budget:
            print(todays_SWEET_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SAVOURY OPTIONS
    elif type == "Savoury":

         #Get a random croissant choice
        SAVOURY_affordable_croissants = dict(ANGUST_savoury_croissants.items())
        todays_SAVOURY_choice = random.choice(list(SAVOURY_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = ANGUST_savoury_croissants.get(todays_SAVOURY_choice)
        if price_check <= budget:
            print(todays_SAVOURY_choice)
            break
        else:
            print("Budget too low :(")
            break


    #ADVENTUROUS OPTIONS
     #Get a random croissant choice
    elif type == "Adventurous":
        ADVENTUROUS_affordable_croissants = dict(ANGUST_adventurous_croissants.items())
        todays_ADVENTUROUS_choice = random.choice(list(ADVENTUROUS_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = ANGUST_adventurous_croissants.get(todays_ADVENTUROUS_choice)
        if price_check <= budget:
            print(todays_ADVENTUROUS_choice)
            break
        else:
            print("Budget too low :(")
            break
    break

#NEMESIS BAKERY CROISSANTS------------------------------------------------------------------------
while bakery == "Nemesis":

    #SAFE OPTIONS
    if type == "Safe":
        
        #Get a random croissant choice
        SAFE_affordable_croissants = dict(NEMESIS_safe_croissants.items())
        todays_SAFE_choice = random.choice(list(SAFE_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = NEMESIS_safe_croissants.get(todays_SAFE_choice)
        if price_check <= budget:
            print(todays_SAFE_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SWEET OPTIONS
    elif type == "Sweet":
       
       #Get a random croissant choice
        SWEET_affordable_croissants = dict(NEMESIS_sweet_croissants.items())
        todays_SWEET_choice = random.choice(list(SWEET_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = NEMESIS_sweet_croissants.get(todays_SWEET_choice)
        if price_check <= budget:
            print(todays_SWEET_choice)
            break
        else:
            print("Budget too low :(")
            break
    
    #SAVOURY OPTIONS
    elif type == "Savoury":

         #Get a random croissant choice
        SAVOURY_affordable_croissants = dict(NEMESIS_savoury_croissants.items())
        todays_SAVOURY_choice = random.choice(list(SAVOURY_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = NEMESIS_savoury_croissants.get(todays_SAVOURY_choice)
        if price_check <= budget:
            print(todays_SAVOURY_choice)
            break
        else:
            print("Budget too low :(")
            break


    #ADVENTUROUS OPTIONS
     #Get a random croissant choice
    elif type == "Adventurous":
        ADVENTUROUS_affordable_croissants = dict(NEMESIS_adventurous_croissants.items())
        todays_ADVENTUROUS_choice = random.choice(list(ADVENTUROUS_affordable_croissants.keys()))
    
        #Check if price of croissant is within budget
        price_check = NEMESIS_adventurous_croissants.get(todays_ADVENTUROUS_choice)
        if price_check <= budget:
            print(todays_ADVENTUROUS_choice)
            break
        else:
            print("Budget too low :(")
            break
    break