#匯入pygame

import pygame
from pygame.locals import QUIT
import random

#pygame初始化
pygame.init()

BACKGROUND_COLOR = (0,0,0)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
HEIGHT = 25
WIDTH = 25

#設定視窗
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))   #依設定顯示視窗
screen.fill(BACKGROUND_COLOR)
# 設定icon圖片
gameIcon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("Snake")           #設定程式標題

MOVE_EVENT = pygame.USEREVENT + 1
tick = 500 # millisecond
pygame.time.set_timer(MOVE_EVENT, tick)


def draw_position(x,y, color, inflate=0):
    cube_height = WINDOW_HEIGHT // HEIGHT
    cube_width = WINDOW_WIDTH // WIDTH
    temp_rect = pygame.Rect(x*cube_width, y*cube_height, cube_width, cube_height).inflate(inflate, inflate)
    pygame.draw.rect(screen, color, temp_rect)

def generate_food(chizu):
    gen=True
    while gen:
        gen = False
        x = random.randint(0,WIDTH-1)
        y = random.randint(0, HEIGHT-1)
        for p in chizu:
            if p==[x,y]:
                gen = True
    return [x,y]        

# 地圖
chizu_1 = [[i,5] for i in range(5,15)] + [[i,15] for i in range(5,15)]

# 初始條件
pos = [WIDTH//2,HEIGHT//2]
direction = [1,0]
length = 3
tail = [pos]
food = generate_food(chizu_1)



#關閉程式的程式碼
running = True
while running:
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and direction!=[0,1]:
        direction = [0, -1]
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and direction!=[1,0]: 
        direction = [-1, 0]
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and direction!=[0,-1]: 
        direction = [0, 1]
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and direction!=[-1,0]: 
        direction = [1, 0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOVE_EVENT:
            pos = [(pos[0]+direction[0])%WIDTH, (pos[1]+direction[1])%HEIGHT]

            for p in tail:
                if p==pos:
                    print('GAME OVER')
    
            for p in chizu_1:
                if p==pos:
                    print('GAME OVER')

            if pos==food:
                length += 1
                if tick > 100:
                    tick -= 50
                    pygame.time.set_timer(MOVE_EVENT, tick)
                food = generate_food(chizu_1)      

            if len(tail) <= length:
                tail.append(pos)
               
            else:
                tail.append(pos)
                tail.pop(0)
            print(tail)
    screen.fill(BACKGROUND_COLOR)
    draw_position(food[0], food[1], (255,0,0))
    draw_position(pos[0], pos[1], (0,255,0))
    for p in tail:
        draw_position(p[0], p[1], (0,255,0), -15)
    for p in chizu_1:
        draw_position(p[0],p[1],(0,0,100))
    
    pygame.display.update()
pygame.quit()    