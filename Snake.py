import sys
import runpy
import pygame
import random
import time

#Library Initialisation
pygame.init()
pygame.font.init()
pygame.display.set_caption("Snakeee")

#Colour COde
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,255, 0)
blue = (0, 0, 255)

#Board Specifications

width = 560
rows = 16
box_width = width // rows
screen =pygame.display.set_mode((width, (width + (width // 16))))

#Misc

game_end = False
font = pygame.font.SysFont("Calibri", (width // 16))
snake_position = [(random.randint(0, (rows - 1)) * box_width), (random.randint(0, (rows - 1)) * box_width)]
fruit_position = [(random.randint(0, (rows - 1)) * box_width), (random.randint(0, (rows - 1)) * box_width)]
snake_body = []
snake_length = 1
points = 0
c_x = 0
c_y = 0

#Dessiner le Tableau

def board():
    xx = 0
    yy = 0

    screen.fill(white)
    pygame.draw.line(screen, black, (0, 0), (width, 0))
    pygame.draw.line(screen, black, (0, width), (width, width))
    pygame.draw.line(screen, black, (0, 0), (0, width))
    pygame.draw.line(screen, black, (width, 0), (width, width))

    for i in range(rows):
        xx = xx + box_width
        yy = yy + box_width
        pygame.draw.line(screen, black, (xx, 0), (xx, width))
        pygame.draw.line(screen, black, (0, yy), (width, yy))

#Dessiner le serpent

def snake(snake_body):
    for i in snake_body:
        pygame.draw.rect(screen, green, [(i[0] + 1), (i[1] + 1), (box_width - 1), (box_width - 1)])
        #Ajout d'yeux
        """if i == 0:
            eye_1 = (snake_body[i][0] + (box_width // 4), snake_body[i][1] + (box_width // 4))
            eye_2 = (snake_body[i][0] + (3 * box_width // 4), snake_body[i][1] + (box_width // 4))
            pygame.draw.circle(screen, white, eye_1, 3)
            pygame.draw.circle(screen, white, eye_2, 3)"""

#Dessiner le fruit
def fruit():
    pygame.draw.rect(screen, red, ((fruit_position[0] + 1),(fruit_position[1] +1), (box_width - 1), (box_width - 1)))

#Dessiner le Tableau de Score

def scoreboard():
    pygame.draw.rect(screen, white,((0, (width + 1)), (width, 65)))
    screen.blit(font.render("Points :", True, white), (0, width))
    screen.blit(font.render(str(points), True, blue), ((width // 5), width))


def end_screen():
    screen.fill(white)
    screen.blit(font.render("GAME OVER", True, red), ((width // 4), (width // 4)))
    screen.blit(font.render("Points:", True, blue), ((width // 4), (width // 4) + (width // 10)))
    screen.blit(font.render(str(points), True, blue), (((width // 4) * 2), (width // 4) + (width // 10)))
    screen.blit(font.render("ESC - Quit", True, black), ((width // 4), (width // 2)))
    screen.blit(font.render("SPACE - Restart", True, black), ((width // 4), ((width // 2) + (width // 10))))
    screen.blit(font.render("TAB - Main Menu", True, black), ((width // 4), ((width // 2) + 2*(width // 10))))

while not game_end:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.key == pygame.K_TAB:
                runpy.run_module(mod_name="Un ptit snake comme ça")

            #Direction
            """if event.key == pygame.K_UP or event.key == pygame.K_w :
                c_y = -box_width
                c_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                c_y = box_width
                c_x = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                c_x = box_width
                c_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                c_x = -box_width
                c_y = 0"""
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                c_y = -box_width
                c_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                c_y = box_width
                c_x = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                c_x = box_width
                c_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                c_x = -box_width
                c_y = 0


            """if c_x > box_width:
                c_x += box_width
            if c_x < box_width:
                c_x -= box_width
            if c_y > box_width:
                c_y += box_width
            if c_y < box_width:
                c_y -= box_width"""

    snake_position[0] += c_x
    snake_position[1] += c_y

    # Longueur Serpent
    snake_head = [snake_position[0], snake_position[1]]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]
    for i in snake_body[:-1]:
        if i == snake_head:
            game_end = True

    # Identify Points
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        snake_length = snake_length + 1
        fruit_position = [(random.randint(0, (rows - 1)) * box_width), (random.randint(0, (rows - 1)) * box_width)]
        ii = 0
        for i in range(len(snake_body)):
            if fruit_position == snake_body[ii]:
                fruit_position = [(random.randint(0, (rows - 1)) * box_width), (random.randint(0, (rows - 1)) * box_width)]
            ii += 1
        fruit()
        points = points + 1

    board()
    snake(snake_body)
    fruit()
    scoreboard()
    pygame.display.update()
    time.sleep(.15)

    while game_end:

        end_screen()
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    game_end = False
                    runpy.run_module(mod_name="Snake")

                if event.key == pygame.K_TAB:
                    runpy.run_module(mod_name="Simple Mini Games")