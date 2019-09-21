import sys
import pygame
import random

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "START"
        # self.all_sprites =
        pygame.font.init()

        def mainLoop(self):     ####Runs the function that is the part of the game we want to be running at any given time
        while True:
            if(self.state == "START1"):
                self.startLoop()
            elif(self.state == "START2"):
                self.startLoop2()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

        def startLoop():
            pygame.key.set_key(1,50)
            while(self.state == "START1"):
                

        def startLoop2():
            pass

        def gameLoop():
            pass

        def endLoop():
            pass
