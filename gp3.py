import random

choiceList = ["rock", "paper", "scissors", "lizard", "spock"]
choiceCounterUser = {"rock":0, "paper":0, "scissors":0, "lizard":0, "spock":0}
choiceCounterComp = {"rock":0, "paper":0, "scissors":0, "lizard":0, "spock":0}
winDictionary = {"user":0, "comp":0, "draw":0}

print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
rounds = int(input("How many rounds do you want to play? ==> "))

def beats(x,y):
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

    choiceCounterUser[x] +=1
    choiceCounterComp[y] +=1
    if x == "scissors":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "paper" and y == "rock":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "rock" and y == "lizard":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "lizard" and y == "spock":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "spock" and y == "scissors":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "scizzors" and y == "lizard":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "lizard" and y == "paper":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "paper" and y == "spock":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "spock" and y == "rock":
        winDictionary["user"] +=1
        return "You win this round!"
    elif x == "rock" and y == "scissors":
        winDictionary["user"] +=1
        return "You win this round!"
        # draw
    elif x == y:
        winDictionary["draw"] += 1
        return "It's a draw!"
    else:
        winDictionary["comp"] += 1
        return "I win this round!"
    
list = ["rock", "rock", "paper", "paper", "scissors", "scissors", "lizard", "lizard", "spock", "spock", 0, 0, 0]

def percentage(i,n):
    percent = str("%.1f"%((i/n)*100))
    if len(list) != 3:
        if len(list) % 2 == 0:
            print("You chose " + list[0]+ " " + str(i) + " time(s) " + percent + "%.")
        else:
            print("I chose " + list[0]+ " " + str(i) + " time(s) " + percent + "%.")
    else:
        print("You won " + str(winDictionary["user"]) + " time(s) " + percent + "%. ")


    del list[0]
for i in range(rounds):
   print("Round " + str(i+1) + " of " + str(rounds) + ":")
   print("What item do you choose?")
   print("1 - rock\n2 - paper\n3 - scissors\n4 - lizard\n5 - spock")
   x = input("Your answer ==> ")
   y = random.choice(choiceList)
   print(beats(x,y))


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
percentage(winDictionary["user"], rounds)