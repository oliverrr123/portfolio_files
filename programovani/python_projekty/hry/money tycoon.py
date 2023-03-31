import pygame
import time

# functions

def buying(productNumber, price, money1, noMoney):
    if money < price:
        noMoney = True
    else:
        productNumber += 1
        money -= price    


# data vars

workerNum = 0
workerIncome = 1
workerPrice = 10

engineerNum = 0 
engineerIncome = 10
engineerPrice = 100

megaEngineerNum = 0
megaEngineerIncome = 100
megaEngineerPrice = 1000

lilFactoryNum = 0
lilFactoryIncome = 500
lilFactoryPrice = 10000

factoryNum = 0
factoryIncome = 1000
factoryPrice = 50000

bigFactoryNum = 0
bigFactoryIncome = 5000
bigFactoryPrice = 100000

money = 0
income = 1

# pygame vars

pygame.init()

unit = 100
size_x, size_y = 16, 9
screen = pygame.display.set_mode((size_x * unit, size_y * unit))

fontBig = pygame.font.Font("freesansbold.ttf", unit)
font = pygame.font.Font("freesansbold.ttf", unit // 2)
fontSmall = pygame.font.Font("freesansbold.ttf", unit // 4)

clock = pygame.time.Clock()

welcome = True
actuallPlaying = False
noMoney = 0
win = False

# game loop

running = True
while running:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                welcome = False
                actuallPlaying = True
            if event.key == pygame.K_1:
                if money < workerPrice:
                    noMoney = 2
                else:
                    workerNum += 1
                    money -= workerPrice
                    workerPrice = round(workerPrice * 1.25) 
            if event.key == pygame.K_2:
                if money < engineerPrice:
                    noMoney = 2
                else:
                    engineerNum += 1
                    money -= engineerPrice
                    engineerPrice = round(engineerPrice * 1.25)
            if event.key == pygame.K_3:
                if money < megaEngineerPrice:
                    noMoney = 2
                else:
                    megaEngineerNum += 1
                    money -= megaEngineerPrice
                    megaEngineerPrice = round(megaEngineerPrice * 1.25) 
            if event.key == pygame.K_4:
                if money < lilFactoryPrice:
                    noMoney = 2
                else:
                    lilFactoryNum += 1
                    money -= lilFactoryPrice 
                    lilFactoryPrice = round(lilFactoryPrice * 1.25)
            if event.key == pygame.K_5:
                if money < factoryPrice:
                    noMoney = 2
                else:
                    factoryNum += 1
                    money -= factoryPrice 
                    factoryPrice = round(factoryPrice * 1.25)
            if event.key == pygame.K_6:
                if money < bigFactoryPrice:
                    noMoney = 2
                else:
                    bigFactoryNum += 1
                    money -= bigFactoryPrice
                    bigFactoryPrice = round(bigFactoryPrice * 1.25)
                    win = True

    welcomeMainTxt = fontBig.render("Welcome to Money Tycoon!", True, (255, 255, 255))
    welcomePressToStartTxt = fontSmall.render("press space to start", True, (255, 255, 255))

    workerProfits = workerNum * workerIncome
    engineerProfits = engineerNum * engineerIncome
    megaEngineerProfits = megaEngineerNum * megaEngineerIncome
    lilFactoryProfits = lilFactoryNum * lilFactoryIncome
    factoryProfits = factoryNum * factoryIncome
    bigFactoryProfits = bigFactoryNum * bigFactoryIncome

    income = 1 + workerProfits + engineerProfits + megaEngineerProfits + lilFactoryProfits + factoryProfits + bigFactoryProfits
    money += income

    moneyTxt = font.render(f"Money:  {money}", True, (255, 255, 255))
    incomeTxt = font.render(f"Income: {income}/s", True, (255, 255, 255))

    shopTxt = font.render("--SHOP--", True, (255, 255, 255))

    shopWorkerTxt = font.render(f"1) worker - {workerPrice}$ - 1$/s - ({workerNum})", True, (255, 255, 255))
    shopEngineerTxt = font.render(f"2) engineer - {engineerPrice}$ - 10$/s - ({engineerNum})", True, (255, 255, 255))
    shopMegaEngineerTxt = font.render(f"3) mega engineer - {megaEngineerPrice}$ - 100$/s - ({megaEngineerNum})", True, (255, 255, 255))
    shopLilFactoryTxt = font.render(f"4) lil factory - {lilFactoryPrice}$ - 500$/s - ({lilFactoryNum})", True, (255, 255, 255))
    shopFactoryTxt = font.render(f"5) factory - {factoryPrice}$ - 1,000$/s - ({factoryNum})", True, (255, 255, 255))
    shopBigFactoryTxt = font.render(f"6) big factory - {bigFactoryPrice}$ - 5,000$/s - ({bigFactoryNum})", True, (255, 255, 255))

    buyTxt = fontSmall.render("to buy a product, press it's number on the keyboard", True, (255, 255, 255))

    noMoneyTxt = fontSmall.render("you don't have enough money!", True, (255, 255, 255))

    winTxt = font.render("You Won!", True, (255, 255, 255))
    winKeepPlayingTxt = fontSmall.render("You can still keep playing if u want :D", True, (255, 255, 255))



    if welcome:
        screen.blit(welcomeMainTxt, (unit * 1.3, size_y * unit // 4))
        screen.blit(welcomePressToStartTxt, (size_x * unit // 2.5, size_y * unit // 2))

    if actuallPlaying:
        screen.fill((0, 0, 0))
        screen.blit(moneyTxt, (unit * 1.3, unit))
        screen.blit(incomeTxt, (unit * 1.3, unit * 1.5))
        screen.blit(shopTxt, (unit * 1.3, unit * 3.5))
        screen.blit(shopWorkerTxt, (unit * 1.3, unit * 4.5))
        screen.blit(shopEngineerTxt, (unit * 1.3, unit * 5))
        screen.blit(shopMegaEngineerTxt, (unit * 1.3, unit * 5.5))
        screen.blit(shopLilFactoryTxt, (unit * 1.3, unit * 6))
        screen.blit(shopFactoryTxt, (unit * 1.3, unit * 6.5))
        screen.blit(shopBigFactoryTxt, (unit * 1.3, unit * 7))
        screen.blit(buyTxt, (unit * 1.3, unit * 8))

    if noMoney > 0:
        screen.blit(noMoneyTxt, (size_x * unit // 2, unit))
        noMoney -= 1
        
    if win:
        screen.blit(winTxt, (size_x * unit // 2, unit * 2))
        screen.blit(winKeepPlayingTxt, (size_x * unit // 2, unit * 2.5))

    clock.tick(20)
    pygame.display.update()
    