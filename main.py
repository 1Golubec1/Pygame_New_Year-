import pygame
import random
import sys
from screen import Screen
from srceen_2 import Screen_2
from pygame.color import THECOLORS
from screen_end_bad import Screen_end_bad
from rule_screen import Rule_screen
from screen_good_end import Screen_good_end

from ball import Ball
from ice import Ice

ball_list = []
time_pass_spawn_ball = 0
speed_spawn_ball = random.randint(20, 80)
skip_ball = 0
ball_frame = 0
count_good_ball_dead = 0
count_bad_ball_dead = 0
State = "START"

# PYGAME
pygame.init()
pygame.font.init()
screen_good_end_obj = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
screen_obj = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
screen_2_obj = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
screen_end_bad_obj = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
rule_screen_obj = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
pygame.display.set_caption('new_year')
# icon = pygame.image.load('img/duck.jpg')
# pygame.display.set_icon(icon)
my_font = pygame.font.SysFont('Comic Sans MS', 30)
font = pygame.font.SysFont('Comic Sans MS', 25)
start_button = my_font.render('Нажмите на "enter" для того, чтобы начать', False, THECOLORS["white"])
rule_button = my_font.render('что бы ознакомится с правилами нажмите на "пробел"', False, THECOLORS["white"])
end_button = my_font.render('Ваш праздник украл гринч,нажмите на "esc" что бы выйти', False, THECOLORS["white"])
rule_button_1 = font.render('В этой игре вам нужно лопать шары, они бывают двух цветов: красного, синего.', False,
                               THECOLORS["black"])
rule_button_2 = font.render("если ловпнуть 20 красных шаров, то игра закончится с плохой концовкой,", False,
                               THECOLORS["black"])
rule_button_3 = font.render("еси лопнуть 30 синих, то она закончится с хорошой концовкой.,", False,
                               THECOLORS["black"])
rule_button_4 = font.render("для того, чтобы начать нажмите на 'enter'", False, THECOLORS["black"])
good_end_button = my_font.render("С наступившим новым годом! Для выхода нажмите 'esc'", False, THECOLORS["black"])
# IMG
window_good_end = Screen_good_end(pygame.image.load("img/good_end.jpg"))
window_rule = Rule_screen(pygame.image.load("img/back_3.jpg"))
window = Screen(pygame.image.load("img/back.jpg"))
start_window = Screen_2(pygame.image.load("img/back_2.jpg"))
window_bad_end = Screen_end_bad(pygame.image.load("img/end_back.jpg"))
ice_obj = Ice(pygame.image.load("img/icicle.png"))
bad_ball = pygame.image.load("img/bad_ball.png")
good_ball = pygame.image.load("img/good_ball.png")
clock = pygame.time.Clock()


def create_ball():
    global ball_frame
    global speed_spawn_ball
    global time_pass_spawn_ball
    ball_frame += 1
    time_pass_spawn_ball += 1
    if time_pass_spawn_ball % speed_spawn_ball == 0 and len(ball_list) < 4:
        ball_list.append(Ball(bad_ball, good_ball))
        speed_spawn_ball = random.randint(20, 80)


def control_move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ice_obj.move_left()
    elif keys[pygame.K_d]:
        ice_obj.move_right()


def ball_update():
    global skip_ball
    for bird in ball_list:
        if bird.active:
            bird.update(screen_obj, ball_frame)
        else:
            skip_ball += 1
            ball_list.remove(bird)


def collision_ball():
    global count_good_ball_dead
    global count_bad_ball_dead
    if ball_list != []:
        for ball in ball_list:
            if Ice.collision(ball, ice_obj):
                if ball.state == "bad_end":
                    count_bad_ball_dead += 1
                    ball_list.remove(ball)
                if ball.state == "good_end":
                    count_good_ball_dead += 1
                    ball_list.remove(ball)


while State == "START":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                State = "PLAY"
            if event.key == pygame.K_SPACE:
                State = "RULE"
    start_window.update(screen_2_obj)
    screen_2_obj.blit(start_button, (300, 300))
    screen_2_obj.blit(rule_button, (240, 400))
    pygame.display.flip()

while State == "RULE":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                State = "PLAY"
    window_rule.update(rule_screen_obj)
    rule_screen_obj.blit(rule_button_1, (100, 75))
    rule_screen_obj.blit(rule_button_2, (100, 185))
    rule_screen_obj.blit(rule_button_3, (100, 300))
    rule_screen_obj.blit(rule_button_4, (100, 425))
    pygame.display.flip()

while State == "PLAY" and count_bad_ball_dead < 20 and count_good_ball_dead < 30:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        control_move()
    count_1 = my_font.render(f'количество лопнутых синих шаров: {count_good_ball_dead}', False, THECOLORS["white"])
    count_2 = my_font.render(f'количество лопнутых красных шаров: {count_bad_ball_dead}', False, THECOLORS["white"])
    create_ball()

    window.update(screen_obj)
    screen_obj.blit(count_1, (1, Screen.HEIGHT - 40))
    screen_obj.blit(count_2, (Screen.WIDTH - 600, Screen.HEIGHT - 40))
    ice_obj.update(screen_obj)

    collision_ball()
    ball_update()
    clock.tick(Screen.FPS)
    pygame.display.flip()

while State == "PLAY" and count_bad_ball_dead >= 20:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                State = "START"

    window_bad_end.update(screen_2_obj)
    screen_end_bad_obj.blit(end_button, (300, 300))
    pygame.display.flip()

while State == "PLAY" and count_good_ball_dead >= 30:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                State = "START"

    window_good_end.update(screen_good_end_obj)
    screen_good_end_obj.blit(good_end_button, (300, 300))
    pygame.display.flip()
