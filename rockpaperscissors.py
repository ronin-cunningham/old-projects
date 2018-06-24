
import random

choices = ["rock", 'paper', 'scissors']




def playainput():
    while True:
        playerinput = input("Input rock, paper, or scissors:   ")
        if playerinput in choices:
            print ("you chose", playerinput)
            break



        print ("oops try again: ")
    return playerinput
        
            





def choose(x):
    choice = random.choice(x)
    print ("I chose %s" %choice)
    return choice

x = playainput()
y = choose(choices)


outcomes = {
    ("rock", "rock"): "Tie!",
    ("rock", "paper"): "you lose",
    ("rock", "scissors"): "you win",
    ("paper", "rock"): "you win",
    ("paper", "paper"): "tie!",
    ("paper", "scissors"): "you lose",
    ("scissors", "rock"): "you lose",
    ("scissors", "paper"): "you win",
    ("scissors", "scissors"): "tie!",
}
print(outcomes[x, y])
