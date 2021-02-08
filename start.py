import pygame

BACKGROUND_COLOR = (100,100,100)

class Start:
    def __init__(self, screen, win_x, win_y):
        self.screen = screen

        # 設定顯示文字
        font = pygame.font.SysFont('couriernew', 35)
        text = font.render('Press S to start!', True, (0,255,0))
        self.text = text
        textRect = text.get_rect()
        textRect.center=(win_x//2, win_y//2)
        self.text_rect = textRect 
    
    def display(self):   
        self.screen.blit(self.text, self.text_rect)

    