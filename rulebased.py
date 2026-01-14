import datetime
from colorama import Fore, init

init(autoreset=True)

def show_menu():
    print(Fore.CYAN + "\nI can help you with:")
    print("- Greetings (hello / hi)")
    print("- Tell current time")
    print("- Tell today's date")
    print("- Introduce myself")
    print("- Exit the chat\n")

def rule_bot():
    print(Fore.GREEN + "🤖 Hello! I am RuleBot")
    name = input("What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_menu()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print(Fore.GREEN + "Hello! Hope you're doing well 😊")

        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(Fore.GREEN + f"Current time is {current_time}")

        elif "date" in user_input:
            today = datetime.datetime.now().strftime("%d-%m-%Y")
            print(Fore.GREEN + f"Today's date is {today}")

        elif "who are you" in user_input:
            print(Fore.GREEN + "I am RuleBot, a simple rule-based chatbot.")

        elif "help" in user_input:
            show_menu()

        elif "bye" in user_input or "exit" in user_input:
            print(Fore.GREEN + "Goodbye! Have a great day 👋")
            break

        else:
            print(Fore.RED + "Sorry, I didn't understand that.")

if __name__ == "__main__":
    rule_bot()
