import pygame
from constants import *

# ends pygame and program
def end():
    shelf.close()
    pygame.quit()
    quit()

# adds text to center of display
def message(s, font, y, color = black):
    text = font.render(s, True, color)
    display.blit(text, text.get_rect(center = (dispWD / 2, dispHT / 2 + y)))

# adds text with color background to display
def button(s, color, center, width = 150):
    rect = pygame.Rect(0, 0, width, 100)
    rect.center = center
    pygame.draw.rect(display, color, rect)

    text = oswald.render(s, True, black)
    display.blit(text, text.get_rect(center = center))

    return rect