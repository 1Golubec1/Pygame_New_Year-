from pygame.color import THECOLORS
import pygame


class Screen:
    WIDTH = 1200
    HEIGHT = 800
    FPS = 120

    def __init__(self, img):
        self.img = pygame.transform.scale(img, (Screen.WIDTH, Screen.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))
