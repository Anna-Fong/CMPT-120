# Greeting for user 
print('Welcome! I am your friendly travel agent bot.\nI will ask you some questions, and make a\n'\
'recommendation based on your answer.\nIf you are interested , I will provide you\n'\
'with a one - time password to create a user\naccount on our website .\n')

# Ask user for name and greet user
userName = input("What is your name? --> ")
print("Hello dear " + userName + "!\n")

# Ask user for age
userAge = int(input("What is your age? --> "))

#calculates the discount if user is a senior (over 64 in age)
seniorDiscount=0
if userAge > 64:
    seniorDiscount=(userAge-64)/100
    print("Great! We offer a senior discount.\nFor every year over 64, you get 1% off.")
else: seniorDiscount=0

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
    print(str(totalVienna)+ "$")

# Function to calculate total Bali cost
def baliTotal():
    totalBali = (flightBali + hotelBali * userNights) * (1-seniorDiscount)
    print(totalBali)

# Function to display standard Vienna costs
def viennaInfo():
    print("\nHow about a trip to Vienna?")
    print("Flight: " + str(flightVienna) + "$")
    print("Hotel: " + str(hotelVienna) + "$/night")
    print("Discount: " + str(int(seniorDiscount)) + "%")
    print("Total for", str(userNights) , " nights (incl. discounts): ", end="")

# Function to display standard Bali costs
def baliInfo():
    print("\nHow about a trip to Bali?")
    print("Flight: " + str(flightBali) + "$")
    print("Hotel: " + str(hotelBali) + "$/night")
    print("Discount: " + str(int(seniorDiscount)) + "%")
    print("Total for", str(userNights) , " nights (incl. discounts): ", end="")

# Make recommendations based on user's responses
# If user prefers culture over beach, recommend Vienna
if userCulture == 'y' and userActivity == 'n':
    viennaInfo()
    viennaTotal()

# If user prefers beach over culture, recommend Bali
if userCulture == 'n' and userActivity == 'y':
    baliInfo()
    baliTotal()

# If user prefers neither culture or beach, recommend none
if userCulture == 'n' and userActivity == 'n':
    print("\nI am sorry, we don't have any trips to offer at this point.")


# If user prefers both culture and beaches, calculate more expensive trip and offer that to the user
# else:
    # should we do the calculation again in here? im not sure how to compare the costs in here

