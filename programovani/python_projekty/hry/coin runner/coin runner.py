import pygame
import tkinter as tk
import random
import os
import sqlite3
        
# --FUNCTIONS--

def screenSwitch(value, window):
    global currentWindow, welcome, menu, shop, achievements, howToPlay, playing, welcomeWindow, menuWindow, shopWindow, achievementsWindow
    currentWindow = value
    window.destroy()

# def screenSwitch(what):
#     global welcome, menu, shop, achievements, howToPlay, playing, welcomeWindow, menuWindow, shopWindow, achievementsWindow

#     screenSwitchCreate("welcome, menu", welcome, menu, welcomeWindow, what)
#     screenSwitchCreate("menu, shop", menu, shop, menuWindow, what)
#     screenSwitchCreate("menu, achievements", menu, achievements, menuWindow, what)
#     screenSwitchCreate("menu, howToPlay", menu, howToPlay, menuWindow, what)
#     screenSwitchCreate("shop, menu", shop, menu, shopWindow, what)
#     screenSwitchCreate("shop, achievements", shop, achievements, shopWindow, what)
#     screenSwitchCreate("shop, howToPlay", shop, howToPlay, shopWindow, what)
#     screenSwitchCreate("achievements, menu", achievements, menu, achievementsWindow, what)
#     screenSwitchCreate("achievements, shop", achievements, shop, achievementsWindow, what)
#     screenSwitchCreate("achievements, howToPlay", achievements, howToPlay, achievementsWindow, what)
#     screenSwitchCreate("howToPlay, menu", howToPlay, menu, howToPlayWindow, what)
#     screenSwitchCreate("howToPlay, shop", howToPlay, shop, howToPlayWindow, what)
#     screenSwitchCreate("howToPlay, achievements", howToPlay, achievements, howToPlayWindow, what)
#     screenSwitchCreate("menu, playing", menu, playing, menuWindow, what)

    # if what == "welcome, menu":
    #     welcome = False
    #     menu = True
    #     welcomeWindow.destroy()
    # if what == "menu, shop":
    #     menu = False
    #     shop = True
    #     menuWindow.destroy()
    # if what == "menu, achievements":
    #     menu = False
    #     achievements = True
    #     menuWindow.destroy()
    # if what == "shop, menu":
    #     shop = False
    #     menu = True
    #     shopWindow.destroy()
    # if what == "shop, achievements":
    #     shop = False
    #     achievements = True
    #     shopWindow.destroy()
    # if what == "achievements, menu":
    #     achievements = False
    #     menu = True
    #     achievementsWindow.destroy()  
    # if what == "achievements, shop":
    #     achievements = False
    #     shop = True
    #     achievementsWindow.destroy()
    # if what == "menu, playing":
    #     menu = False
    #     playing = True
    #     menuWindow.destroy()

def sidebarMake(shop, shopParameters, achievements, howToPlay, switch):
    global coins, sidebar, coinsTxt, shopButton, buttonsSpacing, achievementsButton, howToPlayButton, sidebarSpacing
    
    sidebar = tk.Frame(bg="#585858", height=100, width=50)
    coinsTxtTk = tk.Label(sidebar, text=f"coins: {coins}", bg="#585858", fore="#e6e60a", font=("Courier", 30), height=10, width=10)
    shopButton = tk.Button(sidebar, text="shop", bg="#c3c3c3", font=("Courier", 20), height=1, width=10) # command=lambda *args: screenSwitch("menu, shop")
    # buttonsSpacing = tk.Label(sidebar, text=" ", height=1, bg="#585858")
    # buttonsSpacing2 = tk.Label(sidebar, text=" ", height=1, bg="#585858")
    # buttonsSpacing3 = tk.Label(sidebar, text=" ", height=3, bg="#585858")
    achievementsButton = tk.Button(sidebar, text="achievements", bg="#c3c3c3", font=("Courier", 10), height=2, width=20)
    howToPlayButton = tk.Button(sidebar, text="how to play", bg="#c3c3c3", font=("Courier", 10), height=2, width=20)
    loginButton = tk.Button(sidebar, text="log  in", bg="#c3c3c3", font=("Courier", 10))
    signupButton = tk.Button(sidebar, text="sign up", bg="#c3c3c3", font=("Courier", 10))
    quitButton = tk.Button(sidebar, text="QUIT", bg="#ff0000", font=("Courier", 10), height=2, width=15)
    sidebarSpacing = tk.Label(sidebar, bg="#585858", text=" ", width=10, height=30)

    sidebar.pack(side=tk.LEFT)

    coinsTxtTk.pack()
    shopButton.pack(pady=(0, 10))
    shopButton.configure(text=shop, font=("Courier", shopParameters[0]), height=shopParameters[1], width=shopParameters[2], command=lambda *args: screenSwitch(switch[0][0], switch[0][1]))
    achievementsButton.pack(pady=(0, 10))
    achievementsButton.configure(text=achievements, command=lambda *args: screenSwitch(switch[1][0], switch[1][1]))
    howToPlayButton.pack(pady=(0, 30))
    howToPlayButton.configure(text=howToPlay, command=lambda *args: screenSwitch(switch[2][0], switch[2][1]))
    loginButton.configure(command=lambda *args: screenSwitch(switch[3][0], switch[3][1]))
    loginButton.pack()
    signupButton.configure(command=lambda *args: screenSwitch(switch[4][0], switch[4][1]))
    signupButton.pack()
    quitButton.pack(side=tk.BOTTOM)
    quitButton.configure(command=lambda *args: screenSwitch(" ", switch[0][1]))
    sidebarSpacing.pack()

def getData():
    global nickNameEntry, passWordEntry, connection, cursor, users, sameDataCheck1, sameDataCheck2
    cursor = connection.cursor()
    sameDataCheck1 = cursor.execute('SELECT * FROM data WHERE nick = ?', (nickNameEntry.get(),))
    sameDataCheck2 = cursor.execute('SELECT * FROM data WHERE passW = ?', (passWordEntry.get(),))
    print(sameDataCheck1, sameDataCheck2)
    cursor.fetchone()
    if sameDataCheck1 == "":
        print("hehe")
        if sameDataCheck2 == "":
            print("hehe2")
            cursor = connection.cursor()
            cursor.execute('INSERT INTO data (nick, passW) VALUES (?, ?)', (nickNameEntry.get(), passWordEntry.get()))
            connection.commit()
            for user in users:
                print(user[0], " ", user[1])

    
    

# --TKINTER VARS--

currentWindow = "welcome"

# --SQL--

connection = sqlite3.connect('coinRunnerDataDB.db')

cursor = connection.cursor()
cursor.execute('create table if not exists data (nick TEXT, passW TEXT)')
connection.commit()

users = cursor.execute('SELECT * FROM data')

sameDataCheck1 = ""
sameDataCheck2 = ""


# playing = False
# welcome = True
# menu = False
# shop = False
# achievements = False
# howToPlay = False

# --PYGAME VARS--

pygame.init()

size_x, size_y = 16, 9
unit = 100

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

# fuelImg = pygame.image.load(os.path.join('data', 'D:/3 other/programming/Python/pygame/coin runner/fuel2.png'))      rip fuel - the thing that I couldn't manage making the collision for it lol (maybe later)

# --COIN SURFACES & VARS--

coinBody = pygame.Surface((unit, unit // 1.5))
coinBody.fill((230, 230, 10))

coinBodyX = 0
coinBodyX2 = 0
coinBodyY = 0
coinDY = unit * 0.1
coinRandom = True
        
coinBody2 = pygame.Surface((unit // 1.5, unit))
coinBody2.fill((230, 230, 10))

# --BOMB SURFACES & VARS--

bombBody = pygame.Surface((unit, unit // 1.5))
bombBody.fill((58, 58, 58))

bombBodyX = 0
bombBodyX2 = 0
bombBodyY = -size_y * unit
bombDY = unit * 0.1
bombRandom = True

bombBody2 = pygame.Surface((unit // 1.5, unit))
bombBody2.fill((58, 58, 58))

bombRope = pygame.Surface((unit * 0.05, unit * 0.2))
bombRope.fill((255, 255, 255))

bombRope2 = pygame.Surface((unit * 0.2, unit * 0.05))
bombRope2.fill((255, 255, 255))

bombFire = pygame.Surface((unit * 0.15, unit * 0.15))
bombFire.fill((255, 0, 0))

# --OTHER PYGAME VARS--

clock = pygame.time.Clock()
speed = 20

font = pygame.font.Font("freesansbold.ttf", unit // 2)
fontSmall = pygame.font.SysFont("couriernew", unit // 6)
fontBig = pygame.font.SysFont("couriernew", unit)

carPosition = 0
coinPosition = 0
bombPosition = 0

touchingCoin = False
touchingBomb = False


death = False

screenCreate = True

mousePos = 0

coins = 0
playingCoins = 0

# ------------
# --GAMELOOP--
# ------------

running = True

while running:
    # --TKINER (MENU)--

    if currentWindow == "welcome":
        welcomeWindow = tk.Tk()
        welcomeWindow.configure(bg="black")
        welcomeWindow.attributes("-fullscreen", True)
        welcomeTxtTk = tk.Label(text="Welcome to Coin Runner!", font=("Courier", 50), height=8, width=100, bg="black", fore="white")
        welcomeTxtTk.pack()
        welcomeButtonTk = tk.Button(text="click to continue", font=("Courier", 10), height=2, highlightbackground="black", fore="black", command=lambda *args: screenSwitch("menu", welcomeWindow))
        welcomeButtonTk.pack()
        tk.mainloop()
        

    if currentWindow == "menu":
        menuWindow = tk.Tk()
        menuWindow.configure(bg="black")
        menuWindow.attributes("-fullscreen", True)
        sidebarMake("shop", (20, 1, 10), "achievements", "how to play", (("shop", menuWindow), ("achievements", menuWindow), ("howToPlay", menuWindow), ("login", menuWindow), ("signup", menuWindow)))
        coinRunnerTxt = tk.Label(text="coin runner", font=("Courier", 70), bg="black", fore="white", height=3)
        coinRunnerTxt.pack()
        startButton = tk.Button(text="START!", bg="#00ff00", fore="black", font=("Courier", 50), command=lambda *args: screenSwitch("playing", menuWindow))
        startButton.pack()
        tk.mainloop()

    if currentWindow == "shop":
        shopWindow = tk.Tk()
        shopWindow.configure(bg="black")
        shopWindow.attributes("-fullscreen", True)
        sidebarMake("back to menu", (10, 2, 20), "achievements", "how to play", (("menu", shopWindow), ("achievements", shopWindow), ("howToPlay", shopWindow), ("login", shopWindow), ("signup", shopWindow)))
        tk.mainloop()

    if currentWindow == "achievements":
        achievementsWindow = tk.Tk()
        achievementsWindow.configure(bg="black")
        achievementsWindow.attributes("-fullscreen", True)
        sidebarMake("shop", (20, 1, 10), "back to menu", "how to play", (("shop", achievementsWindow), ("menu", achievementsWindow), ("howToPlay", achievementsWindow), ("login", achievementsWindow), ("signup", achievementsWindow)))
        tk.mainloop()

    if currentWindow == "howToPlay":
        howToPlayWindow = tk.Tk()
        howToPlayWindow.configure(bg="black")
        howToPlayWindow.attributes("-fullscreen", True)
        sidebarMake("shop", (20, 1, 10), "achievements", "back to menu", (("shop", howToPlayWindow), ("achievements", howToPlayWindow), ("menu", howToPlayWindow), ("login", howToPlayWindow), ("signup", howToPlayWindow)))
        tk.mainloop()        

    if currentWindow == "login":
        loginWindow = tk.Tk()
        loginWindow.configure(bg="black")
        loginWindow.attributes("-fullscreen", True)
        nickNameEntry = tk.Entry(bg="#c3c3c3", font=("Courier", 50))
        passWordEntry = tk.Entry(bg="#c3c3c3", font=("Courier", 50))
        confirmButton = tk.Button(text="confirm", bg="#00ff00", font=("Courier", 30), command=getData)
        back = tk.Button(text="back", bg="#585858", font=("Courier", 15), command=lambda *args: screenSwitch("menu", loginWindow))
        nickNameEntry.pack(pady=(400, 20))
        passWordEntry.pack(pady=(0, 50))
        confirmButton.pack()
        back.pack(side=tk.BOTTOM)
        print(nickNameEntry.get())
        print(passWordEntry.get())
        tk.mainloop()

    if currentWindow == "signup":
        signupWindow = tk.Tk()
        signupWindow.configure(bg="black")
        signupWindow.attributes("-fullscreen", True)
        nickNameEntry = tk.Entry(bg="#c3c3c3", font=("Courier", 50))
        passWordEntry = tk.Entry(bg="#c3c3c3", font=("Courier", 50))
        confirmButton = tk.Button(text="confirm", bg="#00ff00", font=("Courier", 30), command=getData)
        back = tk.Button(text="back", bg="#585858", font=("Courier", 15), command=lambda *args: screenSwitch("menu", signupWindow))
        nickNameEntry.pack(pady=(400, 20))
        passWordEntry.pack(pady=(0, 50))
        confirmButton.pack()
        back.pack(side=tk.BOTTOM)
        tk.mainloop()

    # --PYGAME (ACTUALL GAME)--

    if currentWindow == "playing":
        # --EVENTS--
        if screenCreate:
            screen = pygame.display.set_mode((size_x * unit, size_y * unit))
            screenCreate = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if death:
                        death = False
                        coins += playingCoins
                        playingCoins = 0
                        speed = 20
                        coinBodyY = 0
                        coinDY = unit * 0.1
                        coinRandom = True
                        bombBodyY = -size_y * unit
                        bombDY = unit * 0.1
                        bombRandom = True
                        carPosition = 2
                        carX = unit * 7.5
                        currentWindow = "menu"
                        playing = False
                if event.key == pygame.K_RIGHT:
                    if carPosition != 3:
                        carDX = unit * 0.1
                if event.key == pygame.K_LEFT:
                    if carPosition != 1:
                        carDX = -unit * 0.1
                if event.key == pygame.K_UP:
                    carDX = 0
            # if event.type == pygame.MOUSEBUTTONUP:
            #     mousePos = pygame.mouse.get_pos()

        # --welcome in 1.0--
        # welcomeTxt = fontBig.render("welcome to coin runner", True, (0, 0, 255))
        # welcomePressSpace = fontSmall.render("press space to continue", True, (50, 50, 255))

        # if welcome:
        #     screen.fill((0, 0, 0))
        #     screen.blit(welcomeTxt, (unit * 1.35, size_y * unit // 3))
        #     screen.blit(welcomePressSpace, (size_x * unit // 2.5, size_y * unit // 2))

        # --BACKEND--

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


        if bombRandom:
            bombBodyX2 = random.randint(1, 3)
            bombRandom = False
        if bombBodyY > size_x * unit - unit * 2:
            bombRandom = True

        if bombBodyX2 == 1:
            bombBodyX = unit * 5.25
        if bombBodyX2 == 2:
            bombBodyX = unit * 7.75
        if bombBodyX2 == 3:
            bombBodyX = unit * 10.25

        if bombBodyY == size_x * unit - unit:
            bombBodyY = -size_y * unit
            
        bombPosition = bombBodyX2

        if death:
            carDX = 0
            coinDY = 0
            bombDY = 0

        # --BLITTING--

        screen.fill((0, 0, 0))

        coinsTxt = fontSmall.render(f"coins: {playingCoins}", True, (230, 230, 10))
        screen.blit(coinsTxt, (unit * 2, unit))

        screen.blit(coinBody, (coinBodyX, coinBodyY))
        screen.blit(coinBody2, (coinBodyX + unit * 0.15, coinBodyY - unit * 0.2))

        screen.blit(bombRope, (bombBodyX + unit // 2.50 + unit * 0.05, bombBodyY - unit * 0.4))
        screen.blit(bombRope2, (bombBodyX + unit // 2.50 + unit * 0.05, bombBodyY - unit * 0.4))
        screen.blit(bombFire, (bombBodyX + unit // 2.50 + unit * 0.2, bombBodyY - unit * 0.45))
        screen.blit(bombBody, (bombBodyX, bombBodyY))
        screen.blit(bombBody2, (bombBodyX + unit * 0.15, bombBodyY - unit * 0.2))

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

        if death:
            deathTxt = fontBig.render("You Died!", True, (255, 0, 0))
            screen.blit(deathTxt, (size_x * unit // 3, size_y * unit // 3))
            coinsCollectedTxt = font.render(f"coins collected: {playingCoins}", True, (230, 230, 10))
            screen.blit(coinsCollectedTxt, (size_x * unit // 2 - unit * 2, size_y * unit // 2))
            backToMenuDeathText = fontSmall.render("press space to go back to menu", True, (255, 255, 255))
            screen.blit(backToMenuDeathText, (size_x * unit // 2 - unit * 1.5, size_y * unit // 2 + unit))


        # --ANOTHER BACKEND--

        carX += carDX
        coinBodyY += coinDY
        bombBodyY += bombDY

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
                playingCoins += 1
                touchingCoin = False

        if bombPosition == carPosition:
            if bombBodyY - unit * 0.2 == carY:
                touchingBomb = True
                death = True
                carDX = 0
                coinDY = 0
                bombDY = 0
                touchingBomb = False

        # col1 = pygame.sprite.collide_rect(coinBody, carBody)
        # col2 = pygame.sprite.collide_rect(coinBody2, carBody2)
        print(touchingCoin)

        # --THE END--

        clock.tick(speed)
        pygame.display.update()