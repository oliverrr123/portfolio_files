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

def choosingColorsKeys(color):
    if choosingSnakeColor:
        colorOfSnake = color
        choosingSnakeColor = False
        choosingBackgroundColor = True
    elif choosingBackgroundColor:
        colorOfBackground = color
        choosingBackgroundColor = False
        choosingFoodColor = True
    elif choosingFoodColor:
        colorOfFood = color
        choosingFoodColor = False
        playing = True

def choosingColors(fontVar, thingType):
    screen.fill((0, 0, 0))
    mainText = fontVar.render(f"Choose the color of {thingType}:", True, (255, 255, 255))
    screen.blit(mainText, (unit * 4 - unit // 2, size_y * unit // 4))
    red = fontVar.render("red (press 'r')", True, (255, 0, 0))
    screen.blit(red, (unit * 3, size_y * unit // 2))
    green = fontVar.render("green (press 'g')", True, (0, 255, 0))
    screen.blit(green, (unit * 4, size_y * unit // 2 + unit))
    blue = fontVar.render("blue (press 'b')", True, (0, 0, 255))
    screen.blit(blue, (unit * 5, size_y * unit // 2 + unit * 2))
    white = fontVar.render("white (press '1')", True, (255, 255, 255))
    screen.blit(white, (unit * 6, size_y * unit // 2 + unit * 3))
    black = fontVar.render("black (press '0')", True, (50, 50, 50))
    screen.blit(black, (unit * 7, size_y * unit // 2 + unit * 4))

pygame.init()
 
DIRECTIONS = {
    # KEY: (dx, dy)
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_DOWN: (0, 1),
}

DIRECTIONS_2 = {
    # KEY: (dx, dy)
    pygame.K_d: (1, 0),
    pygame.K_w: (0, -1),
    pygame.K_a: (-1, 0),
    pygame.K_s: (0, 1),
}
 
unit = 40
 
size_x, size_y = 15, 15


screen = pygame.display.set_mode((size_x * unit, size_y * unit))
screen.fill((0, 0, 0))
 
character = pygame.Surface((unit, unit), pygame.SRCALPHA)
character.fill((255, 255, 255))
 
character2 = pygame.Surface((unit, unit), pygame.SRCALPHA)
character2.fill((255, 255, 255))

food = pygame.Surface((unit, unit), pygame.SRCALPHA)
food.fill((0, 255, 0))
 
miniMap = pygame.Surface((unit // 2, unit // 2), pygame.SRCALPHA)
miniMap.fill((230, 230, 230))

#fonts
font = pygame.font.Font("freesansbold.ttf", unit * 4 // 3)
font2 = pygame.font.Font("freesansbold.ttf", unit // 2)
chooseColoursFont = pygame.font.Font("freesansbold.ttf", unit // 2)
youDiedFont = pygame.font.Font("freesansbold.ttf", size_x * 6)
pressSpaceFont = pygame.font.Font("freesansbold.ttf", size_x * 3)
controlsFont = pygame.font.Font("freesansbold.ttf", size_x * 2)
 
# { x * 2, Pro každé x z rozsahu od 0 do 10 }
# { 0, 2, 4, 6, 8 ... 18, 20} <- {0, 1, 2, 3, 4 .. 8, 9, 10}
 
# seznam = [ x / 2 for x in range(0, 10) ]
# print(seznam)
 
#    >-(:)==============>
# snake = [ (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0) ]
snake = [(x, size_y // 2) for x in reversed(range(0, 6))]
snake2 = [(x, size_y // 3) for x in reversed(range(0, 6))]

colorOfSnake = 0
colorOfSnake2 = 0
colorOfBackground = 0
colorOfFood = 0

 
food_list = [food_coords(snake) for i in range(0, 6)]
 
dx, dy = 1, 0
dx2, dy2 = 1, 0

clock = pygame.time.Clock()
running = True
playing = False
snakeDied = False
snake2Died = False
welcomeTF = True
choosingSnakeColor = False
choosingSnake2Color = False
choosingBackgroundColor = False
choosingFoodColor = False

speed = 5
 
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if welcomeTF:
                    welcomeTF = False
                    choosingSnakeColor = True
                else:
                    playing = True
            elif event.key == pygame.K_r:
                if choosingSnakeColor:
                    colorOfSnake = (255, 0, 0)
                    choosingSnakeColor = False
                    choosingSnake2Color = True
                elif choosingSnake2Color:
                    colorOfSnake2 = (255, 0, 0)
                    choosingSnake2Color = False
                    choosingBackgroundColor = True
                elif choosingBackgroundColor:
                    colorOfBackground = (255, 0, 0)
                    choosingBackgroundColor = False
                    choosingFoodColor = True
                elif choosingFoodColor:
                    colorOfFood = (255, 0, 0)
                    choosingFoodColor = False
                    playing = True
            elif event.key == pygame.K_g:
                if choosingSnakeColor:
                    colorOfSnake = (0, 255, 0)
                    choosingSnakeColor = False
                    choosingSnake2Color = True
                elif choosingSnake2Color:
                    colorOfSnake2 = (0, 255, 0)
                    choosingSnake2Color = False
                    choosingBackgroundColor = True
                elif choosingBackgroundColor:
                    colorOfBackground = (0, 255, 0)
                    choosingBackgroundColor = False
                    choosingFoodColor = True
                elif choosingFoodColor:
                    colorOfFood = (0, 255, 0)
                    choosingFoodColor = False
                    playing = True      
            elif event.key == pygame.K_b:
                if choosingSnakeColor:
                    colorOfSnake = (0, 0, 255)
                    choosingSnakeColor = False
                    choosingSnake2Color = True
                elif choosingSnake2Color:
                    colorOfSnake2 = (0, 0, 255)
                    choosingSnake2Color = False
                    choosingBackgroundColor = True
                elif choosingBackgroundColor:
                    colorOfBackground = (0, 0, 255)
                    choosingBackgroundColor = False
                    choosingFoodColor = True
                elif choosingFoodColor:
                    colorOfFood = (0, 0, 255)
                    choosingFoodColor = False
                    playing = True    
            elif event.key == pygame.K_1:
                if choosingSnakeColor:
                    colorOfSnake = (255, 255, 255)
                    choosingSnakeColor = False
                    choosingSnake2Color = True
                elif choosingSnake2Color:
                    colorOfSnake2 = (255, 255, 255)
                    choosingSnake2Color = False
                    choosingBackgroundColor = True
                elif choosingBackgroundColor:
                    colorOfBackground = (255, 255, 255)
                    choosingBackgroundColor = False
                    choosingFoodColor = True
                elif choosingFoodColor:
                    colorOfFood = (255, 255, 255)
                    choosingFoodColor = False
                    playing = True    
            elif event.key == pygame.K_0:
                if choosingSnakeColor:
                    colorOfSnake = (0, 0, 0)
                    choosingSnakeColor = False
                    choosingSnake2Color = True
                elif choosingSnake2Color:
                    colorOfSnake2 = (0, 0, 0)
                    choosingSnake2Color = False
                    choosingBackgroundColor = True
                elif choosingBackgroundColor:
                    colorOfBackground = (0, 0, 0)
                    choosingBackgroundColor = False
                    choosingFoodColor = True
                elif choosingFoodColor:
                    colorOfFood = (0, 0, 0)
                    choosingFoodColor = False
                    playing = True   
            elif event.key in DIRECTIONS:
                (dx, dy) = DIRECTIONS[event.key]
            elif event.key in DIRECTIONS_2:
                (dx2, dy2) = DIRECTIONS_2[event.key]
        # elif event.type == pygame.KEYUP:
            # (dx, dy) = (0, 0)

    if welcomeTF:
        screen.fill((0, 0, 0))
        welcome = font.render("Welcome to snake!", True, (255, 255, 255))
        screen.blit(welcome, (unit * 5 // 3, size_y * unit // 4))
        welcome2 = font2.render("press space to continue", True, (230, 230, 230))
        screen.blit(welcome2, (unit * 4, size_y * unit // 2))

    if choosingSnakeColor:
        choosingColors(font2, "1st snake")

    if choosingSnake2Color:
        choosingColors(font2, "2nd snake")

    if choosingBackgroundColor:
        choosingColors(font2, "background")
    
    if choosingFoodColor:
        choosingColors(font2, "food")

    if playing:
        screen.fill(colorOfBackground)
        character.fill(colorOfSnake)
        character2.fill(colorOfSnake2)
        food.fill(colorOfFood)

        (x, y) = snake[0]
        (x2, y2) = snake2[0]
 
        x += dx
        y += dy

        x2 += dx2
        y2 += dy2
 
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

        if x2 >= size_x:
            x2 = 0
        elif x2 < 0:
            x2 = size_x - 1
 
        if y2 >= size_y:
            y2 = 0
        elif y2 < 0:
            y2 = size_y - 1
 
        snake2.insert(0, (x2, y2))

        #pruhlednost
        character.set_alpha(255)

        # naboural do sebe?
        if snake[0] in snake[1:]:
            snakeDied = True
            playing = False
            character.fill((255, 0, 0))
            screen.blit(character, (x * unit, y * unit))
            pygame.display.update()

        if snake2[0] in snake2[1:]:
            snake2Died = True
            playing = False
            character2.fill((255, 0, 0))
            screen.blit(character2, (x2 * unit, y2 * unit))
            pygame.display.update()

        if snake[0] in snake2[1:]:
            snakeDied = True
            playing = False
            character.fill((255, 0, 0))
            screen.blit(character, (x * unit, y * unit))
            pygame.display.update()
        
        if snake2[0] in snake[1:]:
            snake2Died = True
            playing = False
            character.fill((255, 0, 0))
            screen.blit(character, (x * unit, y * unit))
            pygame.display.update()

        # snedl jidlo?
        if snake[0] in food_list:
            food_list.remove(snake[0])
            food_list.append(food_coords(snake))
            speed += 0.1
        else:
            snake.pop()

        if snake2[0] in food_list:
            food_list.remove(snake2[0])
            food_list.append(food_coords(snake2))
            speed += 0.1
        else:
            snake2.pop()

        # 2. vykresli jidlo
        for (x, y) in food_list:
            screen.blit(food, (x * unit, y * unit))
    
        # 3. vykresli hada
        for (x, y) in snake:
            screen.blit(character, (x * unit, y * unit))
            character.set_alpha(max(character.get_alpha() * 0.9, 50))

        for (x2, y2) in snake2:
            screen.blit(character2, (x2 * unit, y2 * unit))
            character.set_alpha(max(character.get_alpha() * 0.9, 50))
        
        #minimap
        #screen.blit(miniMap, snake[0])

        #print(snake[0])
    
        # 4. vypis skore
        #text = font.render(str(len(snake)) + "/" + str(size_x * size_y), True, (25, 200, 25))
        #screen.blit(text, (0, 0))
    
        # vypis skore do titulku okna
        #pygame.display.set_caption(str(len(snake)) + "/" + str(size_x * size_y))


        #idk wadis dis
        #vypis press space to start and controls
        #if playing == False:
        #    if gameOver == False:
        #        pressSpace = pressSpaceFont.render("Press SPACE to start", True, (0, 0, 255))
        #        screen.blit(pressSpace, (size_x * 5, size_y * 15))
        #        controls = controlsFont.render("Controls: arrows", True, (0, 0, 255))
        #        screen.blit(controls, (size_x * 12, size_y * 18))


    # dosahl maximalni delky?
    if (len(snake) == size_x * size_y // 2):
        text = font.render(str("Vyhral jsi"), True, (0, 255, 0))
        screen.blit(text, (size_x * unit // 2, size_y * unit // 2))
        playing = False

    #vypis you died a score
    if snakeDied == True:
        youDiedText = youDiedFont.render("Snake2 won!", True, (200, 25, 25))
        screen.blit(youDiedText, (size_x, size_y * 10))
        #scoreText = font.render("Score: " + str(len(snake)), True, (25, 200, 25))
        #screen.blit(scoreText, (size_x * size_x, size_y * 20))

    if snake2Died == True:
        youDiedText = youDiedFont.render("Snake1 won!", True, (200, 25, 25))
        screen.blit(youDiedText, (size_x, size_y * 10))
        
    pygame.display.update()
    clock.tick(speed)
