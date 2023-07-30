#Purpose: Restructure the previous chatbot as described on Canvas. (Travel Agent Part 2)
#Author: Anna Fong and Kaitlyn Lum
#Date: July 28, 2023



# still need comments

import random

def welcome():
    print('Welcome! I am your friendly travel agent bot.\n'\
    'I will ask you some questions, and make a\nrecommendation based on'\
    ' your answer.\nIf you are interested, I will provide you\n'\
    'with a one - time password to create a user\naccount on our website.\n')

def ask_user_information ():
    
    userName = input("What is your name? --> ")
    print("Hello dear " + userName + "!\n")

    ask_number("What is your age? --> ")

    userAge = numberquestionresponse
    global discount
    discount = compute_discountpercentage(userAge)

    ask_number("\nFor how many nights do you want to stay? --> ")
    userNights = numberquestionresponse

    return userName, userAge, userNights


def ask_user_preferences():

    ask_yesno("Do you like culture and classical music?")
    music = yesnoresponse

    ask_yesno("Do you like beaches and surfing?")
    beaches = yesnoresponse

    return music, beaches
 
 
def ask_yesno(yesnoquestion):

    print(yesnoquestion)
    global yesnoresponse
    yesnoresponse = input("Please answer y/n. --> ")

    if yesnoresponse == "y":
        yesnoresponse = True
    elif yesnoresponse == "n":
        yesnoresponse = False
    else: 
        yesnoresponse = False

    return yesnoresponse

def ask_number(numberquestion):

    global numberquestionresponse
    numberquestionresponse = int(input(numberquestion))

    return numberquestionresponse

def compute_discountpercentage(userAge):
    if userAge > 64:
        seniorDiscount = (userAge - 64)
        print("Great! We offer a senior discount.")
        print("For every year over 64, you get 1% off.")
    else: 
        seniorDiscount = 0
    return seniorDiscount

def compute_totalcost(flightPrice, hotelPrice, nights, age):
    totalCost = (flightPrice + hotelPrice * nights) * (100-discount/100)
    roundedTotalCost = round(totalCost,2)
    return roundedTotalCost

def show_tripdetails(destination, flightPrice, hotelPrice, nights, age):
    if destination == "Vienna" or destination == "Bali":
        totalCost = (flightPrice + hotelPrice * nights) * ((100-discount)/100)
        roundedTotalCost = round(totalCost,2)
        print("\nHow about a trip to " + destination + "?")
        print("Flight: " + str(flightPrice) + "$")
        print("Hotel: " + str(hotelPrice) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for", nights , "nights (incl. discounts): " + str(roundedTotalCost) + "$\n")
    else:
        print("\nI'm sorry, we don't have any trips to offer at this point.\n")

def suggest_trip(culture, activity, viennaTotal, baliTotal):
    if culture == True and activity == False:
        show_tripdetails("Vienna", 997.93, 143.84, nights, age)
        return viennaTotal
    elif culture == False and activity == True:
        show_tripdetails("Bali", 849.93, 235.35, nights, age)
        return baliTotal
    elif culture == False and activity == False:
        show_tripdetails("None", 0, 0, nights, age)
        return None
    else:
        if viennaTotal > baliTotal:
            show_tripdetails("Vienna", 997.93, 143.84, nights, age)
            return viennaTotal
        else: 
            show_tripdetails("Bali", 849.93, 235.35, nights, age)
            return baliTotal
        
def ask_to_createaccount():
    ask_yesno("Are you interested, and want to create a user account?")

# If no, display an apology message
    if yesnoresponse == False:
        print("Sorry to hear that. Please consider using our service again.")
        print("\nGoodbye.")
# If yes, create a password for the user
    else:
        lastLetter = name[-1] 
        beginningPassword = lastLetter * (age % 8)
        middlePassword = name[0]
        endPassword = random.randint(0,5) * "!"
        password = beginningPassword + middlePassword + endPassword
        print("Looking forward to working with you!\nYour one-time password is: " + password)
        print("\nGoodbye.")

#call functions
welcome()
name, age, nights = ask_user_information()
userCulture, userActivity = ask_user_preferences()
#discount = compute_discountpercentage(age)
# vienna
roundedViennaCost = compute_totalcost(997.93, 143.84, nights, age)
# bali
roundedBaliCost = compute_totalcost(849.93, 235.35, nights, age)
suggest_trip(userCulture, userActivity, roundedViennaCost, roundedBaliCost)
ask_to_createaccount()

