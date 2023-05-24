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

# Function to calculate total Bali cost
flightVienna = 997.93
hotelVienna = 143.84

def viennaTotal():
    totalVienna = (flightVienna + hotelVienna * userNights) * (1-seniorDiscount)
    print(totalVienna)

def baliTotal():
    flightBali = 849.93
    hotelBali = 235.35
    totalBali = (flightBali + hotelBali * userNights) * (1-seniorDiscount)
    print(totalBali)

# Function to display standard Vienna costs
def viennaInfo():
    print("\nHow about a trip to Vienna?")
    print("Flight: " + str(flightVienna) + "$")
    print("Hotel: " + str(hotelVienna) + "$/night")
    print("Discount: " + str(int(seniorDiscount)) + "%")
    print("Total for", str(userNights) , " nights (incl. discounts): ", end="")

# Make recommendations based on user's responses
# If user prefers culture over beach -> Vienna
if userCulture == 'y' and userActivity == 'n':
    viennaInfo()
    viennaTotal() #we need dollar sign here
    

  
