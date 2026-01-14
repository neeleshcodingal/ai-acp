import pandas as pd
import time
import sys
from textblob import TextBlob
from colorama import Fore, init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize color output
init(autoreset=True)

# -------------------- DATA LOADING --------------------
def read_movie_data(path="imdb_top_1000.csv"):
    try:
        data = pd.read_csv(path)
        data["text_data"] = data["Genre"].fillna("") + " " + data["Overview"].fillna("")
        return data
    except FileNotFoundError:
        print(Fore.RED + "Dataset not found. Please check the CSV file.")
        sys.exit()

movies = read_movie_data()

# -------------------- TEXT VECTOR SETUP --------------------
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_vectors = vectorizer.fit_transform(movies["text_data"])
similarity_matrix = cosine_similarity(tfidf_vectors)

# -------------------- GENRE EXTRACTION --------------------
def fetch_genres(df):
    genre_set = set()
    for g in df["Genre"].dropna():
        for item in g.split(","):
            genre_set.add(item.strip())
    return sorted(genre_set)

genre_list = fetch_genres(movies)

# -------------------- LOADING EFFECT --------------------
def loading_effect(msg):
    print(Fore.BLUE + msg, end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# -------------------- MOVIE SUGGESTION LOGIC --------------------
def get_movie_suggestions(selected_genre, user_mood=None, min_rating=None, limit=5):
    pool = movies.copy()

    if selected_genre:
        pool = pool[pool["Genre"].str.contains(selected_genre, case=False, na=False)]

    if min_rating:
        pool = pool[pool["IMDB_Rating"] >= min_rating]

    pool = pool.sample(frac=1).reset_index(drop=True)

    suggestions = []
    for _, row in pool.iterrows():
        overview = row["Overview"]
        if pd.isna(overview):
            continue

        mood_score = TextBlob(overview).sentiment.polarity
        suggestions.append((row["Series_Title"], mood_score))

        if len(suggestions) == limit:
            break

    return suggestions if suggestions else None

# -------------------- DISPLAY RESULTS --------------------
def show_results(results, username):
    print(Fore.YELLOW + f"\n🎞 Movie Picks for {username}:\n")
    for i, (movie, score) in enumerate(results, 1):
        mood = "Positive 😊" if score > 0 else "Negative 😞" if score < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}{i}. {movie}  →  {mood} ({score:.2f})")

# -------------------- USER INTERACTION --------------------
def recommendation_flow(user):
    print(Fore.GREEN + "\nAvailable Genres:\n")
    for i, g in enumerate(genre_list, 1):
        print(f"{i}. {g}")

    while True:
        choice = input(Fore.YELLOW + "\nSelect genre (number/name): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(genre_list):
            genre = genre_list[int(choice) - 1]
            break
        elif choice.title() in genre_list:
            genre = choice.title()
            break
        else:
            print(Fore.RED + "Invalid genre. Try again.")

    mood_input = input(Fore.YELLOW + "Describe your current mood: ").strip()
    mood_score = TextBlob(mood_input).sentiment.polarity
    mood_label = "Positive 😊" if mood_score > 0 else "Negative 😞" if mood_score < 0 else "Neutral 😐"
    print(Fore.GREEN + f"Mood detected: {mood_label} ({mood_score:.2f})")

    while True:
        rating_input = input(Fore.YELLOW + "Minimum IMDb rating (7.6–9.3) or skip: ").strip().lower()
        if rating_input == "skip":
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            else:
                print(Fore.RED + "Rating must be between 7.6 and 9.3")
        except ValueError:
            print(Fore.RED + "Enter a valid number.")

    loading_effect("Searching best movies")

    results = get_movie_suggestions(genre, mood_input, rating)
    if not results:
        print(Fore.RED + "No matching movies found.")
        return

    show_results(results, user)

    while True:
        again = input(Fore.YELLOW + "\nWant more suggestions? (yes/no): ").lower()
        if again == "no":
            print(Fore.GREEN + f"\nEnjoy your movies, {user}! 🍿🎬")
            break
        elif again == "yes":
            results = get_movie_suggestions(genre, mood_input, rating)
            show_results(results, user)
        else:
            print(Fore.RED + "Please type yes or no.")

# -------------------- MAIN FUNCTION --------------------
def run_app():
    print(Fore.BLUE + "🎥 Smart Movie Advisor 🎥\n")
    username = input(Fore.YELLOW + "Enter your name: ").strip()
    print(Fore.GREEN + f"\nWelcome, {username}!\n")
    recommendation_flow(username)

if __name__ == "__main__":
    run_app()
