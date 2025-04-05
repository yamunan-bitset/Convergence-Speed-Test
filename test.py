import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import math
import series 
from analytic_fn import *

pygame.init()
screen = pygame.display.set_mode()
w, h = screen.get_size()
h_ = 20000
surface = pygame.Surface((w, h_))
pygame.display.set_caption("Convergence Test")

x_slider = Slider(screen, w-300, h-300, 200, 40, min=0, max=1000, step=1, initial=100)
y_slider = Slider(screen, w-300, h-200, 200, 40, min=0, max=500, step=1, initial=100)
zeta_value = Slider(screen, w-300, h-400, 200, 40, min=2, max=50, step=2, initial=2)
eta_value = Slider(screen, w-300, h-500, 200, 40, min=2, max=50, step=2, initial=2)
x_output = TextBox(screen, w-400, h-300, 50, 50, fontSize=20)
y_output = TextBox(screen, w-400, h-200, 50, 50, fontSize=20)
zeta_output = TextBox(screen, w-400, h-400, 50, 50, fontSize=10)
eta_output = TextBox(screen, w-400, h-500, 50, 50, fontSize=10)

scroll_y = 0
scroll_sensitivity = 100
n = 100

madhava_leibnitz = series.Series(surface, 'sum', lambda n: (-1)**(n-1)/(2*n-1), math.pi/4)
ramanujan_sato_1 = series.Series(surface, 'sum', lambda n: factorial(4*(n-1)) * (1103 + 26390 * (n-1))/ (factorial(n-1)**4 * 396**(4*(n-1))), 9801/(8**0.5 * math.pi))
wallis = series.Series(surface, 'product', lambda n: 4*n**2/(4*n**2 - 1), math.pi/2)
dirichlet_eta_1 = series.Series(surface, 'sum', lambda n: dirichlet_eta(2, n), math.pi**2/12)
zeta_fn = series.Series(surface, 'sum', lambda n: zeta(2, n), math.pi**2/6)
nilakantha_h_1 = series.Series(surface, 'sum', lambda n: modified_eta_odd(1, n), math.pi**2/12)
odd_h = series.Series(surface, 'sum', lambda n: modified_eta_odd(3, n), math.pi**3/32)

zeta_button = Button(screen, 50, h-500, 100, 50, text="Zeta(s)", fontSize=10, margin=20, inactiveColour=zeta_fn.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: zeta_fn.toggle_on_off())
ml_button = Button(screen, 50, h-450, 100, 50, text="Madhava-Leibnitz", fontSize=10, margin=20, inactiveColour=madhava_leibnitz.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: madhava_leibnitz.toggle_on_off())
wallis_button = Button(screen, 50, h-400, 100, 50, text="Wallis", fontSize=10, margin=20, inactiveColour=wallis.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: wallis.toggle_on_off())
rs_button = Button(screen, 50, h-350, 100, 50, text="Ramanujan-Sato", fontSize=10, margin=20, inactiveColour=ramanujan_sato_1.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: ramanujan_sato_1.toggle_on_off())
de_button = Button(screen, 50, h-300, 100, 50, text="eta(s)", fontSize=10, margin=20, inactiveColour=dirichlet_eta_1.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: dirichlet_eta_1.toggle_on_off())
h_odd_button = Button(screen, 50, h-250, 100, 50, text="H(s)", fontSize=10, margin=20, inactiveColour=odd_h.col, hoverColour=(150, 0, 0), pressedColour=(0, 200, 20), radius=20, onClick= lambda: odd_h.toggle_on_off())

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

    zeta_fn.f = lambda n: zeta(zeta_value.getValue(), n)
    zeta_fn.expected = compute_zeta(zeta_value.getValue())
    dirichlet_eta_1.f = lambda n: dirichlet_eta(eta_value.getValue(), n)
    dirichlet_eta_1.expected = compute_dirichlet_eta(eta_value.getValue())
    #odd_h.f = lambda n: modified_eta_odd(h_odd_value.getValue(), n)
    #odd_h.expected = 

    zeta_fn.reset()
    madhava_leibnitz.reset()
    ramanujan_sato_1.reset()
    wallis.reset()
    dirichlet_eta_1.reset()
    odd_h.reset()
    for i in range(1, n):
        zeta_fn.compute()
        madhava_leibnitz.compute()
        ramanujan_sato_1.compute()
        wallis.compute()
        dirichlet_eta_1.compute()
        odd_h.compute()

        zeta_fn.draw((x_slider, y_slider))
        madhava_leibnitz.draw((x_slider, y_slider))
        ramanujan_sato_1.draw((x_slider, y_slider))
        wallis.draw((x_slider, y_slider))
        dirichlet_eta_1.draw((x_slider, y_slider))
        odd_h.draw((x_slider, y_slider))

    y_output.setText(y_slider.getValue())
    x_output.setText(x_slider.getValue())
    zeta_output.setText(f"zeta({zeta_value.getValue()}")
    eta_output.setText(f"eta({eta_value.getValue()})")
    #h_odd_output.setText(f"H({h_odd_value.getValue()})")

    screen.blit(surface, (0, scroll_y))
    pygame_widgets.update(event)
    pygame.display.update()
pygame.quit()