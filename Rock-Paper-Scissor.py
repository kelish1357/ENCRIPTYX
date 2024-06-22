import random

print("Let's play Rock-Paper-Scissors!")

while True:
    userchoice = input("Enter rock, paper, or scissors: ").lower()

    if userchoice not in ["rock", "paper", "scissors"]:
        print("Wrong input! Please enter rock, paper, or scissors.")
        continue

    computerchoice = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {userchoice}")
    print(f"Computer chose: {computerchoice}")

    if userchoice == computerchoice:
        print("It's a tie!")
    elif (userchoice == "rock" and computerchoice == "scissors") or \
         (userchoice == "scissors" and computerchoice == "paper") or \
         (userchoice == "paper" and computerchoice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    playagain = input("\nPlay again? (yes/no): ")
    if playagain.lower()!= "yes":
        break