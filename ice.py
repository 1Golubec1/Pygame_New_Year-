from screen import Screen
import pygame


class Ice:
    WIDTH = 400
    HEIGHT = 150
    SPEED = 10

    def __init__(self, img):
        self.pos_x = (Screen.WIDTH - Ice.WIDTH) // 2
        self.pos_y = 0
        self.img = pygame.transform.scale(img, (Ice.WIDTH, Ice.HEIGHT))

    def move_right(self):
        if self.pos_x < Screen.WIDTH - Ice.WIDTH:
            self.pos_x += Ice.SPEED

    def move_left(self):
        if self.pos_x > 0:
            self.pos_x -= Ice.SPEED

    @staticmethod
    def collision(ball, ice):
        if ball.pos_y == Ice.HEIGHT and ball.pos_x in [i for i in range(ice.pos_x - 200, ice.pos_x + 401)]:
            return True
        return False

    def update(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))

#   and ball.pos_x in [i for i in range(ice.pos_x - 200, ice.pos_x + 201)]
