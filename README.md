# Bubble Sort Visualizer

A visual interactive application that demonstrates the **Bubble Sort** algorithm using Python and tkinter. Watch in real-time as bars rise and swap positions while the algorithm sorts an array of random integers.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Code Architecture](#code-architecture)
- [Understanding the Algorithm](#understanding-the-algorithm)

---

## Overview

This project provides a **GUI-based visualization** of the Bubble Sort algorithm. Instead of just printing array states to the console, the visualizer displays:

- Animated bars of varying heights representing array elements
- Color-coded status indicators for bars (comparing, swapping, sorted)
- Step-by-step animation showing comparisons and swaps
- A complete sort from start to finish with automatic animation

Perfect for learning how sorting algorithms work, this tool makes the abstract concept of bubble sort concrete and easy to follow.

---

## Features

✨ **Real-time Visualization**: Watch bars move and change colors as the algorithm progresses

🎨 **Color-Coded States**:
- **White**: Default state (unsorted)
- **Blue**: Currently being compared
- **Red**: About to be swapped
- **Cyan**: Recently swapped
- **Lime**: Sorted (final state)

⏱️ **Configurable Speed**: Adjust comparison and swap delays to slow down or speed up the animation

📊 **Customizable Array**: Change the number of bars and range of values easily

🔄 **Automatic Animation**: Press start and watch the full sorting process automatically

---

## Requirements

- Python 3.7 or higher
- tkinter (usually included with Python, but may need separate installation on Linux)

### Install tkinter (if needed):

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
tkinter comes bundled with Python by default.

---

## Installation

1. **Clone or download the repository:**
```bash
cd lab7-bubble-sort
```

2. **Verify Python is installed:**
```bash
python --version
```

3. **Run the visualizer:**
```bash
python guibubblesort.py
```

---

## Usage

1. **Launch the application:**
   ```bash
   python guibubblesort.py
   ```

2. **The GUI window opens** showing:
   - A black canvas with colored bars
   - Bars auto-animate as the bubble sort runs
   - The animation starts automatically with random bar heights

3. **Watch the sorting process:**
   - Bars light up in **blue** when being compared
   - Bars turn **red** when about to swap
   - Bars turn **cyan** after swapping
   - All bars turn **lime** when the sort is complete

4. **Interrupt** (close the window) to stop the visualization at any time

---

## How It Works

### Bubble Sort Algorithm

Bubble Sort is a simple comparison-based sorting algorithm that:

1. **Compares adjacent elements** in the array
2. **Swaps them if they're in the wrong order** (left > right)
3. **Repeats until no more swaps are needed**

**Time Complexity:** O(n²) in average and worst cases

**Space Complexity:** O(1) — sorts in-place

### Visual Process

```
Initial:  [64, 34, 25, 12, 22, 11, 90]
Pass 1:   Compares (64,34) → swaps → (34,64,25,12,22,11,90)
          Compares (64,25) → swaps → (34,25,64,12,22,11,90)
          ... continues until 90 is in correct position

Pass 2:   Repeats with remaining unsorted portion
...
Final:    [11, 12, 22, 25, 34, 64, 90]  (sorted!)
```

---

## Configuration

Edit the constants at the top of `guibubblesort.py` to customize the visualization:

```python
WIDTH = 800              # Canvas width in pixels
HEIGHT = 400             # Canvas height in pixels
BAR_COUNT = 30           # Number of bars to sort
COMPARE_DELAY = 60       # Milliseconds between comparisons
SWAP_DELAY = 100         # Milliseconds for swap animation
```

### Speed Control

- **Increase `COMPARE_DELAY` and `SWAP_DELAY`** to slow down the animation (better for learning)
- **Decrease them** to speed up (better for demonstration)
- **Values in milliseconds** (e.g., 100 = 0.1 seconds)

### Array Customization

- **`BAR_COUNT`**: Modify to sort more or fewer bars (try 10 for slow, 50 for fast)
- **Random range**: Change `random.randint(10, 100)` in the `__init__` method to adjust bar heights

---

## Project Structure

```
lab7-bubble-sort/
├── guibubblesort.py       # Main GUI visualizer (run this)
├── main.py                # Original console-based bubble sort
├── test_main.py           # Basic tests for bubble sort
├── twodimensional.py      # Alternative implementation or extension
├── README.md              # This file
├── JOURNAL.md             # Development log
├── REPORT.md              # Project report
├── prompts_history.md     # Chat/prompt history
└── .github/               # GitHub workflow and config files
```

---

## Code Architecture

### Main Class: `SortVisualizer`

The core of the visualizer is the `SortVisualizer` class, which manages:

#### Initialization (`__init__`)
- Creates the tkinter window and canvas
- Generates a random array of integers
- Initializes sorting state variables (`i`, `j`, `swapping`)
- Starts the animation loop with `root.after(500, self.bubble_step)`

#### Key Methods

| Method | Purpose |
|--------|---------|
| `draw_bars()` | Draws all bars on canvas with white fill |
| `update_bar(index, color)` | Updates a single bar's height and color |
| `swap_animation(j)` | Animates the swap of two adjacent bars |
| `reset_after_swap(j)` | Resets colors after swap, increments `j` |
| `bubble_step()` | Main loop—compares, swaps, progresses algorithm |
| `reset_no_swap()` | Handles non-swap comparisons |
| `finish()` | Colors all bars lime when sort is complete |

#### Animation Flow

```
bubble_step() checks if arr[j] > arr[j+1]
    ↓
Yes → swap_animation(j):
    1. Color both bars RED
    2. Wait SWAP_DELAY ms
    3. Perform swap in array
    4. Color both bars CYAN
    5. Color both bars WHITE (reset)
    6. Increment j, loop
    
No → reset_no_swap():
    1. Color bars WHITE
    2. Increment j, loop
```

#### State Management

The visualizer tracks:
- **`i`**: Pass number (outer loop)
- **`j`**: Current pair index (inner loop)
- **`swapping`**: Boolean flag to prevent overlapping animations
- **`arr`**: The array being sorted
- **`rects`**: Canvas rectangle IDs for efficient updates

---

## Understanding the Algorithm

### Step-by-Step Example

Given array: `[3, 1, 2]`

**Pass 1 (i=0):**
- Compare j=0: (3 > 1)? YES → swap → [1, 3, 2]
- Compare j=1: (3 > 2)? YES → swap → [1, 2, 3]

**Pass 2 (i=1):**
- Compare j=0: (1 > 2)? NO → [1, 2, 3]

**Pass 3 (i=2):**
- No comparisons needed (sorted)

**Result: [1, 2, 3]** ✓

### Key Insights

1. **After each pass**, the largest unsorted element "bubbles" to the end
2. **Inner loop range**: `n - i - 1` avoids checking already-sorted elements
3. **Early termination possible**: Could optimize by tracking if any swaps occurred
4. **Stability**: Bubble Sort is a stable algorithm (equal elements maintain relative order)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Window won't open | Ensure tkinter is installed (`python -m tkinter` to test) |
| Animation too fast | Increase `COMPARE_DELAY` and `SWAP_DELAY` values |
| Animation too slow | Decrease delay values or reduce `BAR_COUNT` |
| Bars not visible | Check that `WIDTH` and `HEIGHT` are set appropriately |
| Python not found | Ensure Python is in your PATH; use `python3` on some systems |

---

## Learning Outcomes

After using this visualizer, you should understand:

✓ How bubble sort compares adjacent elements

✓ Why swaps occur and when they happen

✓ The concept of "passes" through the array

✓ Why bubble sort is O(n²) — nested loops over array

✓ How to visualize abstract algorithms concretely

✓ Basic tkinter GUI development with canvas drawing and animation

---

## Extensions & Ideas

Consider enhancing this project with:

- **Step-by-step control**: Add "Next Step" button to manually progress
- **Algorithm comparison**: Visualize multiple sorts side-by-side (Quick Sort, Merge Sort, etc.)
- **Statistics**: Display comparison count, swap count, and execution time
- **User input**: Allow users to input their own array or load data from a file
- **Sound**: Add audio feedback for comparisons and swaps
- **Export**: Save animation frames as video or GIF

---

## License

This project is for educational purposes. Feel free to modify and share it.

---

## Questions?

Refer to the inline code comments in `guibubblesort.py` for detailed explanations, or consult the `JOURNAL.md` for development notes.

Happy sorting! 🎨📊
