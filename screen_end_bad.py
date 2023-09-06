import pygame


class Screen_end_bad:
    WIDTH = 1200
    HEIGHT = 800

    def __init__(self, img):
        self.img = pygame.transform.scale(img, (Screen_end_bad.WIDTH, Screen_end_bad.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))
