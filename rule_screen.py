import pygame


class Rule_screen:
    WIDTH = 1200
    HEIGHT = 800

    def __init__(self, img):
        self.img = pygame.transform.scale(img, (Rule_screen.WIDTH,Rule_screen.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))
