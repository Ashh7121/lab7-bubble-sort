import pygame
import random
import sys

# Config
WIDTH = 800
HEIGHT = 400
BAR_COUNT = 30

COMPARE_DELAY = 60    
SWAP_DELAY = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer (Pygame)")
clock = pygame.time.Clock()


class SortVisualizer:
    def __init__(self):
        self.arr = [random.randint(10, 100) for _ in range(BAR_COUNT)]
        self.bar_width = WIDTH / BAR_COUNT

        self.i = 0
        self.j = 0
        self.swapping = False

        self.last_time = pygame.time.get_ticks()
        self.delay = COMPARE_DELAY

        self.highlight = (-1, -1, "white")  # (index1, index2, color)

    def draw_bars(self):
        screen.fill((0, 0, 0))
        max_val = max(self.arr)

        for i, val in enumerate(self.arr):
            x = i * self.bar_width
            height = (val / max_val) * HEIGHT
            y = HEIGHT - height

            color = (255, 255, 255)

            if i == self.highlight[0] or i == self.highlight[1]:
                if self.highlight[2] == "blue":
                    color = (0, 150, 255)
                elif self.highlight[2] == "red":
                    color = (255, 50, 50)
                elif self.highlight[2] == "cyan":
                    color = (0, 255, 255)
                elif self.highlight[2] == "green":
                    color = (0, 255, 0)

            pygame.draw.rect(screen, color, (x, y, self.bar_width, height))

        pygame.display.flip()

    def step(self):
        now = pygame.time.get_ticks()

        if now - self.last_time < self.delay:
            return

        self.last_time = now

        n = len(self.arr)

        if self.swapping:
            return

        if self.i < n:
            if self.j < n - self.i - 1:
                # Highlight comparison
                self.highlight = (self.j, self.j + 1, "blue")
                self.delay = COMPARE_DELAY

                if self.arr[self.j] > self.arr[self.j + 1]:
                    self.swapping = True
                    self.highlight = (self.j, self.j + 1, "red")
                    pygame.time.set_timer(pygame.USEREVENT, SWAP_DELAY)
                else:
                    self.j += 1
            else:
                self.j = 0
                self.i += 1
        else:
            self.highlight = (-1, -1, "green")

    def handle_swap(self):
        # Perform swap
        self.arr[self.j], self.arr[self.j + 1] = self.arr[self.j + 1], self.arr[self.j]
        self.highlight = (self.j, self.j + 1, "cyan")

        self.j += 1
        self.swapping = False
        pygame.time.set_timer(pygame.USEREVENT, 0)


def main():
    visualizer = SortVisualizer()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.USEREVENT:
                visualizer.handle_swap()

        visualizer.step()
        visualizer.draw_bars()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()