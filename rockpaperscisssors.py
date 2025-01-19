import random

def display_choices(user_choice, computer_choice):
    print(f"\nYour choice: {user_choice.lower()}")
    print(f"Computer's choice: {computer_choice.lower()}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def rock_paper_scissors():
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to end the game.")

    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter your choice: ").lower()
        if user_choice == "exit":
            print("\nThank you for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()