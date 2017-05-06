import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
    pygame.init();
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    bg_color = (230,230,230)
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion");
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)

    
run_game()
