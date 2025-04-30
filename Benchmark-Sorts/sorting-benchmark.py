# Name: Irving F Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Compare the performance of Bubble Sort and Quick Sort using different real-world datasets of varying sizes.

'''Note: I put a ton of comments in my code for personal use. I add notes to help me understand what
I'm doing and why I'm doing it. I'm not sure if this is a good practice or not, but I'm doing it for now.'''

# Benchmark Sorts Project Skeleton

import pandas as pd              # This import is for loading/manipulating CSV data, and necessary for the pandas library
import random                    # This import is for shuffling data and generating almost-sorted datasets
import time                      # This import is for measuring sort execution time
import matplotlib.pyplot as plt  # This import is for plotting performance results, and necessary to visualize the data

#==================== START OF DATA LOADING FUNCTIONS ====================#
def load_pokemon(field):
    df = pd.read_csv('Pokemon.csv')     # Load Pokémon dataset
    return df[field].dropna().tolist()  # Extract specified column, drop missing values, convert to list

def load_tokens(field):
    df = pd.read_csv('tokens.csv')      # Load MTG tokens dataset
    return df[field].dropna().tolist()

def load_games(field):
    df = pd.read_csv('games.csv')       # Load video games dataset
    return df[field].dropna().tolist()
#===================== END OF DATA LOADING FUNCTIONS =====================#

#==================== START OF DATA MANIPULATION FUNCTIONS ====================#
def almost_sorted(data, fraction=0.05):
    data.sort()                         # Sort the data first
    n_swaps = int(len(data) * fraction) # Calculate swaps (5% of data size by default)
    for _ in range(n_swaps):
        idx1 = random.randint(0, len(data) - 1) # Random index 1 means a random number between 0 and the length of the data - 1
                                                # This is to ensure that the random number is within the bounds of the data list
        idx2 = random.randint(0, len(data) - 1) 
        data[idx1], data[idx2] = data[idx2], data[idx1]  # Randomly swap elements
    return data
#===================== END OF DATA MANIPULATION FUNCTIONS =====================#

#==================== START OF SORTING ALGORITHMS ====================#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):                       # Outer loop: passes through the list
        for j in range(0, n-i-1):            # Inner loop: compare adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if out of order

def quick_sort(arr):
    if len(arr) <= 1:                        # Base case: already sorted
        return arr
    pivot = arr[len(arr) // 2]               # Choose middle element as pivot
    left = [x for x in arr if x < pivot]     # Elements < pivot
    middle = [x for x in arr if x == pivot]  # Elements == pivot
    right = [x for x in arr if x > pivot]    # Elements > pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort sublists
#===================== END OF SORTING ALGORITHMS =====================#

#==================== START OF TIMING FUNCTION ====================#
def time_sort(sort_func, data):
    start = time.perf_counter()        
    result = sort_func(data.copy())    # Sort a copy to avoid modifying original data
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000  # Convert seconds to milliseconds
    return elapsed_ms
#===================== END OF TIMING FUNCTION =====================#

#==================== START OF DEFINITIONS DISPLAY ====================#
def show_definitions():
    import textwrap
    wrapper = textwrap.TextWrapper(width=80)

    print("\nDefinitions:")

    print("\nBubble Sort:")
    bubble_def = ("Bubble Sort is a simple sorting algorithm that repeatedly steps through the "
                "list, compares adjacent elements, and swaps them if they are in the wrong order. "
                "This process continues until no swaps are needed.")
    print(wrapper.fill(bubble_def))

    print("\nQuick Sort:")
    quick_def = ("Quick Sort is a divide-and-conquer algorithm. It selects a 'pivot' element from the "
                "array and partitions the other elements into two sub-arrays, according to whether "
                "they are less than or greater than the pivot. The sub-arrays are then sorted recursively.")
    print(wrapper.fill(quick_def))
#===================== END OF DEFINITIONS DISPLAY =====================#

#==================== START OF USER MENU ====================#
def main_menu():
    while True:
        print("\nWelcome! Which dataset would you like to sort?")
        print("1. Pokemon Data (Small ~1k)")
        print("2. MTG Token Data (Medium ~5k)")
        print("3. Video Games Data (Large ~10k)")
        print("4. Definitions")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            valid_fields = ['Name', 'Total', 'HP']
            field = get_valid_field("\nSort Pokemon by", valid_fields)
            pokemon_data = load_pokemon(field)
            prepare_and_sort(pokemon_data, field, "Pokemon", field)
        elif choice == '2':
            valid_fields = ['artist', 'name', 'colorIdentity']
            field = get_valid_field("\nSort MTG Tokens by", valid_fields)
            token_data = load_tokens(field)
            prepare_and_sort(token_data, field, "MTG_Tokens", field)
        elif choice == '3':
            valid_fields = ['title', 'rating', 'userscore']
            field = get_valid_field("\nSort Video Games by", valid_fields)
            games_data = load_games(field)
            prepare_and_sort(games_data, field, "Games", field)
        elif choice == '4':
            show_definitions()
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
#===================== END OF USER MENU =====================#

#==================== START OF FIELD VALIDATION ====================#
def get_valid_field(prompt, valid_fields):
    while True:
        print(f"{prompt}: {', '.join(valid_fields)}")
        field = input("Enter your choice: ").strip()
        if field in valid_fields:
            return field
        else:
            print("Invalid choice. Please choose a valid field.")
#===================== END OF FIELD VALIDATION =====================#

#==================== START OF SORTING AND TIMING PREPARATION ====================#
def prepare_and_sort(data, label, dataset_name, field_name):
    is_numeric = all(isinstance(x, (int, float)) for x in data)

    while True:
        print("\nDo you want to:")
        print("1. Randomize the data")
        print("2. Make it almost sorted")
        option = input("\nEnter choice (1-2): ").strip()

        if option == '1':
            random.shuffle(data)
            break
        elif option == '2':
            data = almost_sorted(data)
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

    # Sort the data for consistent comparison
    data.sort(key=lambda x: float(x) if is_numeric else str(x).lower())

    # Save data option with dynamic filename
    save_choice = input("\nWould you like to save a copy of the dataset being sorted? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = f"{dataset_name}_{field_name}_sorted_data.txt"  # e.g., "Pokemon_Name_sorted_data.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for item in data:
                f.write(f"{item}\n")  # Write each item on a new line
        print(f"\nData saved to '{filename}'")
    else:
        print(f"Sample data to be sorted ({label}):")
        for item in data[:10]:
            print(f" - {item}")
        print("...")

    print("\nTiming Bubble Sort and Quick Sort...")

    bubble_times = []
    quick_times = []

    for i in range(5):
        bubble_times.append(time_sort(bubble_sort, data.copy()))  # Ensure fresh copy
        quick_times.append(time_sort(quick_sort, data.copy()))

    print("\nRun Times (ms):")
    for i in range(5):
        print(f"Run {i+1}: Bubble Sort: {bubble_times[i]:.2f} ms | Quick Sort: {quick_times[i]:.2f} ms")

    plot_all_runs(bubble_times, quick_times, label, len(data))
#===================== END OF SORTING AND TIMING PREPARATION =====================#

#==================== START OF GRAPHING FUNCTION ====================#
def plot_all_runs(bubble_times, quick_times, label, dataset_size):
    # Create a list of run numbers [1, 2, 3, 4, 5]
    runs = list(range(1, 6))
    # Calculate the average time for each sorting algorithm
    avg_bubble = sum(bubble_times) / len(bubble_times)
    avg_quick = sum(quick_times) / len(quick_times)
    # Plot the bubble sort times with red dots
    plt.plot(runs, bubble_times, marker='o', label='Bubble Sort', color='red')
    # Plot the quick sort times with green dots
    plt.plot(runs, quick_times, marker='o', label='Quick Sort', color='green')
    # Add red text labels above each Bubble Sort data point
    for i, t in enumerate(bubble_times):
        plt.text(runs[i], t + 2, f"{t:.1f} ms", color='red', ha='center')
    # Add green text labels below each Quick Sort data point
    for i, t in enumerate(quick_times):
        plt.text(runs[i], t - 2, f"{t:.1f} ms", color='green', ha='center')
    # Draw a dashed horizontal red line for Bubble Sort average
    plt.axhline(avg_bubble, color='red', linestyle='--', linewidth=1,
                label=f'Avg Bubble: {avg_bubble:.2f} ms')
    # Draw a dashed horizontal green line for Quick Sort average
    plt.axhline(avg_quick, color='green', linestyle='--', linewidth=1,
                label=f'Avg Quick: {avg_quick:.2f} ms')
    # Label the x-axis and y-axis
    plt.xlabel('Run Number')
    plt.ylabel('Time (ms)')
    # Title includes what was sorted and the dataset size
    plt.title(f'Sorting Times over 5 Runs ({label}, Size: {dataset_size})')
    # Display legend showing which line is which
    plt.legend()
    # Enable a background grid for easier reading
    plt.grid(True)
    # Adjust spacing so everything fits cleanly
    plt.tight_layout()
    # Show the plot window
    plt.show()
#===================== END OF GRAPHING FUNCTION =====================#

if __name__ == "__main__":
    main_menu()

