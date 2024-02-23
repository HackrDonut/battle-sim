from sys import exit
from os import system
import battle

while True:
    print("Welcome to My Text-Based Battle Simulator!")

    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("\n>> ")

    if choice == "1":
        battle.start()
    elif choice == "2":
        print("Load game")
    elif choice == "3":
        print("Goodbye.")
        exit(0)
    input("Press ENTER to continue.\n>> ")
    system("cls")