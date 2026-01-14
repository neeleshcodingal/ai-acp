from colorama import Fore, init
import datetime

init(autoreset=True)

def show_help():
    print(Fore.CYAN + "\nI can:")
    print("- Greet you")
    print("- Tell current time")
    print("- Introduce myself")
    print("- Exit the chat\n")

def hello_ai():
    print(Fore.GREEN + "🤖 Hello! I am HelloAI")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!\n")

    show_help()

    while True:
        user = input(Fore.YELLOW + f"{name}: ").lower()

        if "hello" in user or "hi" in user:
            print(Fore.GREEN + "Hello! Hope you're having a great day 😊")

        elif "time" in user:
            now = datetime.
