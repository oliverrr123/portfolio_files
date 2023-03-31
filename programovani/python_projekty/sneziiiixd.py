import pygame
import random

resolution_x, resolution_y = 1600, 900
max_depth = 5

def generate_snow_snowflake():
    return {
        'x': random.randint(0, resolution_x),
        'y': random.randint(0, resolution_y),
        'z': random.randint(1, max_depth)
    }

pygame.init()

screen = pygame.display.set_mode((resolution_x, resolution_y))

charsize = 20
radius = charsize // 2

snow = [generate_snow_snowflake() for i in range(100)]

clock = pygame.time.Clock()

wind = 0
gravity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                wind -= 1
            elif event.key == pygame.K_RIGHT:
                wind += 1
            elif event.key == pygame.K_UP:
                gravity -= 1
            elif event.key == pygame.K_DOWN:
                gravity += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                wind = 0
            elif event.key == pygame.K_RIGHT:
                wind = 0

    for snowflake in snow:
        snowflake['x'] += wind // snowflake['z']
        snowflake['y'] += gravity // snowflake['z']

        if snowflake['x'] > resolution_x:
            snowflake['x'] = 0
        if snowflake['x'] < 0:
            snowflake['x'] = resolution_x

        if snowflake['y'] > resolution_y:
            snowflake['x'] = random.randint(0, resolution_x)
            snowflake['y'] = 0
        if snowflake['y'] < 0:
            snowflake['x'] = random.randint(0, resolution_x)
            snowflake['y'] = resolution_y
        


    screen.fill((0, 0, 0))
    for snowflake in snow:
        pygame.draw.circle(screen, (255, 255, 255, 255), (snowflake['x'], snowflake['y']), radius // snowflake['z'])
    clock.tick(20)
    pygame.display.update()