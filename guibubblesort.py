import tkinter as tk
import random

# Config
WIDTH = 800
HEIGHT = 400
BAR_COUNT = 30

COMPARE_DELAY = 60   # slower comparisons
SWAP_DELAY = 100      # longer pause for swaps


class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bubble Sort Visualizer")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.arr = [random.randint(10, 100) for _ in range(BAR_COUNT)]
        self.bar_width = WIDTH / BAR_COUNT

        self.rects = []
        self.draw_bars()

        self.i = 0
        self.j = 0
        self.swapping = False

        self.root.after(500, self.bubble_step)

    def draw_bars(self):
        self.canvas.delete("all")
        self.rects = []

        max_val = max(self.arr)

        for i, val in enumerate(self.arr):
            x0 = i * self.bar_width
            y0 = HEIGHT - (val / max_val) * HEIGHT
            x1 = (i + 1) * self.bar_width
            y1 = HEIGHT

            rect = self.canvas.create_rectangle(
                x0, y0, x1, y1,
                fill="white",
                outline="black"
            )
            self.rects.append(rect)

    def update_bar(self, index, color="white"):
        val = self.arr[index]
        max_val = max(self.arr)

        x0 = index * self.bar_width
        y0 = HEIGHT - (val / max_val) * HEIGHT
        x1 = (index + 1) * self.bar_width
        y1 = HEIGHT

        self.canvas.coords(self.rects[index], x0, y0, x1, y1)
        self.canvas.itemconfig(self.rects[index], fill=color)

    def swap_animation(self, j):
        """Make swap very obvious: red → pause → swap → update"""
        # Step 1: highlight in red
        self.update_bar(j, "red")
        self.update_bar(j + 1, "red")

        def do_swap():
            # Step 2: swap values
            self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

            # Step 3: update bars visually
            self.update_bar(j, "cyan")
            self.update_bar(j + 1, "cyan")

            # Step 4: reset after short delay
            self.root.after(SWAP_DELAY, lambda: self.reset_after_swap(j))

        self.root.after(SWAP_DELAY, do_swap)

    def reset_after_swap(self, j):
        self.update_bar(j, "white")
        self.update_bar(j + 1, "white")

        self.j += 1
        self.swapping = False
        self.root.after(COMPARE_DELAY, self.bubble_step)

    def bubble_step(self):
        if self.swapping:
            return

        n = len(self.arr)

        if self.i < n:
            if self.j < n - self.i - 1:
                self.update_bar(self.j, "blue")
                self.update_bar(self.j + 1, "blue")

                if self.arr[self.j] > self.arr[self.j + 1]:
                    self.swapping = True
                    self.swap_animation(self.j)
                else:
                    # Reset if no swap
                    self.root.after(
                        COMPARE_DELAY,
                        lambda: self.reset_no_swap()
                    )
            else:
                self.j = 0
                self.i += 1
                self.root.after(COMPARE_DELAY, self.bubble_step)

        else:
            self.finish()

    def reset_no_swap(self):
        self.update_bar(self.j, "white")
        self.update_bar(self.j + 1, "white")
        self.j += 1
        self.root.after(COMPARE_DELAY, self.bubble_step)

    def finish(self):
        for i in range(len(self.arr)):
            self.update_bar(i, "lime")


if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()
