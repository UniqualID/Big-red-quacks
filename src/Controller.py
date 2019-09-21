import sys
import pygame
import random

WIDTH = 640
HEIGHT = 480

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "START1"
        # self.all_sprites =
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

    def startLoop1():
        pygame.key.set_repeat(1,50)
        while(self.state == "START1"):
            background = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg").convert_alpha(),(WIDTH, HEIGHT))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            font = pygame.font.SysFont("arial", 40, True)
            title = font.render('Cold War!', True, (250,250,250))
            self.screen.blit(title, (100,100))
            pygame.draw.rect(self.screen, (80,208,255), (50,400,150,50)) #quit
            pygame.draw.rect(self.screen, (0,192,0), (440,400,150,50)) #start
            font = pygame.font.SysFont("arial", 30, True)
            start_button = font.render('PLAY', True, (0,0,0))
            self.screen.blit(start_button, (485,415))
            quit_button = font.render('QUIT', True, (0,0,0))
            self.screen.blit(quit_button, (95,415))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            if click[0] == 1 and mouse[0] in range(440,590) and mouse[1] in range(400,450):
                self.state = "GAME"
            if click[0] == 1 and mouse[0] in range(50,200) and mouse[1] in range(400,450):
                sys.exit()
            pygame.display.flip()


    def startLoop2():
        pygame.key.set_repeat(1,50)
        while(self.state == "START2"):
            pass

    def gameLoop():
        sys.exit()

    def endLoop():
        pass
