import pygame
import time
import random
import itertools
 
 
def food_coords(snake):
    # vyber nahodnou hodnotu ze
    # seznamu dvojic souradnic PRO vsechny hodnoty promennych food_x, food_y ze seznamu vsech kombinaci hodnot z rozsahu 0-size_x a 0-size_y
    # ktere nejsou v hadovi
    possible_food_coordinates = [(food_x, food_y) for food_x, food_y in list(
        itertools.product(range(size_x), range(size_y))) if (food_x, food_y) not in snake]
    return random.choice(possible_food_coordinates)
 
 
pygame.init()
 
DIRECTIONS = {
    # KEY: (dx, dy)
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_DOWN: (0, 1),
}
 
unit = 40
 
size_x, size_y = 10, 10
 
screen = pygame.display.set_mode((size_x * unit, size_y * unit))
screen.fill((100, 0, 0))
 
character = pygame.Surface((unit, unit), pygame.SRCALPHA)
character.fill((255, 255, 255))
 
food = pygame.Surface((unit, unit), pygame.SRCALPHA)
food.fill((0, 200, 150))
 
font = pygame.font.Font("freesansbold.ttf", unit)
 
# { x * 2, Pro každé x z rozsahu od 0 do 10 }
# { 0, 2, 4, 6, 8 ... 18, 20} <- {0, 1, 2, 3, 4 .. 8, 9, 10}
 
# seznam = [ x / 2 for x in range(0, 10) ]
# print(seznam)
 
#    >-(:)==============>
# snake = [ (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0) ]
snake = [(x, size_y // 2) for x in reversed(range(0, 6))]
 
food_list = [food_coords(snake) for i in range(0, 6)]
 
dx, dy = 1, 0
 
clock = pygame.time.Clock()
running = True
playing = False
speed = 5
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                playing = True
            elif event.key in DIRECTIONS:
                (dx, dy) = DIRECTIONS[event.key]
        # elif event.type == pygame.KEYUP:
            # (dx, dy) = (0, 0)
 
    if playing:
        (x, y) = snake[0]
 
        x += dx
        y += dy
 
        # prochazeni zdi
        if x >= size_x:
            x = 0
        elif x < 0:
            x = size_x - 1
 
        if y >= size_y:
            y = 0
        elif y < 0:
            y = size_y - 1
 
        snake.insert(0, (x, y))
 
        # naboural do sebe?
        if snake[0] in snake[1:]:
            running = False
 
        # snedl jidlo?
        if snake[0] in food_list:
            food_list.remove(snake[0])
            food_list.append(food_coords(snake))
 
            speed += 0.1
        else:
            snake.pop()
 
        # dosahl maximalni delky?
        if (len(snake) == size_x * size_y):
            text = font.render("Vyhral jsi", True, (255, 255, 255))
            screen.blit(text, (size_x * unit // 2, size_y * unit // 2))
            playing = False
 
        # vykreslovani
        # 1. preplacni pozadi
        screen.fill((0, 0, 0))
 
    # 2. vykresli hada
    character.set_alpha(255)
    for (x, y) in snake:
        screen.blit(character, (x * unit, y * unit))
        character.set_alpha(max(character.get_alpha() * 0.9, 50))
 
    # 3. vykresli jidlo
    for (x, y) in food_list:
        screen.blit(food, (x * unit, y * unit))
 
    # 4. vypis skore
    text = font.render(str(len(snake)) + "/" +
                       str(size_x * size_y), True, (0, 255, 0))
    screen.blit(text, (0, 0))
 
    # vypis skore do titulku okna
    pygame.display.set_caption(str(len(snake)) + "/" + str(size_x * size_y))
 
    pygame.display.update()
    clock.tick(speed)