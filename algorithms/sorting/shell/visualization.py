import pygame
from random import randint

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
CLOCK_TICK = 60
MIN_BAR_HEIGHT, MAX_BAR_HEIGHT = 1, WINDOW_HEIGHT
BAR_WIDTH = 20
N_OF_BARS = WINDOW_WIDTH // BAR_WIDTH

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Insertion Sort')
        self.clock = pygame.time.Clock()
        self.generate_numbers()
        self.is_running = True
    
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
        n = len(self.numbers)
        h = 1
        while h < n // 3: h = 3 * h + 1
        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and self.numbers[j] < self.numbers[j - h]:
                    self.numbers[j], self.numbers[j - h] = self.numbers[j - h], self.numbers[j]
                    self.draw_bars()
                    j -= h
            h //= 3
    
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