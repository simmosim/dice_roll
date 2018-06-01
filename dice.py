import random

def roll():
    num_rolled = random.randint(1, 6)
    return num_rolled

def main():
    rolling = True
    while rolling:
        roll_again = input("Would you like to roll the dice? (Any key for YES / N for NO): ")
        if roll_again.lower() != "n":
            num_rolled = roll()
            print("You rolled a", num_rolled)
        if roll_again.lower() == "n":
            print("Thanks for rolling. See you next time")
            rolling = False
main()
