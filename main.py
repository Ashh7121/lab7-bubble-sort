import time
import os


def clear_console():
    """Clear the terminal in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_bubble_state(arr, i, j, swapped):
    """Display the array state for a bubble sort pass.

    TODO: implement in-place redraw by using curses or rich.Live.
    """
    # TODO 1: migrate this to curses redraw buffer for smooth animation.
    # TODO 2: add color highlighting for compared indices i and j, and swapped pair.
    clear_console()
    print(f"Pass: {i}, comparing indices {j} and {j+1}, swapped={swapped}")
    print(' '.join(str(x) for x in arr))


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # sorting

    return arr


def bubble_sort_visual(arr, delay=0.15, use_curses=False):
    """Bubble sort with visualization support.

    This function is a stub to host in-place redraw logic.
    TODO: if use_curses, launch curses window and update frame; else use
    console clear + print currently.
    """
    if use_curses:
        # TODO: implement curses-based rendering for in-place animation.
        # - initialize curses
        # - draw each frame
        # - handle cleanup with curses.endwin()
        raise NotImplementedError('Curses visualization not implemented yet')

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            swapped = False
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print_bubble_state(arr, i, j, swapped)
            time.sleep(delay)

    return arr


if __name__ == '__main__':
    print("Sorted array is: ", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    # TODO: Add an interactive mode or command-line arguments to run bubble_sort_visual().