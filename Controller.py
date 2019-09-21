import sys
import pygame
import random



class Controller:
    def __init__(self, width=640*2+160, height=480*2):
        pygame.init()
        self.country_values = [["USA", 350000, 355000, 1000000, 40, 35, 15, 20, 5, 20, [-1, 1, 0, 0, 0, 0]],
                               ["UK", 100000, 102500, 125000, 15, 20, 5, 35, 30, 35, [1, -1, 0, 0, 0, 0]],
                               ["Russia", 500000, 475000, 500000, 50, 20, 30, 5, 0, 15, [0, 0, -1, 1, 0, 0]],
                               ["Korea", 150000, 140000, 170000, 25, 20, 10, 25, 10, 15, [0, 0, 1, -1, 0, 0]],
                               ["China", 1500000, 1500000, 1600000, 20, 25, 20, 10, 5, 45, [0, 0, 0, 0, -1, 1]],
                               ["Pakistan", 200000, 215000, 201250, 15, 15, 15, 40, 25, 30, [0, 0, 0, 0, 1, -1]]]
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "START2"
        pygame.font.init()

    def mainLoop(self):     ####Runs the function that is the part of the game we want to be running at any given time
        while True:
            if(self.state == "START1"):
                self.startLoop1()
            elif(self.state == "START2"):
                self.startLoop2()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def startLoop1(self):
        pygame.key.set_repeat(1,50)
        b1x = 150
        b1y = 560
        b2x = 1090
        b2y = 560
        while(self.state == "START1"):
            background = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg").convert_alpha(),(640*2+160, 480*2))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            font = pygame.font.SysFont("arial", 40, True)
            title = font.render('Cold War!', True, (250,250,250))
            self.screen.blit(title, (630,100))
            pygame.draw.rect(self.screen, (80,208,255), (b1x,b1y,200,100)) #quit ((RGB)(x, y, length x, length y))
            pygame.draw.rect(self.screen, (0,192,0), (b2x,b2y,200,100)) #play
            font = pygame.font.SysFont("arial", 45, True)
            start_button = font.render('PLAY', True, (0,0,0))
            self.screen.blit(start_button, (b2x+57,b2y+35))
            quit_button = font.render('QUIT', True, (0,0,0))
            self.screen.blit(quit_button, (b1x+57,b2y+35))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            if click[0] == 1 and mouse[0] in range(b1x,b1x+200) and mouse[1] in range(b1y,b1y+100):
                sys.exit()
            if click[0] == 1 and mouse[0] in range(b2x,b2x+200) and mouse[1] in range(b2y,b2y+100):
                self.state = "START2"
            pygame.display.flip()


    def startLoop2(self):
        b1x = 145
        b1y = 560
        b2x = 1090
        b2y = 560
        pygame.key.set_repeat(1,50)
        while(self.state == "START2"):
            background = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg").convert_alpha(),(640*2+160, 480*2))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            font = pygame.font.SysFont("arial", 40, True)
            title = font.render('Cold War!', True, (250,250,250))
            self.screen.blit(title, (630,100))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b1y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))

            font = pygame.font.SysFont("arial", 30, True)
            start_button = font.render('Select Difficulty', True, (0,0,0))
            self.screen.blit(start_button, (485,415))
            quit_button = font.render('Pick a Country', True, (0,0,0))
            self.screen.blit(quit_button, (95,415))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            if click[0] == 1 and mouse[0] in range(440,590) and mouse[1] in range(400,450):
                self.state = "GAME"
            if click[0] == 1 and mouse[0] in range(50,200) and mouse[1] in range(400,450):
                sys.exit()
            pygame.display.flip()

    def gameLoop(self):
        sys.exit()

    def endLoop(self):
        pass
