import pygame


class Screen_good_end:
    WIDTH = 1200
    HEIGHT = 800

    def __init__(self, img):
        self.img = pygame.transform.scale(img, (Screen_good_end.WIDTH, Screen_good_end.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))
