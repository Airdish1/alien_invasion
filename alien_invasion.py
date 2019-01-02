import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():

    #Start game and create the screen

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make an group of aliens
    aliens = Group()
    # Make a group to store the bullets
    bullets = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings,screen, aliens)

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

