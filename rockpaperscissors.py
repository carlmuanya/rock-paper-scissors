import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    #Logical statements for rock
    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "rock" and computer_pick == "paper":
        computer_wins += 1
        print("You lost! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "rock" and computer_pick == "rock":
        print("It was a draw! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    #Logical statements for paper
    if user_input == "paper" and computer_pick == "scissors":
        computer_wins += 1
        print("You lost! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "paper" and computer_pick == "paper":
        print("It was a draw! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    #Logical statements for scissors
    if user_input == "scissors" and computer_pick == "scissors":
        print("It was a draw! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

    if user_input == "scissors" and computer_pick == "rock":
        computer_wins += 1
        print("You lost! |", "User wins = ", user_wins, "Computer wins = ", computer_wins)

print("Goodbye!")
