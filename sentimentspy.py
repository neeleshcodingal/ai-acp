from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment = "Negative 😞"
        color = Fore.RED
    else:
        sentiment = "Neutral 😐"
        color = Fore.YELLOW

    print(color + f"\nSentiment: {sentiment}")
    print(color + f"Polarity Score: {polarity:.2f}")

def main():
    print(Fore.CYAN + "🔍 Welcome to SentimentSpy 🔍")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input(Fore.YELLOW + "Enter a sentence: ").strip()

        if user_input.lower() == "exit":
            print(Fore.CYAN + "Thank you for using SentimentSpy 👋")
            break

        analyze_sentiment(user_input)

if __name__ == "__main__":
    main()
