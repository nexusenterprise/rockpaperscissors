import random

input("welcome to rock paper scissors, press enter to start")

user_score = 0
cpu_score = 0
while True:
    user_choice = input("rock, paper, scissors: ").strip().lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again.")
    else:
        random_num = random.randint(0, 2)
        if random_num == 0:
            cpu_choice = "rock"
        elif random_num == 1:
            cpu_choice = "paper"
        elif random_num == 2:
            cpu_choice = "scissors"

        print()
        print("Your choice:", user_choice)
        print("computer's choice:", cpu_choice)
        print()
        if user_choice == "rock":
            if cpu_choice == "rock":
                print("It's a tie!")
            elif cpu_choice == "paper":
                print("You lost!")
                cpu_score += 1
            elif cpu_choice == "scissors":
                print("You won!")
                user_score += 1
        elif user_choice == "paper":
            if cpu_choice == "paper":
                print("it's a tie!")
            elif cpu_choice == "scissors":
                print("you lost!")
                cpu_score += 1
            elif cpu_choice == "rock":
                print("you won!")
                user_score += 1
        elif user_choice == "scissors":
            if cpu_choice == "scissors":
                print("it's a tie!")
            elif cpu_choice == "rock":
                print("you lost!")
                cpu_score += 1
            elif cpu_choice == "paper":
                print("you won!")
                user_score += 1

    print("You have",user_score,"wins")
    print("The computer has",cpu_score,"wins")
    print()
    repeat = input("Play again? (y/n)").lower()
    while repeat != "n" and repeat != "y":
        repeat = input("Invalid input, please try again: ").lower()
    if repeat == "n":
        break