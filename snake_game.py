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
        "black": (0, 0, 0),
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
        self.high_score = 0  

        self.game_display = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('Snake Game')

        self.snake_block = 10
        self.snake_List = []
        self.snake_Head = []
        self.Length_of_snake = 1

        self.clock = pygame.time.Clock()

        self.font_style = pygame.font.SysFont("arial", 15)
        self.score_font = pygame.font.SysFont("arial", 15)

    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, (0, 0, 0))
        self.game_display.blit(value, [0, 0])

    def High_score(self):
        high_score_text = self.score_font.render("High Score: " + str(self.high_score), True, (0, 0, 0))
        self.game_display.blit(high_score_text, [self.settings.width - 200, 0])

    def our_snake(self):
        for x in self.snake_List:
            pygame.draw.rect(self.game_display, self.settings.snake_color, [x[0], x[1], self.snake_block, self.snake_block])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.game_display.blit(mesg, [self.settings.width / 6, self.settings.height / 3])

    def reset_game(self):
        """Reset all variables to start a new game."""
        self.snake_List = []
        self.snake_Head = []
        self.Length_of_snake = 1
        self.game_close = False
        self.game_over = False

    def gameLoop(self):
        while not self.game_over:
            self.reset_game()

            x1 = self.settings.width / 2
            y1 = self.settings.height / 2
            x1_change = 0
            y1_change = 0

            foodx = round(random.randrange(0, self.settings.width - self.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, self.settings.height - self.snake_block) / 10.0) * 10.0

            while not self.game_close:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                        self.game_close = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -self.snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = self.snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -self.snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = self.snake_block
                            x1_change = 0

                if x1 >= self.settings.width or x1 < 0 or y1 >= self.settings.height or y1 < 0:
                    self.game_close = True

                x1 += x1_change
                y1 += y1_change
                self.game_display.fill((51, 153, 213))

                pygame.draw.rect(self.game_display, self.settings.fruit_color, [foodx, foody, self.snake_block, self.snake_block])

                self.snake_Head = []
                self.snake_Head.append(x1)
                self.snake_Head.append(y1)
                self.snake_List.append(self.snake_Head)

                if len(self.snake_List) > self.Length_of_snake:
                    del self.snake_List[0]

                for x in self.snake_List[:-1]:
                    if x == self.snake_Head:
                        self.game_close = True

                self.our_snake()
                self.Your_score(self.Length_of_snake - 1)
                self.High_score()  

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, self.settings.width - self.snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, self.settings.height - self.snake_block) / 10.0) * 10.0
                    self.Length_of_snake += 1

                    
                    if self.Length_of_snake - 1 > self.high_score:
                        self.high_score = self.Length_of_snake - 1

                self.clock.tick(self.settings.snake_speed)

            while self.game_close:
                self.game_display.fill((50, 153, 213))
                self.message("You Lost! Press Q to Quit or Press C to Play Again!", (213, 50, 80))
                self.Your_score(self.Length_of_snake - 1)
                self.High_score()  
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.reset_game()

        pygame.quit()
        quit()


def main():
    user_settings = get_user_settings()
    settings = Settings(
        width=user_settings["width"],
        height=user_settings["height"],
        snake_color=user_settings["snake_color"],
        fruit_color=user_settings["fruit_color"],
        snake_speed=user_settings["snake_speed"]
    )
    game = Game(settings)
    game.gameLoop()


if __name__ == "__main__":
    main()
