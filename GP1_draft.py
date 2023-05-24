# Purpose: Create a program that acts as a "travel agent bot". For example, it will ask the user some 
#          questions and make a recommendation based on their responses. 
# Authors: Anna Fong
# Date: May 22, 2023
# Course: CMPT 120


# Display welcome message
print("Welcome! I am your friendly travel agent bot. I will ask you some questions, and make a " + 
      "recommendation based on your answer.\nIf you are interested, I will provide you with a " + 
      "one-time password to create a user account on our website.\n")

# Ask user for name and greet user
userName = input("What is your name? ")
print("Hello dear " + userName + "!\n")

# Ask user for age
userAge = float(input("What is your age? "))

# Tell user about discount if they are 65+, store discount value in a variable
if userAge > 64:
    discount = userAge - 64
    print("Great! We offer a senior discount.\nFor every year over 64, you get 1% off.")
else:
    discount = 0

# Ask user how many nights they want to stay
userNights = int(input("\nFor how many nights do you want to stay? "))

# Ask whether the user is interested in culture and classical music, or beaches and surfing
userCulture = input("Do you like culture and classical music?\nPlease answer y/n. ")
userActivity = input("Do you like beaches and surfing?\nPlease answer y/n. ")

# Calculate total cost for Vienna trip
flightVienna = 997.93
hotelVienna = 143.84
if discount == 0:
    totalVienna = flightVienna + hotelVienna * userNights
if discount != 0:
    totalVienna = (flightVienna + hotelVienna * userNights) * ((100 - discount)/100)

# Calculate total cost for Bali trip
flightBali = 849.93
hotelBali = 235.35
if discount == 0:
    totalBali = flightBali + hotelBali * userNights
if discount != 0:
    totalBali = (flightBali + hotelBali * userNights) * ((100 - discount)/100)

# Round total costs
roundedVienna = round(totalVienna, 2)   
roundedBali = round(totalBali, 2) 

# Make recommendations based on user's responses
# If user prefers culture over beach -> Vienna
if userCulture == 'y' and userActivity == 'n':
    print("\nHow about a trip to Vienna?")
    print("Flight: " + str(flightVienna) + "$")
    print("Hotel: " + str(hotelVienna) + "$/night")
    print("Discount: " + str(int(discount)) + "%")
    print("Total for " + str(userNights) + " nights (incl. discounts): " + str(totalVienna) + "$")

# If user prefers beach over culture -> Bali
if userCulture == 'n' and userActivity == 'y':
    print("\nHow about a trip to Bali?")
    print("Flight: " + str(flightBali) + "$")
    print("Hotel: " + str(hotelBali) + "$/night")
    print("Discount: " + str(int(discount)) + "%")
    print("Total for " + str(userNights) + " nights (incl. discounts): " + str(totalBali) + "$")

# If user prefers neither culture or beach -> None
if userCulture == 'n' and userActivity == 'n':
    print("\nI am sorry, we don't have any trips to offer at this point.")

# If user prefers both culture and beach -> Most expensive option (Bali if equal)
if userCulture == 'y' and userActivity == 'y':
    if totalBali >= totalVienna:
        print("\nHow about a trip to Bali?")
        print("Flight: " + str(flightBali) + "$")
        print("Hotel: " + str(hotelBali) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for " + str(userNights) + " nights (incl. discounts): " + str(totalBali) + "$")    
    if totalVienna > totalBali:
        print("How about a trip to Vienna?")
        print("Flight: " + str(flightVienna) + "$")
        print("Hotel: " + str(hotelVienna) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for " + str(userNights) + " nights (incl. discounts): " + str(totalVienna) + "$")

# Generate a one-time password
