from screen import Screen
from ice import Ice
import random
import pygame


class Ball:
    SIZE = 50

    def __init__(self, bad_ball, good_ball):
        self.ball = random.choice([bad_ball, good_ball])
        if self.ball == bad_ball:
            self.ball = pygame.transform.scale(bad_ball, (Ball.SIZE, Ball.SIZE))
            self.state = "bad_end"
            self.speed = random.randint(3, 6)
            self.pos_x = random.randint(1, Screen.WIDTH)
        else:
            self.ball = pygame.transform.scale(good_ball, (Ball.SIZE, Ball.SIZE))
            self.state = "good_end"
            self.speed = random.randint(1, 4)
            self.pos_x = random.randint(1, Screen.WIDTH)
        self.pos_y = Screen.HEIGHT - Ball.SIZE
        self.active = True
        self.move()

    def move(self):
        if self.pos_y > 0:
            self.pos_y -= self.speed
        else:
            self.active = False



    def update(self, screen, frame):
        self.move()
        screen.blit(self.ball, (self.pos_x, self.pos_y))
