import random

# Global score variables
user_score = 0
computer_score = 0
ties = 0

def play():
    """Function to play a single round of Rock-Paper-Scissors."""
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    while user not in ['r', 'p', 's']:
        user = input("Invalid input! Please enter 'r', 'p', or 's': ").lower()
    
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")

    if user == computer:
        return "tie"
    elif is_win(user, computer):
        return "win"
    else:
        return "lose"

def is_win(player, opponent):
    """Checks if the player has won."""
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def update_score(result):
    """Updates the score based on the result."""
    global user_score, computer_score, ties  # Use global variables
    
    if result == "win":
        user_score += 1
    elif result == "lose":
        computer_score += 1
    else:
        ties += 1  # When it's a tie

def display_score():
    """Displays the current scoreboard."""
    print("\nThe Scoreboard:")
    print(f"User: {user_score}, Computer: {computer_score}, Ties: {ties}\n")


for i in range(5):
    result = play()  
    update_score(result)  
    display_score()  
