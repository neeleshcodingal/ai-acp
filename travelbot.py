import re
import random
from colorama import Fore, init

init(autoreset=True)

# Travel data
places = {
    "beach": ["bali", "maldives", "phuket", "miami", "bondi beach"],
    "mountain": ["himalayas", "andes", "rocky mountains", "swiss alps"],
    "city": ["new york", "paris", "tokyo", "london", "sydney"]
}

jokes_list = [
    "Why did the programmer quit traveling? Too many bugs!",
    "Why was the laptop cold on vacation? It left its Windows open!",
    "Why do travelers love Wi-Fi? Because roaming is expensive!"
]

weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy", "Foggy"]


# Utility function
def clean_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())


# Recommendation feature
def suggest_places():
    print("Available categories: beach / mountain / city")
    category = clean_text(input("Choose a category: "))

    if category in places:
        destination = random.choice(places[category])
        print(Fore.GREEN + "Recommended destination: " +
              Fore.YELLOW + destination.title())
    else:
        print(Fore.RED + "Sorry, that category is not available.")


# Joke feature
def tell_joke():
    choice = clean_text(input("Do you want to hear a joke? (yes/no): "))
    if choice == "yes":
        print(Fore.GREEN + random.choice(jokes_list))
    else:
        print(Fore.RED + "Alright, maybe later!")


# Weather feature
def show_weather():
    choice = clean_text(input("Check today's weather? (yes/no): "))
    if choice == "yes":
        print(Fore.GREEN + "Today's weather is: " +
              Fore.YELLOW + random.choice(weather_conditions))
    else:
        print(Fore.RED + "Okay, skipping weather update.")


# Help menu
def show_help():
    print(Fore.CYAN + "\nI can help you with:")
    print("- Travel recommendations (type 'recommend')")
    print("- Tell a joke (type 'joke')")
    print("- Weather update (type 'weather')")
    print("- Help menu (type 'help')")
    print("- Exit chat (type 'exit' or 'bye')\n")


# Main chatbot loop
def start_chat():
    print(Fore.CYAN + "Hello! I'm TravelMate 🤖")
    user_name = input("What's your name? ")
    print(f"Nice to meet you, {user_name}!\n")

    show_help()

    while True:
        user_input = clean_text(input(Fore.YELLOW + f"{user_name}: "))

        if "recommend" in user_input:
            suggest_places()
        elif "joke" in user_input:
            tell_joke()
        elif "weather" in user_input:
            show_weather()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelMate: Safe travels! Goodbye 👋")
            break
        else:
            print(Fore.RED + "Sorry, I didn't understand that.")


# Run program
if __name__ == "__main__":
    start_chat()
