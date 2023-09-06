import pygame


class Screen_2:
    WIDTH = 1200
    HEIGHT = 800

    def __init__(self, img):
        self.img = pygame.transform.scale(img, (Screen_2.WIDTH, Screen_2.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))
