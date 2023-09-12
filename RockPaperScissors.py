# Import necessary modules
import random


# Initialize the random number generator.
random.seed()

# Play the game
def play():
    """
    This function contains the logic of the game.
    """
    # Available elements of the game.
    r = "rock"
    p = "paper"
    s = "scissors"
    available_options = (r, p, s)
    # Get the user's selected element.
    while True:
        user_element = input("\nSelect an element (Rock, Paper, Scissors): ").lower()
        if user_element in available_options:
            break
        else:
            print("Please select an element.")
            continue
    # Get the computer's selected element.
    pc_element = random.choice(available_options)
    # Define the logic if the game.
    # User = Computer => Draw
    # Rock > Scissors, Paper > Rock, Scissors > Paper => Win
    # Other than that => Lose
    if user_element == pc_element:
        print("\nUser: ", user_element.title())
        print("Computer: ", pc_element.title())
        print("\nDraw")
        input("\nPress any key to continue...")
    elif (user_element == r and pc_element == s) or (user_element == p and pc_element == r) or (user_element == s and pc_element == p):
        print("\nUser: ", user_element.title())
        print("Computer: ", pc_element.title())
        print("\nUser Won")
        print("Computer Lost")
        input("\nPress any key to continue...")
    elif (pc_element == r and user_element == s) or (pc_element == p and user_element == r) or (pc_element == s and user_element == p):
        print("\nUser: ", user_element.title())
        print("Computer: ", pc_element.title())
        print("\nUser Won")
        print("Computer Lost")
        input("\nPress any key to continue...")

# In case if "you" want to open this module on its own.
if __name__ == "__main__":
    play()