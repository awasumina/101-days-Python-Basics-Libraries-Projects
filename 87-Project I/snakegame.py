import pygame
import time
import random
from pygame.locals import *

pygame.init()

red = (255, 0, 0)
blue= (0, 0, 255)  
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (0, 255, 255)

win_width = 900
win_height = 700
window = pygame.display.set_mode((win_height, win_height))
pygame.display.set_caption("Snake Game")
time.sleep(2)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

# choosing font
# fonts = pygame.font.get_fonts()
# print(fonts)

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# display user score

def user_score(score) :
    number = score_font.render("Score :"+ str(score), True, red)
    # blit function takes two params data to be displayed and coordintees
    
    window.blit(number, [0, 0])
    
def message(msg) :
    msg = font_style.render(msg, True, red)
    window.blit(msg, [win_width/18, win_height / 3] )
    
def snake_game(sanke, snake_len_list):
    
    for x in snake_len_list:
        pygame.draw.rect(window, green, [x[0], x[1], sanke ,snake])
 
def quit_game() :
    pygame.quit()
    quit()   

def game_loop() :
    gameOver = False
    gameClose = False
    
    x1 = win_width / 2
    y1 = win_height / 2
    
    x1_change = 0
    y1_change = 0
    change = 0
    
    snake_len_list = []
    snake_len = 1
    
    foodx = round(random.randrange( 0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange( 0, win_height - snake) / 10.0) * 10.0
    
    while not gameOver :
        
        while gameClose == True :
            
            window.fill(grey)
            message("You lost!! Press p to play again and q to quit the game")
            user_score(snake_len - 1)
            pygame.display.update()
            
            for event in pygame.event.get() :
                
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = True
                        quit_game()
                        
                    if event.key == pygame.K_p :
                        game_loop()
                        
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN :
                
                if event.key == K_LEFT :
                    x1_change = -snake
                    y1_change = 0
                
                if event.key == K_RIGHT :
                    x1_change = snake
                    y1_change = 0
                
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                
                if event.key == K_DOWN :
                    x1_change = 0
                    y1_change = snake
                        
        # Snake die conditon
        
        if x1 > win_width or x1 < 0 or y1 > win_height or y1 < 0 :
            gameClose = True
        
        # Collision with body of the snake
        
        
        x1 += x1_change
        y1 += y1_change
        
        window.fill(grey)
        pygame.draw.rect(window, yellow , [foodx, foody, snake, snake])
        
        snake_size = []
        snake_size.append(x1)
        snake_size.append(y1)
        snake_len_list.append(snake_size)
        
        if len(snake_len_list) > snake_len :
            del snake_len_list[0]
            
        snake_game(snake, snake_len_list)
        
        user_score(snake_len - 1)
        pygame.display.update()
                        
        #  snake eat food
        
        if x1 == foodx and y1 == foody :
            
             foodx = round(random.randrange( 0, win_width - snake) / 10.0) * 10.0
             foody = round(random.randrange( 0, win_height - snake) / 10.0) * 10.0
            
             snake_len += 1
             
        clock.tick(snake_speed)
    
    
game_loop()