import pygame
import json

BACKGROUND_COLOR = (20,20,20)
WALL_COLOR = (0,0,128)

class Game:
    def __init__(self, screen, win_x, win_y):
        self.screen = screen
        self.win_x = win_x
        self.win_y = win_y
        with open('./maps.json') as f:
            self.maps = json.load(f)
        self.current_map = 2

    def draw_rect(self, p, color, inflate=0):
        cube_height = self.win_x // 25
        cube_width = self.win_y // 25
        temp_rect = pygame.Rect(p[0]*cube_width, p[1]*cube_height, cube_width, cube_height).inflate(inflate, inflate)
        pygame.draw.rect(self.screen, color, temp_rect)
    
    def display(self):
        self.screen.fill(BACKGROUND_COLOR)
        for p in self.maps[self.current_map]['walls']:
            self.draw_rect(p, WALL_COLOR)