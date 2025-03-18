import json
from datetime import datetime
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

genres = [
    "Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", 
    "Documentary", "Drama", "Family", "Fantasy", "Historical", "Horror", 
    "Musical", "Mystery", "Romance", "Sci-Fi", "Sports", "Thriller", 
    "War", "Western", "Superhero", "Noir", "Experimental", "Silent", 
    "Indie", "Coming-of-Age"
]

class Movies:
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

class Review:
    def __init__(self, reviewer_name, comment, rating):
        self.reviewer_name = reviewer_name
        self.comment = comment
        self.rating = rating

class MovieCollection:
    def __init__(self, filename="movies.json"):
        self.filename = filename
        self.movies = self.load_movies()

    def load_movies(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                movies = []
                for movie in data:
                    movie_obj = Movies(movie["title"], movie["genre"], movie["year"])
                    for review in movie.get("reviews", []):
                        movie_obj.add_review(Review(**review))
                    movies.append(movie_obj)
                return movies
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_movies(self):
        with open(self.filename, "w") as file:
            json.dump([
                {
                    "title": movie.title,
                    "genre": movie.genre,
                    "year": movie.year,
                    "reviews": [
                        {
                            "reviewer_name": review.reviewer_name,
                            "comment": review.comment,
                            "rating": review.rating
                        }
                        for review in movie.reviews
                    ]
                }
                for movie in self.movies
            ], file, indent=4)

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_movies()

    def add_review(self, movie_title, review):
        for movie in self.movies:
            if movie.title.lower() == movie_title.lower():
                movie.add_review(review)
                self.save_movies()
                print(f"{Fore.GREEN}Review added for '{movie.title}'{Style.RESET_ALL}")
                return
        print(f"{Fore.RED}Movie not found.{Style.RESET_ALL}")

    def view_movies(self, page=1, per_page=10):
        clear_screen()
        print(f"{Fore.CYAN}{'No.':<5}{'Title':<35}{'Year':<8}{'Genre'}{Style.RESET_ALL}")
        for i, movie in enumerate(self.movies, start=1):
            print(f"{Fore.YELLOW}{str(i):<5}{Style.RESET_ALL}{movie.title:<35}{movie.year:<8}{movie.genre}")


    def display_movie_details(self, selected_movie):
        print(f"\n{Fore.CYAN}Title:{Style.RESET_ALL} {selected_movie.title}")
        print(f"{Fore.CYAN}Genre:{Style.RESET_ALL} {selected_movie.genre}")
        print(f"{Fore.CYAN}Year:{Style.RESET_ALL} {selected_movie.year}")
        if selected_movie.reviews:
            total_rating = sum(review.rating for review in selected_movie.reviews)
            average_rating = total_rating / len(selected_movie.reviews)

            # Assign Emoji Based on Average Rating
            if average_rating >= 3.5:
                emoji = "😊"
            elif average_rating >= 2.5:
                emoji = "😐"
            else:
                emoji = "😞"

            print(f"{Fore.CYAN}Average Rating:{Style.RESET_ALL} {average_rating:.1f} {emoji}")
        else:
            print(f"{Fore.CYAN}Average Rating:{Style.RESET_ALL} No reviews yet.")

        print(f"\n{Fore.CYAN}Reviews:{Style.RESET_ALL}")
        if selected_movie.reviews:
            for review in selected_movie.reviews:
                print(f" - {Fore.GREEN}{review.reviewer_name}:{Style.RESET_ALL} {review.comment} {Fore.YELLOW}(Rating: {review.rating}){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No reviews yet.{Style.RESET_ALL}")

        input("\nPress enter when done...")

def main_menu():
    while True:
        clear_screen()
        print(f"\n{Fore.MAGENTA}{'-' * 15} Rotten Mangoes {'-' * 15}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1. Add Movie{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Review a Movie{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Show All Movies{Style.RESET_ALL}")
        print(f"{Fore.CYAN}4. Exit{Style.RESET_ALL}")
        try:
            choice = int(input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}"))

            match choice:
                case 1:
                    clear_screen()
                    print(f"\n{Fore.MAGENTA}{'-' * 15} Rotten Mangoes - Add a Movie {'-' * 15}{Style.RESET_ALL}")
                    while True:
                        try:
                            title = input(f"{Fore.YELLOW}Enter movie name: {Style.RESET_ALL}")
                            year = int(input(f"{Fore.YELLOW}Enter release year: {Style.RESET_ALL}"))

                            if any(movie.title == title and movie.year == year for movie in RottenMangoes.movies):
                                print(f"{Fore.RED}A movie title in that year already exists.{Style.RESET_ALL}")
                                confirmation = input(f"{Fore.YELLOW}Add anyway (Y/N): {Style.RESET_ALL}")
                                match confirmation:
                                    case "Y":
                                        break
                                    case "N":
                                        continue
                                    case _:
                                        print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
                            break
                        except ValueError:
                            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")

                    while True:
                        try:
                            genre = input(f"{Fore.YELLOW}Enter movie genre: {Style.RESET_ALL}")
                            if genre in genres:
                                break
                            else:
                                print(f"{Fore.RED}Invalid genre!{Style.RESET_ALL}")
                        except ValueError:
                            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")

                    new_movie = Movies(title, genre, year)
                    RottenMangoes.add_movie(new_movie)

                case 2:
                    clear_screen()
                    print(f"\n{Fore.MAGENTA}{'-' * 15} Rotten Mangoes - Review a Movie {'-' * 15}{Style.RESET_ALL}")
                    RottenMangoes.view_movies()
                    while True:
                        try:
                            selection = int(input(f"{Fore.YELLOW}Select a movie number to review: {Style.RESET_ALL}"))
                            if selection > len(RottenMangoes.movies):
                                print(f"{Fore.RED}Selection does not exist{Style.RESET_ALL}")
                            else:
                                selection = RottenMangoes.movies[selection - 1].title
                                clear_screen()
                                break
                        except ValueError:
                            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")

                    print(f"{Fore.MAGENTA}{'-' * 15} Rotten Mangoes - Reviewing {selection} {'-' * 15}{Style.RESET_ALL}")
                    while True:
                        try:
                            name = input(f"{Fore.YELLOW}Enter your reviewer name: {Style.RESET_ALL}")
                            if name.strip() == "":
                                name = "Anonymous"
                                break
                            else:
                                break
                        except ValueError:
                            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")

                    while True:
                        try:
                            rating = int(input(f"{Fore.YELLOW}Rating of the movie (1-5): {Style.RESET_ALL}"))
                            if not (1 <= rating <= 5):
                                print(f"{Fore.RED}Invalid rating! 1-5 only!{Style.RESET_ALL}")
                            else:
                                break
                        except ValueError:
                            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")

                    while True:
                        try:
                            comment = input(f"{Fore.YELLOW}Enter your comment: {Style.RESET_ALL}")
                            break
                        except ValueError:
                            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")

                    new_review = Review(name, comment, rating)
                    RottenMangoes.add_review(selection, new_review)
                    
                case 3:
                    clear_screen()
                    print(f"\n{Fore.MAGENTA}{'-' * 15} Rotten Mangoes - Movie Details {'-' * 15}{Style.RESET_ALL}")
                    RottenMangoes.view_movies()

                    while True:
                        try:
                            selection = int(input(f"{Fore.YELLOW}Select a movie number to view details: {Style.RESET_ALL}"))
                            if selection < 1 or selection > len(RottenMangoes.movies):
                                print(f"{Fore.RED}Selection does not exist.{Style.RESET_ALL}")
                            else:
                                clear_screen()
                                selected_movie = RottenMangoes.movies[selection - 1]
                                RottenMangoes.display_movie_details(selected_movie)
                                break
                        except ValueError:
                            print(f"{Fore.RED}Invalid Input! Please enter a number.{Style.RESET_ALL}")
                case 4:
                    exit()
                case _:
                    print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")


RottenMangoes = MovieCollection()
main_menu()