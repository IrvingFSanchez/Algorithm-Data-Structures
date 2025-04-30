# Name: Irving F Sanchez
# Course: Algorithm and Data Structures SP25-CPSC-34000-002
# School: Lewis University, Romeoville, IL
# Purpose: Compare the performance of Bubble Sort and Quick Sort using different real-world datasets of varying sizes.

'''Note: I put a ton of comments in my code for personal use. I add notes to help me understand what
I'm doing and why I'm doing it. I'm not sure if this is a good practice or not, but I'm doing it for now.'''


import pandas as pd
import random
import time
import matplotlib.pyplot as plt


#==================== START OF DATA LOADING FUNCTIONS ====================#
def load_pokemon(field):
    df = pd.read_csv('Pokemon.csv')
    return df[field].dropna().tolist()

def load_tokens(field):
    df = pd.read_csv('tokens.csv')
    return df[field].dropna().tolist()

def load_games(field):
    df = pd.read_csv('games.csv')
    return df[field].dropna().tolist()
#===================== END OF DATA LOADING FUNCTIONS =====================#

#==================== START OF DATA MANIPULATION FUNCTIONS ====================#
def almost_sorted(data, fraction=0.05):
    data.sort()
    n_swaps = int(len(data) * fraction)
    for _ in range(n_swaps):
        idx1 = random.randint(0, len(data) - 1)
        idx2 = random.randint(0, len(data) - 1)
        data[idx1], data[idx2] = data[idx2], data[idx1]
    return data
#===================== END OF DATA MANIPULATION FUNCTIONS =====================#

#==================== START OF SORTING ALGORITHMS ====================#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
#===================== END OF SORTING ALGORITHMS =====================#

#==================== START OF TIMING FUNCTION ====================#
def time_sort(sort_func, data):
    start = time.perf_counter()
    result = sort_func(data.copy())
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
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

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            valid_fields = ['Name', 'Total', 'HP']
            field = get_valid_field("Sort Pokemon by", valid_fields)
            pokemon_data = load_pokemon(field)
            prepare_and_sort(pokemon_data, field)
        elif choice == '2':
            valid_fields = ['artist', 'name', 'colorIdentity']
            field = get_valid_field("Sort MTG Tokens by", valid_fields)
            token_data = load_tokens(field)
            prepare_and_sort(token_data, field)
        elif choice == '3':
            valid_fields = ['title', 'rating', 'userscore']
            field = get_valid_field("Sort Video Games by", valid_fields)
            games_data = load_games(field)
            prepare_and_sort(games_data, field)
        elif choice == '4':
            show_definitions()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
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
def prepare_and_sort(data, label):
    while True:
        print("\nDo you want to:")
        print("1. Randomize the data")
        print("2. Make it almost sorted")
        option = input("Enter choice (1-2): ").strip()

        if option == '1':
            random.shuffle(data)
            break
        elif option == '2':
            data = almost_sorted(data)
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

    print("\nTiming Bubble Sort and Quick Sort...")

    bubble_times = []
    quick_times = []

    for i in range(5):
        bubble_times.append(time_sort(bubble_sort, data))
        quick_times.append(time_sort(quick_sort, data))

    print("\nRun Times (ms):")
    for i in range(5):
        print(f"Run {i+1}: Bubble Sort = {bubble_times[i]:.2f}, Quick Sort = {quick_times[i]:.2f}")

    plot_all_runs(bubble_times, quick_times, label, len(data))
#===================== END OF SORTING AND TIMING PREPARATION =====================#

#==================== START OF GRAPHING FUNCTION ====================#
def plot_all_runs(bubble_times, quick_times, label, dataset_size):
    runs = list(range(1, 6))
    avg_bubble = sum(bubble_times) / len(bubble_times)
    avg_quick = sum(quick_times) / len(quick_times)

    plt.plot(runs, bubble_times, marker='o', label='Bubble Sort', color='red')
    plt.plot(runs, quick_times, marker='o', label='Quick Sort', color='green')

    for i, t in enumerate(bubble_times):
        plt.text(runs[i], t + 2, f"{t:.1f} ms", color='red', ha='center')
    for i, t in enumerate(quick_times):
        plt.text(runs[i], t - 2, f"{t:.1f} ms", color='green', ha='center')

    plt.axhline(avg_bubble, color='red', linestyle='--', linewidth=1, label=f'Avg Bubble: {avg_bubble:.2f} ms')
    plt.axhline(avg_quick, color='green', linestyle='--', linewidth=1, label=f'Avg Quick: {avg_quick:.2f} ms')

    plt.xlabel('Run Number')
    plt.ylabel('Time (ms)')
    plt.title(f'Sorting Times over 5 Runs ({label}, Size: {dataset_size})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
#===================== END OF GRAPHING FUNCTION =====================#


if __name__ == "__main__":
    main_menu()

