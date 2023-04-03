import pygame as pg
import math
import random
import numpy as np

class random:
    def __init__(floor, ceil):
        self.floor = floor
        self.ceil = ceil
        self.seed = random.randint()

    def get(input_vec: tuple):
        seed = 0
        
        for index, element in enumerate(input_vec):
            seed += element * (10 ** (index + 1))

        return (((7237 * (seed * self.seed)) % 103) % (self.ceil - self.floor)) + self.floor

class noise:
    def __init__(height, levels):
        self.height = height
        self.levels = levels
        self.seed = time.time()
        self.maps = []
        for i in range(levels):
            self.maps.append(random(height * ((i + 1) / levels)))

def main():

    screen = pg.display.set_mode((750, 500))

    running = true

    draw_noise()

    while running:

        events = pg.event.get()

        for event in events:
            if event.type == 32787:
                running = False

    return 0

if __name__ == "__main__":
    print(np.random.seed(123))