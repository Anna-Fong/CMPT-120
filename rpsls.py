# Purpose: A program for the game "Rock, Paper, Scissors, Lizard, Spock" as
#          shown on Canvas.
# Authors: Kaitlyn Lum, Anna Fong
# Date: July 24, 2023

# import random module
import random

# list and dictionaries to keep track of points and choices
choiceList = ["rock", "paper", "scissors", "lizard", "spock"]
choiceCounterUser = {"rock":0, "paper":0, "scissors":0, "lizard":0, "spock":0}
choiceCounterComp = {"rock":0, "paper":0, "scissors":0, "lizard":0, "spock":0}
winDict = {"user":0, "comp":0, "draw":0}

# display welcome message
print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

# ask user for number of rounds
rounds = int(input("How many rounds do you want to play? ==> "))

# function to see who wins
def beats(x,y):
    global draws
    draws = "False"
    if x == "1":
        x = "rock"
    elif x == "2":
        x = "paper"
    elif x == "3":
        x = "scissors"
    elif x == "4":
        x = "lizard"
    elif x == "5":
        x = "spock"
    # accumulator to add points
    choiceCounterUser[x] +=1
    choiceCounterComp[y] +=1
    # if statements to compare to see who wins the round
    # user wins
    if x == "scissors" and y == "paper":
        return True
    elif x == "paper" and y == "rock":
        return True
    elif x == "rock" and y == "lizard":
        return True
    elif x == "lizard" and y == "spock":
        return True
    elif x == "spock" and y == "scissors":
        return True
    elif x == "scizzors" and y == "lizard":
        return True
    elif x == "lizard" and y == "paper":
        return True
    elif x == "paper" and y == "spock":
        return True
    elif x == "spock" and y == "rock":
        return True
    elif x == "rock" and y == "scissors":
        return True
    # draw
    elif x == y:
        draws = "True"
        return False
    # computer wins
    else:
        return False
    
# list for percentage function to write the statistics
list = ["rock", "rock", "paper", "paper", "scissors", "scissors", 
        "lizard", "lizard", "spock", "spock", 0, 0, 0]

# function to display percentage
def percentage(i,n):
    # calculate percentage
    percent = str("%.1f"%((i/n)*100))
    # show percentage
    if len(list) > 3:
        if len(list) % 2 != 0:
            print("You chose", list[0], str(i) , "time(s) (" + percent + "%).")
        else:
            print("I chose", list[0], str(i) , "time(s) (" + percent + "%).")
    elif len(list)==3:
        print("You won", str(winDict["user"]) , "round(s) (" + percent + "%).")
    elif len(list)==2:
        print("I won", str(winDict["comp"]) , "round(s) (" + percent + "%).")
    else:
        print("We had", str(winDict["draw"]) , "draw(s) (" + percent + "%). ")
    # remove first element of list
    del list[0]

# for loop for rounds of the game
for i in range(rounds):
    print("\nRound " + str(i+1) + " of " + str(rounds) + ":")
    print("What item do you choose?")
    print("1 - rock\n2 - paper\n3 - scissors\n4 - lizard\n5 - spock")
    # get user answer
    x = input("your answer ==> ")
    # generate random answer for computer
    y = random.choice(choiceList)
    print("I chose:",y)
    # call function to see who wins
    # if beats function return true
    if beats(x,y) and draws == "False":
        print("You win this round!")
        winDict["user"] +=1
    # if beats function return false
    else:
        if draws == "True":
            print("It's a draw!")
            winDict["draw"] +=1
            draws = "False"
        else:
            print("I win this round!")
            winDict["comp"] +=1

print("\nStatistics:")
# call percentage function for statistics
percentage(choiceCounterUser["rock"],rounds)
percentage(choiceCounterComp["rock"], rounds)
percentage(choiceCounterUser["paper"], rounds)
percentage(choiceCounterComp["paper"], rounds)
percentage(choiceCounterUser["scissors"], rounds)
percentage(choiceCounterComp["scissors"], rounds)
percentage(choiceCounterUser["lizard"], rounds)
percentage(choiceCounterComp["lizard"], rounds)
percentage(choiceCounterUser["spock"], rounds)
percentage(choiceCounterComp["spock"], rounds)
percentage(winDict["user"], rounds)
percentage(winDict["comp"], rounds)
percentage(winDict["draw"], rounds)

# compare wins to see who won the game
if winDict["user"]>winDict["comp"] and winDict['user']>=winDict['draw']:
    print("\nYou are the winner!")

elif winDict["user"]<winDict["comp"] and winDict["comp"]>=winDict["draw"]:
    print("\nI am the winner!")

else:
    print("\nThere is no winner.")