import pygame
import random
from pygame_widgets.button import Button

colours = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 165, 0),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (165, 42, 42),
    (255, 192, 203),
    (50, 205, 50),
    (0, 128, 128),
    (0, 0, 128),
    (128, 128, 0),
    (128, 0, 0),
    (128, 128, 128),
    (192, 192, 192),
    (255, 215, 0),
    (75, 0, 130),
    (238, 130, 238),
]

col_index = 0
class Series:
    def __init__(self, screen, series_type, f, expected):
        global col_index
        self.f = f
        self.type = series_type
        self.expected = expected
        self.n = 1
        if self.type == 'product':
            self.res = 1
        else:
            self.res = 0
        self.toggle = True
        self.screen = screen
        self.col = colours[col_index]
        col_index += 1
    
    def compute(self):
        if self.type == 'sum':
            self.res += self.f(self.n)
        elif self.type == 'product':
            self.res *= self.f(self.n)
        elif self.type == 'continued-fraction':
            pass
        elif self.type == 'asymptotic-approximation':
            pass
        self.n += 1

    def reset(self):
        if self.type == 'product':
            self.res = 1
        else:
            self.res = 0
        self.n = 1

    def draw(self, slider):
        if self.toggle:
            pygame.draw.circle(self.screen, self.col, (self.screen.get_size()[0]/2 + (self.res - self.expected) * 10 * slider[0].getValue(), 10 + (self.n-1) * slider[1].getValue()), 5)

    def toggle_on_off(self):
        self.toggle = not self.toggle
