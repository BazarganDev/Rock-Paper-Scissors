# Import necessary modules
import pyfiglet
import RockPaperScissors


def show_banner():
    """
    Print out a nice banner.
    """
    banner = pyfiglet.figlet_format("ROCK PAPER SCISSORS")
    print(banner)

def lets_play():
    """
    Ask user if he/she wants to play the game.
    """
    while True:
        is_playing = input("\nWanna play? (y/n) ")
        if is_playing.lower() == 'n':
            print("OK\nBye")
            input("\nPress any key to continue...")
            quit()
        else:
            if is_playing.lower() != 'y':
                print("Invalid input.")
            else:
                break
    
    RockPaperScissors.play()

# Start the program
def Start_Program():
    show_banner()
    lets_play()

Start_Program()