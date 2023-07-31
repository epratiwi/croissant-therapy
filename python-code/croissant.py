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

#NAME INPUT LOGIC
#Name logic - this will check if user has input their name and return with an error message if they did not enter their name.

name_logic = False
while not name_logic:
    user_name = input("What is your name? ")
    if user_name != "":
        name_logic = True
    else:
        print("Please enter your name! ")

#BAKERY INPUT LOGIC-------------------------------------------------------------------------------------------
#Bakery logic - asks the user which bakery they would like to go to and checks whether they enter valid bakery choices and will return error message if anything other than those 3 bakery choices are chosen.

bakery_prompt = ""
while True:
    bakery_prompt = input("Hello " + str(user_name) + "! Are we going to Beacoup, Angus T or Nemesis cafe today? ")

    if bakery_prompt.lower() == "nemesis" or bakery_prompt.lower() == "beacoup" or bakery_prompt.lower() == "angus t":
        break

    else:
        print("Please choose a valid bakery!")

bakery_input = bakery_prompt

#TYPE INPUT LOGIC---------------------------------------------------------------------------------------------
#Type logic - this will ask the user what type of croissant they would like. Checks if user's input matches either safe, sweet, savoury or adventurous choices. Will return error message if anything other than those 4 choices is chosen.

type_prompt = ""
while True:
    type_prompt = input("Are you feeling Safe, Sweet, Savoury or Adventurous today? ")

    if type_prompt.lower() == "safe" or type_prompt.lower() == "sweet" or type_prompt.lower() == "savoury" or type_prompt.lower() == "adventurous":
        break

    else:
        print("Please choose a valid croissant type! ")

type_input = type_prompt 

#BUDGET INPUT LOGIC--------------------------------------------------------------------------------------------
#Budget logic - Asks the user what their budget is for that day. Checks if budget is greater than 0 and if it is an integer.

budget_logic = False
while not budget_logic:
    try:
        budget_input = int(input("Final question. What is your budget today?" ))
        if budget_input > 0:
            budget_logic = True
            acceptable_budget_input = str(budget_input)
        else:
            print("Budget needs to be more than 0!")
    except ValueError:
        print ("Please input a valid budget!")

#Program Variables-------------------------------------------------------------------------------------------------

bakery = bakery_input.lower()
type = type_input.lower()
budget = acceptable_budget_input

#-----------------------------------------------PROGRAM LOGIC--------------------------------------------------------------

#BEACOUP BAKERY CROISSANTS
#If user input beacoup as their chosen bakery, the program will then check which type of croissant user want!

while bakery == "beacoup":

    #SAFE OPTIONS
    if type == "safe":

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
    elif type == "sweet":
        
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
    elif type == "savoury":

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
    elif type == "adventurous":

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
#If user input angus t as their chosen bakery, the program will then check which type of croissant user want!

while bakery == "angus t":

    #SAFE OPTIONS
    if type == "safe":
        
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
    elif type == "sweet":
       
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
    elif type == "savoury":

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
    elif type == "adventurous":
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
#If user input nemesis as their chosen bakery, the program will then check which type of croissant user want!

while bakery == "nemesis":

    #SAFE OPTIONS
    if type == "safe":
        
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
    elif type == "sweet":
       
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
    elif type == "savoury":

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
    elif type == "adventurous":
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