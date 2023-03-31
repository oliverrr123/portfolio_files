import pygame
import random
import os

pygame.init()

size_x, size_y = 16, 9
unit = 100
screen = pygame.display.set_mode((size_x * unit, size_y * unit))

carBody = pygame.Surface((unit * 1.5, unit * 2))
carBody.fill((140, 140, 140))

carX, carY = size_x * unit // 2 - unit // 2, size_y * unit - unit * 3
carDX = 0

carBody2 = pygame.Surface((unit * 1.65, unit * 1.3))
carBody2.fill((160, 160, 160))

carWheels = pygame.Surface((unit * 0.15, unit * 0.35))
carWheels.fill((100, 100, 100))

carLights = pygame.Surface((unit * 0.35, unit * 0.15))
carLights.fill((255, 255, 0))

lines = pygame.Surface((unit * 0.05, size_y * unit))
lines.fill((50, 50, 50))

coinBody = pygame.Surface((unit, unit // 1.5))
coinBody.fill((230, 230, 10))

# fuelImg = pygame.image.load(os.path.join('data', 'D:/3 other/programming/Python/pygame/coin runner/fuel2.png'))      rip fuel - the thing that I couldn't manage making the collision for it lol (maybe later)

coinBodyX = 0
coinBodyX2 = 0
coinBodyY = 0
coinDY = unit * 0.1
coinRandom = True
        
coinBody2 = pygame.Surface((unit // 1.5, unit))
coinBody2.fill((230, 230, 10))

clock = pygame.time.Clock()
speed = 20

font = pygame.font.Font("freesansbold.ttf", unit // 2)
fontSmall = pygame.font.SysFont("couriernew", unit // 6)
fontBig = pygame.font.SysFont("couriernew", unit)

car = []

carPosition = 0
coinPosition = 0

coins = 0

touchingCoin = False

welcome = True
playing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                playing = True
            if event.key == pygame.K_RIGHT:
                carDX = unit * 0.1
            if event.key == pygame.K_LEFT:
                carDX = -unit * 0.1
            if event.key == pygame.K_UP:
                carDX = 0

    welcomeTxt = fontBig.render("welcome to coin runner", True, (0, 0, 255))
    welcomePressSpace = fontSmall.render("press space to continue", True, (50, 50, 255))

    if welcome:
        screen.fill((0, 0, 0))
        screen.blit(welcomeTxt, (unit * 1.35, size_y * unit // 3))
        screen.blit(welcomePressSpace, (size_x * unit // 2.5, size_y * unit // 2))

    if playing:
        speed += 0.01

        if coinRandom:
            coinBodyX2 = random.randint(1, 3)
            coinRandom = False
        if coinBodyY > size_x * unit - unit * 2:
            coinRandom = True

        if coinBodyX2 == 1:
            coinBodyX = unit * 5.25
        if coinBodyX2 == 2:
            coinBodyX = unit * 7.75
        if coinBodyX2 == 3:
            coinBodyX = unit * 10.25

        if coinBodyY == size_x * unit - unit:
            coinBodyY = -unit
            
        coinPosition = coinBodyX2

        screen.fill((0, 0, 0))

        coinsTxt = fontSmall.render(f"coins: {coins}", True, (230, 230, 10))
        screen.blit(coinsTxt, (unit * 2, unit))

        screen.blit(coinBody, (coinBodyX, coinBodyY))
        screen.blit(coinBody2, (coinBodyX + unit * 0.15, coinBodyY - unit * 0.2))

        screen.blit(lines, (size_x * unit // 2 - unit, 0))
        screen.blit(lines, (size_x * unit // 2 + unit * 1.5, 0))
        screen.blit(lines, (size_x * unit // 2 - unit * 3.5, 0))
        screen.blit(lines, (size_x * unit // 2 + unit * 4, 0))
        screen.blit(carWheels, (carX - unit * 0.15, carY + unit * 0.6))
        screen.blit(carWheels, (carX - unit * 0.15, carY + unit * 1.3))
        screen.blit(carWheels, (carX + unit * 1.50, carY + unit * 0.6))
        screen.blit(carWheels, (carX + unit * 1.50, carY + unit * 1.3))
        screen.blit(carLights, (carX + unit * 0.15, carY - unit * 0.15))
        screen.blit(carLights, (carX + unit, carY - unit * 0.15))
        screen.blit(carBody, (carX, carY))
        screen.blit(carBody2, (carX - unit * 0.08, carY + unit * 0.5))

        carX += carDX
        coinBodyY += coinDY

        if carX == size_x * unit // 4 + unit:
            carDX = 0
            carPosition = 1
        if carX == unit * 10:
            carDX = 0
            carPosition = 3
        if carX == unit * 7.5:
            carDX = 0
            carPosition = 2

        if coinPosition == carPosition:
            if coinBodyY - unit * 0.2 + unit == carY:
                touchingCoin = True
                coins += 1
                touchingCoin = False

        print(coins, touchingCoin)


    clock.tick(speed)
    pygame.display.update()