from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("\nRock, Paper, Scissors?\t")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    
    player = False
    computer = t[randint(0,2)]

# Output

#Rock, Paper, Scissors? rock
#That's not a valid play. Check your spelling!

#Rock, Paper, Scissors? Rock
#Tie!

#Rock, Paper, Scissors? Paper
#You lose! Scissors cut Paper

#Rock, Paper, Scissors? Rock
#You lose! Paper covers Rock

#Rock, Paper, Scissors? Scissors
#Tie!

#Rock, Paper, Scissors? Rock
#You win! Rock smashes Scissors
