import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import math
import series 

pygame.init()
screen = pygame.display.set_mode()
w, h = screen.get_size()
h_ = 20000
surface = pygame.Surface((w, h_))
pygame.display.set_caption("Convergence Test")

x_slider = Slider(screen, w-300, h-300, 200, 40, min=0, max=500, step=1, initial=100)
y_slider = Slider(screen, w-300, h-200, 200, 40, min=0, max=500, step=1, initial=100)
x_output = TextBox(screen, w-400, h-300, 50, 50, fontSize=20)
y_output = TextBox(screen, w-400, h-200, 50, 50, fontSize=20)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def zeta(s, n):
    return 1 / n**s

def dirichlet_eta(s, n):
    return (-1)**(n+1) / n**s

def modified_eta_even(s, n):
    return (-1)**(n+1) / (2*n)**s

def modified_eta_odd(s, n):
    return (-1)**(n+1) / (2*n-1)**s

scroll_y = 0
scroll_sensitivity = 100
n = 100

#basel = sum.Sum(surface, lambda n: 1/n**2, lambda n: (6*n)**0.5, math.pi)
basel = series.Series(surface, 'sum', lambda n: zeta(2, n), math.pi**2/6)
madhava_leibnitz = series.Series(surface, 'sum', lambda n: (-1)**(n-1)/(2*n-1), math.pi/4)
zeta4 = series.Series(surface, 'sum', lambda n: zeta(4, n), math.pi**4 / 90)
ramanujan_sato_1 = series.Series(surface, 'sum', lambda n: factorial(4*(n-1)) * (1103 + 26390 * (n-1))/ (factorial(n-1)**4 * 396**(4*(n-1))), 9801/(8**0.5 * math.pi))
wallis = series.Series(surface, 'product', lambda n: 4*n**2/(4*n**2 - 1), math.pi/2)
dirichlet_eta_1 = series.Series(surface, 'sum', lambda n: dirichlet_eta(2, n), math.pi**2/12)
H_2 = series.Series(surface, 'sum', lambda n: modified_eta_even(2, n), math.pi**2/48)
H_3 = series.Series(surface, 'sum', lambda n: modified_eta_odd(3, n), math.pi**3/32)

zeta2_button = Button(screen, 50, h-550, 100, 50, text="Zeta(2)", fontSize=10, margin=20, inactiveColour=basel.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: basel.toggle_on_off())
zeta4_button = Button(screen, 50, h-500, 100, 50, text="Zeta(4)", fontSize=10, margin=20, inactiveColour=zeta4.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: zeta4.toggle_on_off())
ml_button = Button(screen, 50, h-450, 100, 50, text="Madhava-Leibnitz", fontSize=10, margin=20, inactiveColour=madhava_leibnitz.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: madhava_leibnitz.toggle_on_off())
wallis_button = Button(screen, 50, h-400, 100, 50, text="Wallis", fontSize=10, margin=20, inactiveColour=wallis.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: wallis.toggle_on_off())
rs_button = Button(screen, 50, h-350, 100, 50, text="Ramanujan-Sato", fontSize=10, margin=20, inactiveColour=ramanujan_sato_1.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: ramanujan_sato_1.toggle_on_off())
de1_button = Button(screen, 50, h-300, 100, 50, text="eta(2)", fontSize=10, margin=20, inactiveColour=dirichlet_eta_1.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: dirichlet_eta_1.toggle_on_off())
h2_button = Button(screen, 50, h-250, 100, 50, text="H(2)", fontSize=10, margin=20, inactiveColour=H_2.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: H_2.toggle_on_off())
h3_button = Button(screen, 50, h-200, 100, 50, text="H(3)", fontSize=10, margin=20, inactiveColour=H_3.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: H_3.toggle_on_off())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            scroll_y += event.y * scroll_sensitivity
        elif event.type == pygame.QUIT:
            running = False
        

    screen.fill((255, 255, 255))
    surface.fill((255, 255, 255))

    pygame.draw.line(surface, (0, 0, 0), (w/2, 0), (w/2, h_), 5)

    zeta4.reset()
    madhava_leibnitz.reset()
    basel.reset()
    ramanujan_sato_1.reset()
    wallis.reset()
    dirichlet_eta_1.reset()
    H_2.reset()
    H_3.reset()
    for i in range(1, n):
        zeta4.compute()
        basel.compute()
        madhava_leibnitz.compute()
        ramanujan_sato_1.compute()
        wallis.compute()
        dirichlet_eta_1.compute()
        H_2.compute()
        H_3.compute()

        zeta4.draw((x_slider, y_slider))
        basel.draw((x_slider, y_slider))
        madhava_leibnitz.draw((x_slider, y_slider))
        ramanujan_sato_1.draw((x_slider, y_slider))
        wallis.draw((x_slider, y_slider))
        dirichlet_eta_1.draw((x_slider, y_slider))
        H_2.draw((x_slider, y_slider))
        H_3.draw((x_slider, y_slider))

    y_output.setText(y_slider.getValue())
    x_output.setText(x_slider.getValue())

    screen.blit(surface, (0, scroll_y))
    pygame_widgets.update(event)
    pygame.display.update()
pygame.quit()