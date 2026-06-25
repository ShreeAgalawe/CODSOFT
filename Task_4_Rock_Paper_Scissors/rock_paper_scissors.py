import random

def get_user_choice():
    # Prompt the user to choose rock, paper, or scissors [cite: 56]
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("\nChoose rock, paper, or scissors: ").lower().strip()
        if user_input in valid_choices:
            return user_input
        print("Invalid input. Please check your spelling and try again.")

def get_computer_choice():
    # Generate a random choice for the computer [cite: 57, 58]
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    # Determine the winner based on standard logic [cite: 59]
    if user == computer:
        return "tie"
    # Rock beats scissors, scissors beat paper, and paper beats rock [cite: 60]
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    print("--- Rock, Paper, Scissors ---")
    # Keep track of the user's and computer's scores 
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display the user's choice and the computer's choice [cite: 60]
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        winner = determine_winner(user_choice, computer_choice)

        # Display the result, whether the user wins, loses, or it's a tie [cite: 61]
        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print(f"Scoreboard -> You: {user_score} | Computer: {computer_score}")

        # Ask the user if they want to play another round [cite: 63]
        play_again = input("\nPlay another round? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\n--- Final Score ---")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()