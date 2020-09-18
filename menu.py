#!/usr/bin/python3
"""
"""
import pygame
import pygame_menu



pygame.init()
surface = pygame.display.set_mode((600, 800))

def set_difficulty(value, difficulty):
    if value == 1:
        return(1)
    else:
        return (2)

def start_the_game():
    # Do the job here !
    pass

def Play_Mode(mode, value):
    pass

menu = pygame_menu.Menu(500, 500, 'Master Mind Game',
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add_text_input('Enter Your Name :', default='Master')
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_selector('Play Mode :', [('Single Player', 1), ('Two Players', 2)], onchange=Play_Mode)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)