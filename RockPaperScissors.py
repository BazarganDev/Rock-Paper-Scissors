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
        selected_option = input("\nPick an element (Rock, Paper, Scissors)\n-> ")
        if selected_option.lower() not in available_options:
            print("Please pick up an element.")
            continue
        else:
            break
    user_element = selected_option
    # Get the computer's selected element.
    pc_element = random.choice(available_options)
    # Define the logic if the game.
    # User = Computer => Draw
    # Rock > Scissors, Paper > Rock, Scissors > Paper => Win
    # Other than that => Lose
    if user_element == pc_element:
        print(f"User: {user_element}")
        print(f"Computer: {pc_element}")
        print("\nDraw")
        input("\nPress any key to continue...")
    elif (
        user_element == r and pc_element == s or
        user_element == p and pc_element == r or
        user_element == s and pc_element == p
        ):
        print(f"User: {user_element}")
        print(f"Computer: {pc_element}")
        print("\nUser won!!!")
        print("Computer lost!!!")
        input("\nPress any key to continue...")
    else:
        print(f"User: {user_element}")
        print(f"Computer: {pc_element}")
        print("\nUser lost!!!")
        print("Computer won!!!")
        input("\nPress any key to continue...")

# In case if you want to open this module on its own.
if __name__ == "__main__":
    play()