#匯入pygame

import pygame
from pygame.locals import QUIT
import random

from start import Start
from game import Game

#pygame初始化
pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

#設定視窗
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   #依設定顯示視窗

start_page = Start(screen, WINDOW_WIDTH, WINDOW_HEIGHT)
game_page = Game(screen, WINDOW_WIDTH, WINDOW_HEIGHT)

# 設定icon圖片
gameIcon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("SNAKE")           #設定程式標題

MOVE_EVENT = pygame.USEREVENT + 1

state = 'START'  # 'GAME' 'END'

running = True
while running:
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction!=[0,1]:
        direction = [0, -1]

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if state == 'START':
        start_page.display()
        if keys[pygame.K_s]: state = 'GAME'
    elif state == 'GAME':
        game_page.display()
        if keys[pygame.K_d]: state = 'END'
    elif state == 'END':
        print('END')
        if keys[pygame.K_s]: state = 'GAME'
    pygame.display.update()
pygame.quit()    