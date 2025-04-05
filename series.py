import pygame
import random
from pygame_widgets.button import Button
from colours import colours, col_index

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
            pygame.draw.circle(self.screen, self.col, (self.screen.get_size()[0]/2 + (self.res - self.expected)/(self.expected) * 100 * slider[0].getValue(), 10 + (self.n-1) * slider[1].getValue()), 5)

    def toggle_on_off(self):
        self.toggle = not self.toggle
