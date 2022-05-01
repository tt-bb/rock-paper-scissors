import random


def user_choice():
    print("\t(Enter the number of your choice)")
    print("\t1. Rock")
    print("\t2. Paper")
    print("\t3. Scissors")
    choice = input("\t> ")
    while choice not in ("1", "2", "3"):
        choice = input("\tEnter the NUMBER of your choice (1-3) > ")
    return int(choice) - 1


def game():
    choices = ["rock", "paper", "scissors"]
    computer = random.randint(0, 2)
    computer = choices[computer]
    user = choices[user_choice()]

    print(f"\n[You chose {user} and the computer chose {computer}]\n")

    if user == computer:
        print("========")
        print("= DRAW =")
        print("========")
    elif user == "rock":
        if computer == "paper":
            print("------------")
            print("- You LOSE -")
            print("------------")
        else:
            print("+++++++++++")
            print("+ You WON +")
            print("+++++++++++")
    elif user == "paper":
        if computer == "rock":
            print("+++++++++++")
            print("+ You WON +")
            print("+++++++++++")
        else:
            print("------------")
            print("- You LOSE -")
            print("------------")
    else:
        if computer == "rock":
            print("------------")
            print("- You LOSE -")
            print("------------")
        else:
            print("+++++++++++")
            print("+ You WON +")
            print("+++++++++++")


def continuation_validation():
    user_continue = "none"
    while user_continue.lower() not in ("true", "t", "false", "f", ""):
        print("\tDo you want to continue ?")
        print("\tt(rue) / f(alse)")
        print("\t\t(default = true)")
        user_continue = input("\t> ")
    if user_continue in ("true", "t", ""):
        return True
    else:
        return False


if __name__ == "__main__":
    print("~~~ ROCK — PAPER —SCISSORS ~~~\n")
    to_play = True
    while to_play:
        game()
        to_play = continuation_validation()
