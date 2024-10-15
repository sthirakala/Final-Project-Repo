# Author   : Sahasra Thirakala
# Email    : sthirakala@umass.edu
# Spire ID : 34692111

import time 
import random
import pygame

s_speed = 100

window_x = 1000
window_y = 1000

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
red = pygame.Color(255,0,0)

scoreboard = {}

def add_player(player_name):
    scoreboard[player_name] = 0

def update_score(player_name, score):
    if player_name in scoreboard:
        scoreboard[player_name] += score
    else:
        print("Player not found.")

def display_scoreboard():
    print("Scoreboard:")
    for player, score in scoreboard.items():
        print(f"{player}: {score}")

#Example 
add_player("player1")

update_score("player1", 10)
update_score("player1", 15)

display_scoreboard() 
