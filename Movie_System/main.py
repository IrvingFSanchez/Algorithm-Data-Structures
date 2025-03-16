# Name: Irving F Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Implement recursive directory traversal and a menu system for movie recommendations.

import os
import pyfiglet  # Import pyfiglet for title banner
from colorama import Fore, Style  # Import colorama for colored text
from deque import Deque  # Import the Deque class
from movie import MovingPicture

''' /*---+---+---+--Start of ErrorManagement Class Block---+---+---+--*/ '''

class ErrorManagement:
    
    ''' Here this class will manage errors while directory traversing just covering my back '''

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == PermissionError:
            print("[Permission Denied!] Recken you don't have permission to access this directory. Sorry Chum.")
            return True
        elif exc_type == FileNotFoundError:
            print("[Invalid Path!] Recken the path you entered is invalid. Sorry Chum.")
            return True
        return False

''' /*---+---+---+--End of ErrorManagement Class Block---+---+---+--*/ '''

''' /*---+---+---+--Start of Traversal Function Block---+---+---+--*/ '''

def explore_speakeasy(speakeasy_path, film_deque):
    
    with ErrorManagement():
        for item in os.listdir(speakeasy_path):
            joint_path = os.path.join(speakeasy_path, item)
            
            if os.path.isfile(joint_path) and item.endswith(".txt"):
                try:
                    with open(joint_path, "r") as file:
                        lines = file.readlines()
                        
                        # Extract data from lines
                        title = lines[0].strip().split(": ")[1]
                        year = int(lines[1].strip().split(": ")[1])
                        genre = lines[2].strip().split(": ")[1]
                        rating = float(lines[3].strip().split(": ")[1])
                        
                        # Create a MovingPicture object and add it to the deque
                        flick = MovingPicture(title, year, genre, rating)
                        film_deque.append(flick)
                        print(f"Loaded: {flick}")  # Print confirmation
                except (ValueError, IndexError) as e:
                    print(f"[Error] This file's got a screw loose: {joint_path}. Skipping...")
                    print(f"Details: {e}")
            
            elif os.path.isdir(joint_path):
                # Recursively explore sub-speakeasies
                explore_speakeasy(joint_path, film_deque)

''' /*---+---+---+--End of Traversal Function Block---+---+---+--*/ '''

''' /*---+---+---+--Start of Menu Functions Block---+---+---+--*/ '''

def list_all_movies(film_deque, color):
    """
    List all movies in the deque.
    """
    print(f"\n{color}Loaded Moving Pictures:{Style.RESET_ALL}")
    print(f"{color}{'-' * 70}{Style.RESET_ALL}")
    for flick in sorted(film_deque, key=lambda x: x.title):
        print(f"{color}{flick.title:<30} ({flick.year}) - {flick.genre:<20} - Rating: {flick.rating:>4.1f}{Style.RESET_ALL}")

def recommend_movie(film_deque, color):
    """
    Recommend a movie based on the rules of the deque (FIFO for a queue).
    """
    if not film_deque.is_empty():
        flick = film_deque.popleft()
        print(f"\n{color}Recommended Movie: {flick}{Style.RESET_ALL}")
        film_deque.append(flick)  # Add it back to the end of the deque
    else:
        print(f"\n{color}No movies available to recommend. The speakeasy is dry!{Style.RESET_ALL}")

def autocomplete_movie_title(film_deque, partial_title):
    """
    Return a list of movie titles that match the partial title.
    """
    partial_title = partial_title.lower()
    return [flick.title for flick in film_deque if partial_title in flick.title.lower()]

def search_movie_by_title(film_deque, color):
    """
    Search for a movie by title with autocomplete suggestions.
    """
    while True:
        partial_title = input(f"\n{color}Enter the title of the movie you're looking for (or 'q' to quit): {Style.RESET_ALL}").strip().lower()
        
        if partial_title == 'q':
            print(f"\n{color}Alright, back to the main menu!{Style.RESET_ALL}")
            break
        
        # Get autocomplete suggestions
        suggestions = autocomplete_movie_title(film_deque, partial_title)
        
        if not suggestions:
            print(f"\n{color}No movies found with '{partial_title}'. Try again!{Style.RESET_ALL}")
            continue
        
        # Display suggestions
        print(f"\n{color}Suggestions:{Style.RESET_ALL}")
        for i, title in enumerate(suggestions, 1):
            print(f"{color}{i}. {title}{Style.RESET_ALL}")
        
        # Ask the user to select a movie
        try:
            choice = int(input(f"\n{color}Enter the number of the movie you want to see (or 0 to keep typing): {Style.RESET_ALL}"))
            if choice == 0:
                continue
            elif 1 <= choice <= len(suggestions):
                selected_title = suggestions[choice - 1]
                for flick in film_deque:
                    if flick.title.lower() == selected_title.lower():
                        print(f"\n{color}Found: {flick}{Style.RESET_ALL}")
                        return
            else:
                print(f"\n{color}Invalid choice. Try again!{Style.RESET_ALL}")
        except ValueError:
            print(f"\n{color}Invalid input. Please enter a number.{Style.RESET_ALL}")

def recommend_top_3_movies(film_deque, color):
    """
    Recommend the top 3 movies by rating, and allow the user to see the next 3 until they stop.
    """
    if len(film_deque) < 3:
        print(f"\n{color}Not enough movies to recommend a top 3. The speakeasy needs more flix!{Style.RESET_ALL}")
        return
    
    # Sort all movies by rating in descending order
    sorted_movies = sorted(film_deque, key=lambda x: x.rating, reverse=True)
    
    start_index = 0
    while True:
        # Get the next 3 movies
        next_3_movies = sorted_movies[start_index:start_index + 3]
        
        if not next_3_movies:
            print(f"\n{color}No more movies to recommend. You've reached the end of the line, old sport!{Style.RESET_ALL}")
            break
        
        # Display the next 3 movies
        print(f"\n{color}Top Movies by Rating:{Style.RESET_ALL}")
        for flick in next_3_movies:
            print(f"{color}{flick}{Style.RESET_ALL}")
        
        # Ask the user if they want to see the next 3
        choice = input(f"\n{color}Would you like to see the next 3 movies? (yes/no): {Style.RESET_ALL}").strip().lower()
        if choice not in ('yes', 'y'):
            print(f"\n{color}Alright, back to the main menu!{Style.RESET_ALL}")
            break
        
        # Move to the next set of 3 movies
        start_index += 3

''' /*---+---+---+--End of Menu Functions Block---+---+---+--*/ '''

''' /*---+---+---+--Start of Main Function Block---+---+---+--*/ '''

def main():
    # Display title banner
    title_banner = pyfiglet.figlet_format("Movie Library", font="big")
    
    # Creating a border of asterisks around title
    border = "*" * (len(title_banner.splitlines()[0]) + 4) # Adjusting border length to match banner width
    
    print()
    print(Fore.RED + border + Style.RESET_ALL) # Print border in white
    print(Fore.BLUE + Style.BRIGHT + f"{title_banner}" + Style.RESET_ALL) # Print title banner in blue
    print(Fore.WHITE + border + Style.RESET_ALL) # Print border in white

    print(Fore.MAGENTA + "\nWelcome to the Movie Recommendation System!\n" + Style.RESET_ALL)
    
    film_deque = Deque()  # Create a Deque to store movies
    
    while True:
        speakeasy_path = input(Fore.MAGENTA + "\nEnter the (directory) you want to explore movie-flix! " + Style.RESET_ALL)
        
        if os.path.exists(speakeasy_path):
            print(Fore.MAGENTA + f"\nExploring directory: {speakeasy_path}\n" + Style.RESET_ALL)
            explore_speakeasy(speakeasy_path, film_deque)
            print(Fore.MAGENTA + f"\nFinished loading. Total moving picture flix loaded: {len(film_deque)}" + Style.RESET_ALL)
            break
        else:
            print("[Invalid Path] This speakeasy don't exist, old sport. Try again.")
    
    # Main menu loop
    while True:
        print(Fore.MAGENTA + "\nMain Menu:" + Style.RESET_ALL)
        print(Fore.GREEN + "1. List all movies" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Recommend a movie" + Style.RESET_ALL)
        print(Fore.BLUE + "3. Search for a movie by title" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Recommend Top 3 movies by rating" + Style.RESET_ALL)
        print(Fore.RED + "5. Exit" + Style.RESET_ALL)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            list_all_movies(film_deque, Fore.GREEN)
        elif choice == "2":
            recommend_movie(film_deque, Fore.YELLOW)
        elif choice == "3":
            search_movie_by_title(film_deque, Fore.BLUE)
        elif choice == "4":
            recommend_top_3_movies(film_deque, Fore.CYAN)
        elif choice == "5":
            print(Fore.RED + "\nThanks for visiting the Speakeasy Movie Library System! Catch you on the flip side!\n" + Style.RESET_ALL)
            break
        else:
            print("\nInvalid choice, old sport. Try again!")

''' /*---+---+---+--End of Main Function Block---+---+---+--*/ '''

''' /*---+---+---+--Start of Main Execution Block---+---+---+--*/ '''

if __name__ == "__main__":
    main()
    
''' /*---+---+---+--End of Main Execution Block---+---+---+--*/ '''

# NOTE: speakeasy means path in this context it's a 1920s terminology
# flix = movies in this context it's a 1920s terminology
# old sport = friend in this context it's a 1920s terminology
# chum = friend in this context it's a 1920s terminology
# screw loose = something is wrong in this context it's a 1920s terminology
# dry = empty in this context it's a 1920s terminology


'''Out of all of the ADT's none of them had an advantage over the other. They all had their own unique features that made them useful in their own way. But Deque
does allow for more flexibility in terms of adding and removing elements from the front and back of the list. It also allows for more flexibility in terms of
iterating through the list and allows me to add more features in the future that would benefit from deque'''