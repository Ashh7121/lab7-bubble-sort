import random
import time
import os

def clear():
    # Clear terminal (works on Windows & Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_array(arr, highlight_index=None):
    for i, val in enumerate(arr):
        bar = '█' * val
        if i == highlight_index:
            print(f"\033[91m{bar}\033[0m")  # Red highlight
        else:
            print(bar)
    print("\n")

def bubble_sort_visual(arr, delay=0.1):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            clear()
            print_array(arr, j)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            time.sleep(delay)

    # Final display
    clear()
    print_array(arr)
    print("Sorted!")

if __name__ == "__main__":
    size = 20
    arr = [random.randint(1, 20) for _ in range(size)]

    bubble_sort_visual(arr, delay=0.05)