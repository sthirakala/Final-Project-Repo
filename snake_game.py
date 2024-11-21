# Author   : Sahasra Thirakala
# Email    : sthirakala@umass.edu
# Spire ID : 34692111

import pygame
import time
import random


pygame.init()


def get_user_settings():
    print("Welcome to the Snake Game!")
    print("Please input the following settings:")

  
    width = int(input("Enter width of the game window: "))
    height = int(input("Enter height of the game window: "))
    
    snake_speed = int(input("Enter snake speed: "))
    
    
    available_colors = {
        "red": (255, 0, 0),
        "yellow": (255, 255, 0),
        "orange": (255, 165, 0),
        "green": (144, 238, 144),
        "blue": (0, 0, 255),
        "pink": (255, 192, 203),
        "purple": (128, 0, 128),
        "brown": (137, 81, 41), 
        "black": (0,0,0),
        "white": (255, 255, 255)
    }
    print("Choose a color for the snake: red, yellow, orange, green, blue, pink, purple, brown, black, white")
    snake_color_input = input("Enter snake color: ").strip().lower()
    snake_color = available_colors.get(snake_color_input, (0, 255, 0)) 

    
    print("Choose a color for the fruit: red, yellow, orange, green, blue, pink, purple, brown, black, white")
    fruit_color_input = input("Enter fruit color: ").strip().lower()
    fruit_color = available_colors.get(fruit_color_input, (255, 0, 0)) 

    return {
        "width": width,
        "height": height,
        "snake_color": snake_color,
        "fruit_color": fruit_color,
        "snake_speed": snake_speed
    }

class Settings:
    def __init__(self, width=600, height=400, snake_color=(0, 255, 0), fruit_color=(255, 0, 0), snake_speed=15):
        self.width = width
        self.height = height
        self.snake_color = snake_color
        self.fruit_color = fruit_color
        self.snake_speed = snake_speed


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.game_over = False
        self.game_close = False

     
        self.game_display = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('Snake Game')

      
        self.snake_block = 10
        self.snake_List = []
        self.snake_Head = []
        self.Length_of_snake = 1

    
        self.clock = pygame.time.Clock()

    
        self.font_style = pygame.font.SysFont("arial", 25)
        self.score_font = pygame.font.SysFont("arial", 35)

   
    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, (0, 0, 0))
        self.game_display.blit(value, [0, 0])

