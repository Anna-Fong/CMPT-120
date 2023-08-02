#Purpose: Restructure the previous chatbot as described on Canvas. 
#Author: Anna Fong and Kaitlyn Lum
#Date: July 28, 2023

# import random module
import random

# function to welcome the user
def welcome():
    print('Welcome! I am your friendly travel agent bot.\n'\
    'I will ask you some questions, and make a\nrecommendation based on'\
    ' your answer.\nIf you are interested, I will provide you\n'\
    'with a one - time password to create a user\naccount on our website.\n')

# function to ask for user information
def ask_user_information ():
    
    # ask for name
    userName = input("What is your name? --> ")
    print("Hello dear " + userName + "!\n")

    # ask for age
    ask_number("What is your age? --> ")

    # call the discount function
    userAge = numberquestionresponse
    global discount
    discount = compute_discountpercentage(userAge)

    # ask for number of nights
    ask_number("\nFor how many nights do you want to stay? --> ")
    userNights = numberquestionresponse

    # return name, age, nights
    return userName, userAge, userNights

# function to ask for user preferences
def ask_user_preferences():

    # ask about culture
    ask_yesno("Do you like culture and classical music?")
    music = yesnoresponse

    # ask about beaches
    ask_yesno("Do you like beaches and surfing?")
    beaches = yesnoresponse

    # return preferences as booleans
    return music, beaches
 
# function to ask yes/no question
def ask_yesno(yesnoquestion):

    print(yesnoquestion)
    global yesnoresponse
    yesnoresponse = input("Please answer y/n. --> ")

    # set booleans based on response
    if yesnoresponse == "y":
        yesnoresponse = True
    elif yesnoresponse == "n":
        yesnoresponse = False
    else: 
        yesnoresponse = False

    # return their choice as a boolean
    return yesnoresponse

# function to ask a number-related question
def ask_number(numberquestion):

    global numberquestionresponse
    numberquestionresponse = int(input(numberquestion))

    # return their number response
    return numberquestionresponse

# function to calculate the discount
def compute_discountpercentage(userAge):
    # if 65 and over, each year is 1%
    if userAge > 64:
        seniorDiscount = (userAge - 64)
        print("Great! We offer a senior discount.")
        print("For every year over 64, you get 1% off.")
    # otherwise, no discount
    else: 
        seniorDiscount = 0
    # return discount as integer
    return seniorDiscount

# function to calculate cost of trip
def compute_totalcost(flightPrice, hotelPrice, nights, age):
    totalCost = (flightPrice + hotelPrice * nights) * ((100-discount)/100)
    roundedTotalCost = round(totalCost,2)
    # return cost as float
    return roundedTotalCost

# function to display the trip details 
def show_tripdetails(destination, flightPrice, hotelPrice, nights, age):
    if destination == "Vienna" or destination == "Bali":
        totalCost = (flightPrice + hotelPrice * nights) * ((100-discount)/100)
        roundedTotalCost = round(totalCost,2)
        print("\nHow about a trip to " + destination + "?")
        print("Flight: " + str(flightPrice) + "$")
        print("Hotel: " + str(hotelPrice) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for", nights , "nights (incl. discounts): " +
              str(roundedTotalCost) + "$\n")
    else:
        print("\nI'm sorry, we don't have any trips to offer at this point.\n")

# function to decide where the user should go, based on their preferences
def suggest_trip(culture, activity, viennaTotal, baliTotal):
    # if culture, then vienna trip
    if culture == True and activity == False:
        show_tripdetails("Vienna", 997.93, 143.84, nights, age)
        return viennaTotal
    # if beaches, then bali trip
    elif culture == False and activity == True:
        show_tripdetails("Bali", 849.93, 235.35, nights, age)
        return baliTotal
    # if neither culture or beaches, no trip
    elif culture == False and activity == False:
        show_tripdetails("None", 0, 0, nights, age)
        return None
    # if culture and beaches, choose the more expensive one. If equal, bali
    else:
        if viennaTotal > baliTotal:
            show_tripdetails("Vienna", 997.93, 143.84, nights, age)
            return viennaTotal
        else: 
            show_tripdetails("Bali", 849.93, 235.35, nights, age)
            return baliTotal
        
# function to ask user to make an account
def ask_to_createaccount():
    ask_yesno("Are you interested, and want to create a user account?")
    # If no, display an apology message
    if yesnoresponse == False:
        print("Sorry to hear that. Please consider using our service again.")
        print("\nGoodbye.")
    #If yes, create a password for the user
    else:
        lastLetter = name[-1] 
        beginningPassword = lastLetter * (age % 8)
        middlePassword = name[0]
        endPassword = random.randint(0,5) * "!"
        password = beginningPassword + middlePassword + endPassword
        print("Looking forward to working with you!\nYour one-time password is: "
               + password)
        print("\nGoodbye.")

#call functions
welcome()
name, age, nights = ask_user_information()
userCulture, userActivity = ask_user_preferences()
roundedViennaCost = compute_totalcost(997.93, 143.84, nights, age)
roundedBaliCost = compute_totalcost(849.93, 235.35, nights, age)
suggest_trip(userCulture, userActivity, roundedViennaCost, roundedBaliCost)
ask_to_createaccount()

