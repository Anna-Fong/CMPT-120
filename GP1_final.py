# Purpose: Create a program that acts as a "travel agent bot". For example, it will ask the user some 
#          questions and make a recommendation based on their responses. 
# Authors: Anna Fong, Kaitlyn Lum
# Date: May 22, 2023
# Course: CMPT 120

import random

# Greeting for user 
print('Welcome! I am your friendly travel agent bot.\nI will ask you some questions, and make a\n'\
'recommendation based on your answer.\nIf you are interested, I will provide you\n'\
'with a one - time password to create a user\naccount on our website.\n')

# Ask user for name and greet user
userName = input("What is your name? --> ")
print("Hello dear " + userName + "!\n")

# Ask user for age
userAge = int(input("What is your age? --> "))

#calculates the discount if user is a senior (over 64 in age)
if userAge > 64:
    seniorDiscount = (userAge - 64)/100
    print("Great! We offer a senior discount.\nFor every year over 64, you get 1% off.")
else: seniorDiscount = 0

# Ask user how many nights they want to stay
userNights = int(input("\nFor how many nights do you want to stay? --> "))

# Ask whether the user is interested in culture and classical music, or beaches and surfing
userCulture = input("Do you like culture and classical music?\nPlease answer y/n. --> ")
userActivity = input("Do you like beaches and surfing?\nPlease answer y/n. --> ")

# Variables to store cost information
flightVienna = 997.93
hotelVienna = 143.84
flightBali = 849.93
hotelBali = 235.35

# Function to calculate total Vienna cost
def viennaTotal():
    totalVienna = (flightVienna + hotelVienna * userNights) * (1-seniorDiscount)
    rTotalVienna = round(totalVienna,2)
    print(str(rTotalVienna) + "$")
    return totalVienna

# Function to calculate total Bali cost
def baliTotal():
    totalBali = (flightBali + hotelBali * userNights) * (1-seniorDiscount)
    rTotalBali = round(totalBali,2)
    print(str(rTotalBali) + "$")
    return totalBali

# Function to display standard Vienna costs
def viennaInfo():
    print("\nHow about a trip to Vienna?")
    print("Flight: " + str(flightVienna) + "$")
    print("Hotel: " + str(hotelVienna) + "$/night")
    print("Discount: " + str(int(seniorDiscount*100)) + "%")
    print("Total for", str(userNights) , "nights (incl. discounts): ", end="")

# Function to display standard Bali costs
def baliInfo():
    print("\nHow about a trip to Bali?")
    print("Flight: " + str(flightBali) + "$")
    print("Hotel: " + str(hotelBali) + "$/night")
    print("Discount: " + str(int(seniorDiscount*100)) + "%")
    print("Total for", str(userNights) , "nights (incl. discounts): ", end="")

# Make recommendations based on user's responses
# If user prefers culture over beach, recommend Vienna
if userCulture == 'y' and userActivity == 'n':
    viennaInfo()
    viennaTotal()

# If user prefers beach over culture, recommend Bali
elif userCulture == 'n' and userActivity == 'y':
    baliInfo()
    baliTotal()

# If user prefers neither culture or beach, recommend none
elif userCulture == 'n' and userActivity == 'n':
    print("\nI am sorry, we don't have any trips to offer at this point.")

# If user prefers both culture and beaches, calculate more expensive trip and offer that to the user
else: 
    # Re-write total costs of both trips. Must re-write lines because they are stuck in functions
    totalVienna = (flightVienna + hotelVienna * userNights) * (1-seniorDiscount)
    totalBali = (flightBali + hotelBali * userNights) * (1-seniorDiscount)

    # If the trip to Vienna is more expensive, suggest this trip to the user
    # This prints out the totals when doing this kind of comparison
    if totalVienna>totalBali:
        viennaInfo()
        viennaTotal()

    # When the price for Bali is more expensive or equal to Vienna, suggest going to Bali to user
    else: 
        baliInfo()
        baliTotal()
 
# Ask user if they are interested in creating a user account
userAccount = input("\nAre you interested, and want to create a user account?\nPlease answer y/n: --> ")

# If no, display an apology message
if userAccount == 'n':
    print("Sorry to hear that. Please consider using our service again.")

# If yes, create a password for the user
elif userAccount == 'y':
    lastLetter = userName[-1] 
    beginningPassword = lastLetter * (userAge % 8)
    middlePassword = userName[0]
    endPassword = random.randint(0,5) * "!"
    password = beginningPassword + middlePassword + endPassword
    print("Looking forward to working with you!\nYour one-time password is: " + password)

# Display goodbye message
print("\nGoodbye.")



