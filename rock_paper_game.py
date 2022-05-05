import random

while True:
    choices = ["rock", "paper", "seasor"]
    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input("rock, paper or seasor? :").lower()

    # if player.isalpha():   #you can also use this

    print("Computer choice:", computer)
    print("player choice:", player)
    if computer == player:
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        if computer == "seasor":
            print("You win!")

    elif player == "seasor":
        if computer == "rock":
            print("You lose!")
        if computer == "paper":
            print("You win!")

    elif player == "paper":
        if computer == "seasor":
            print("You lose!")
        if computer == "rock":
            print("You win!")

    play_again = input("play again(yes/no): ").lower()
    if play_again != "yes":
        break
print("bye!")
