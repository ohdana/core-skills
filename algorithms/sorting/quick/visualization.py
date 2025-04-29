import pygame
from random import randint, shuffle

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
CLOCK_TICK = 60
MIN_BAR_HEIGHT, MAX_BAR_HEIGHT = 1, WINDOW_HEIGHT
BAR_WIDTH = 20
N_OF_BARS = WINDOW_WIDTH // BAR_WIDTH

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Quick Sort')
        self.clock = pygame.time.Clock()
        self.generate_numbers()
        self.is_running = True
        self.is_sorted = False
    
    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    
            self.visualize()
            
        pygame.quit()
        exit()
    
    def visualize(self):
        self.draw_bars()
        if not self.is_sorted:
            shuffle(self.numbers)
            self.sort(self.numbers, 0, len(self.numbers) - 1)
            self.is_sorted = True

    def sort(self, array, left, right):
        if right <= left: return
        j = self.partititon(array, left, right)
        self.sort(array, left, j - 1)
        self.sort(array, j + 1, right)

    def partititon(self, array, left, right):
        i = left + 1
        j = right
        partitioning_item = array[left]
        while True:
            while array[i] < partitioning_item:
                if i == right: break
                i += 1
            while partitioning_item < array[j]:
                if j == left: break
                j -= 1

            if i >= j: break
            array[i], array[j] = array[j], array[i]
            self.draw_bars()

        array[left], array[j] = array[j], array[left]
        self.draw_bars()

        return j
    
    def draw_bars(self):
        self.display_surface.fill('black')
        self.generate_bars()
        for bar in self.bars:
            pygame.draw.rect(self.display_surface, 'white', bar)
        pygame.display.update()
        self.clock.tick(CLOCK_TICK)
        
    def generate_bars(self):
        self.bars = []
        for i, height in enumerate(self.numbers):
            pos_x = BAR_WIDTH * i
            pos_y = WINDOW_HEIGHT - height
            self.bars.append(pygame.Rect((pos_x, pos_y), (BAR_WIDTH, height)))
            
    def generate_numbers(self):
        self.numbers = [randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for i in range(N_OF_BARS)]
        
if __name__ == '__main__':
    main = Main()
    main.run()