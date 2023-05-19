import random


print("Enter the choice : \n")
ch = int(input("1.Single player 2.Multiplayer\n"))


if ch == 1:

    choices = ["rock", "paper", "scisors"]

    comp = random.choice(choices)
    pp = 0
    cp = 0

    name = input("Enter the player name ")
    print("\n")
    print("INSTRUCTIONS\nTHE Given choices only be selected .No other choices are allowed.The game is out of 3 .Who scores first 3 points they win\n")

    print("Lets start the game\n")

    while pp < 3 and cp < 3:
        player = input("rock paper scisors  \t").lower()
        comp = random.choice(choices)

        print("Player : ", player)
        print("Computer : ", comp)

        if (player == "rock" and comp == "scisors") or (player == "paper" and comp == "rock") or (player == "scisors" and comp == "paper"):
            print("You got a point ! \U0001f600")
            pp = pp+1
        elif (player == "rock" and comp == "rock") or (player == "paper" and comp == "paper") or (player == "scisors" and comp == "scisors"):
            print("No points")
        elif (player == 'q'):
            break
        elif (player not in choices):
            print("wrong choice")
        else:
            print("Computer got a point")
            cp = cp+1
    print("\nscore board \n")
    print("................\n")
    print("{} : {} \nComputer: {} \n ".format(name, pp, cp))
    if (cp > pp):
        print("You lost")
    elif (cp == pp):
        print("Draw")
    else:
        print("hurray ! {} win \U0001f600".format(name))
else:

    choices = ["rock", "paper", "scisors"]

    f=0
    pp = 0
    cp = 0

    name1 = input("Enter the player 1 name ")
    name2 = input("Enter the player 2 name ")
    print("\n")
    print("INSTRUCTIONS\nTHE Given choices only be selected .No other choices are allowed.The game is out of 3 .Who scores first 3 points they win\n")

    print("Lets start the game\n")

    while pp < 3 and cp < 3:
        print("{} : ".format(name1))
        player = input("rock paper scisors  \t").lower()
        print("{} : ".format(name2))
        

        comp = input("rock paper scisors  \t").lower()


        if (player == "rock" and comp == "scisors") or (player == "paper" and comp == "rock") or (player == "scisors" and comp == "paper"):
            print("{} got a point ! \U0001f600".format(name1))
            pp = pp+1
        elif (player == "rock" and comp == "rock") or (player == "paper" and comp == "paper") or (player == "scisors" and comp == "scisors"):
            print("No points")
        elif player == 'q' :
                print("{} quit the game {} wins  \U0001f600".format(name1,name2))
                f=1
                break
        elif comp == 'q' :
                print("{} quit the game {} wins \U0001f600".format(name2,name1))
                f=1
                break
        elif ((player  not in choices) or (comp not in choices)):
            print("wrong choice")
        else:
            print("{} got a point \U0001f600".format(name2))
            cp = cp+1
   
    print("\nscore board \n")
    print("................\n")
    print("{} : {} \n{}: {} \n ".format(name1, pp,name2, cp))
    if f==0:
        if (cp > pp):
            print("{} wins \U0001f600".format(name2))
        elif (cp == pp):
            print("Draw")
        else:
            print("hurray ! {} win \U0001f600".format(name1))

