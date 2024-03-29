#Purpose: Restructure the previous chatbot as described on Canvas. (Travel Agent Part 2)
#Author: Anna Fong and Kaitlyn Lum
#Date: July 28, 2023

# PART 2

import random

destinations = []
flight_prices = []
hotel_prices = []
highlights = []
dest_highlights = []
accumulators = []

destinationFile = open("C:/Users/annaf/AppData/Local/Programs/Python/Python311/destinations.csv", 'r')
for aline in destinationFile:
    aline = aline.replace("\n", "")
    destinations.append(aline)
    accumulators.append(0)

flightPriceFile = open("C:/Users/annaf/AppData/Local/Programs/Python/Python311/flight_prices.csv", 'r')
for aline in flightPriceFile:
    aline = aline.replace("\n", "")
    flight_prices.append(aline)

hotelPriceFile = open("C:/Users/annaf/AppData/Local/Programs/Python/Python311/hotel_prices.csv", 'r')
for aline in hotelPriceFile:
    aline = aline.replace("\n", "")
    hotel_prices.append(aline)

highlightsFile = open("C:/Users/annaf/AppData/Local/Programs/Python/Python311/highlights.csv", 'r')
for aline in highlightsFile:
    aline = aline.replace("\n", "")
    highlights.append(aline)

print(destinations)
print(flight_prices)
print(hotel_prices)
print(highlights)

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

vacation_activity_booleans = []
def ask_user_preferences():
    
    for highlight in highlights:
        highlightQuestion = "Do you like " + highlight + " ?"
        vacation_activity_booleans.append(ask_yesno(highlightQuestion))
    return vacation_activity_booleans
 
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

def compute_totalcost(tripDestination, numberOfNights, age):
    global roundedTotalCost
    if (tripDestination in destinations):
        for i in range(len(destinations)):
            if place == destinations[i]:
                global index
                index = i
        totalCost = (float(flight_prices[index]) + float(hotel_prices[index]) * float(numberOfNights)) * ((100-discount)/100)
        roundedTotalCost = round(totalCost, 2)
    else:
        roundedTotalCost = 0
    return roundedTotalCost

def show_tripdetails(tripDestination, numberOfNights, age):
    if roundedTotalCost == 0:
        print("I'm sorry, we don't have any trips to offer at this point.\n")
    else:

        #totalCost = (flightPrice + hotelPrice * nights) * ((100-discount)/100)
        #roundedTotalCost = round(totalCost,2)
        print("\nHow about a trip to " + tripDestination + "?")
        print("Flight: " + str(flight_prices[index]) + "$")
        print("Hotel: " + str(hotel_prices[index]) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for", numberOfNights , "nights (incl. discounts): " + str(roundedTotalCost) + "$\n")

def suggest_trip(booleanValues):
    destHighlightsFile = open("C:/Users/annaf/AppData/Local/Programs/Python/Python311/dest_highlights.csv", 'r')
    for aline in destHighlightsFile:
        aline = aline.replace("\n", "").split(",")
        dest_highlights.append(aline)
    print(dest_highlights)
    
    for i in range(len(dest_highlights)):
        for j in (range(len(dest_highlights[i]))):
            if booleanValues[j] == True and dest_highlights[i][j] == "1":
                print(i)
                accumulators[i] += 1

    # i = 0 to start off. If new i is larger, then replace i with larger number.
    count = 0
    global place
    for i in range(len(accumulators)):
        if accumulators[i] > count:
            count = accumulators[i]
            place = destinations[i]
    if count > 0:
        return place
    else:
        place = "No place"
        return place
        
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
ask_user_preferences()
suggest_trip(vacation_activity_booleans)
compute_totalcost(place, nights, age)
show_tripdetails(place, nights, age)
ask_to_createaccount()