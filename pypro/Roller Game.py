import random

collector = []  # Initialize empty list

def roller(roll):
    if roll == "Y":
        v = random.randint(1, 6)
        print(f"The dice rolled to {v}")
        return v  # Return the rolled value
    else:
        print("Your chance is over")
        return None  # Return None if not rolling

# Keep rolling until the user says "N"
while True:
    roll = input("Do you need to roll? (Y/N): ").strip().upper()  # Normalize input
    
    if roll == "N":
        print("Game Over!")
        break  # Exit the loop

    rolled_value = roller(roll)  # Call the function
    
    if rolled_value is not None:
        collector.append(rolled_value)  # Append valid roll to the list

print("Collected rolls:", collector)  # Display collected values
