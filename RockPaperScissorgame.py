import random

options=("rock", "paper", "scissors")

name=input("Enter your name:")
print("\n")
print(f"Hello {name}, Welcome to the game\n")

player= None

computer= random.choice(options)
# computer="rock"
player=input("Enter your choice(rock, paper, scissors):")
print("\n")

print(f"The palyer chooses {player}")
print("\n")

print(f"The computer chooses {computer}")

print("\n")

if (player=="rock" and computer=="scissors") or():
    print("Player wins")
elif (player=="scissors" and computer=="paper"):
    print("Player wins")
elif (player=="paper" and computer=="rock"):
    print( "Player wins")
elif (player== computer):
    print("Its a tie")
else:
    print("Computer wins")

    
    
