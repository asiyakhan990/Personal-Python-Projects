import pygame
import time
import random
import os

pygame.init()

# Window
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

# Load sounds
eat_sound = pygame.mixer.Sound("eat.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

# High score file
def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Score display
def score_display(score):
    value = score_font.render("Score: " + str(score), True, white)
    win.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3 + y_offset])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    high_score = load_high_score()
    
    gameover_sound_played = False  

    while not game_over:

        while game_close:
            if not gameover_sound_played:
                pygame.mixer.Sound.play(gameover_sound)
                gameover_sound_played = True  

            win.fill(blue)
            message("Game Over! Press C to Play Again or Q to Quit", red)
            message(f"Your Score: {snake_length - 1}", white, 40)
            message(f"High Score: {high_score}", white, 80)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = snake_block
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += dx
        y += dy
        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(snake_length - 1)
        pygame.display.update()

        # Food collision
        if x == food_x and y == food_y:
            pygame.mixer.Sound.play(eat_sound)
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    # Save high score if beaten
    final_score = snake_length - 1
    if final_score > high_score:
        save_high_score(final_score)

    pygame.quit()
    quit()

game_loop()
