import sys
import pygame
import time
import helper_functions
from PlayerCountry import PlayerCountry



class Controller:
    def __init__(self, width=640*2+160, height=480*2):
        pygame.init()

        # IN ORDER:             Name, population, cReasources, gRate, GDP, gpdGrowth, nukes, antiair, food production, treasury, #nukes, faValues]
        self.country_values = [["USA", 350000000, 350000000, 1.05, 1000000, 1.03, 0, 0, 0, 1000000*5, 0, {"USA" : -1, "UK" : 1, "Russia" : 0, "Korea" : 0, "China" : 0, "Pakistan" : 0}],
                               ["UK", 66000000, 66250000, 1.04, 250000, 1.02, 0, 0, 0, 250000*5, 0, {"USA" : 1, "UK" : -1, "Russia" : 0, "Korea" : 0, "China" : 0, "Pakistan" : 0}],
                               ["Russia", 145000000, 144500000, 1.08, 800000, 1.01, 0, 0, 0, 800000*5, 0, {"USA" : 0, "UK" : 0, "Russia" : -1, "Korea" : 1, "China" : 0, "Pakistan" : 0}],
                               ["China", 1400000000, 1400000000, 1.03, 700000, 1.04, 0, 0, 0, 700000*5, 0, {"USA" : 0, "UK" : 0, "Russia" : 0, "Korea" : 0, "China" : -1, "Pakistan" : 1}],
                               ["Pakistan", 200000000, 200000000, 1.09, 300000, 1.025, 0, 0, 0, 300000*5, 0, {"USA" : 0, "UK" : 0, "Russia" : 0, "Korea" : 0, "China" : 1, "Pakistan" : -1}],
                               ["Korea", 25000000, 24750000, 1.02, 100000, 1.02, 0, 0, 0, 100000*5, 0, {"USA" : 0, "UK" : 0, "Russia" : 1, "Korea" : -1, "China" : 0, "Pakistan" : 0}]]

        self.cities = { "USA" : { "Chicago" : [23333333.3, 0], "Salt Lake" : [23333333.3, 0], "Los Angeles" : [23333333.3, 0], "Jacksonville" : [23333333.3, 0], "Seattle" : [23333333.3, 0], "San Fransisco" : [23333333.3, 0], "Houston" : [23333333.3, 0], "Austin" : [23333333.3, 0], "Washington DC" : [23333333.3, 0], "Pheonix" : [23333333.3, 0], "St. Louis" : [23333333.3, 0], "Columbus" : [23333333.3, 0], "Charlotte" : [23333333.3, 0], "Denver" : [23333333.3, 0]},
                        "China" : { "Urumqi" : [233333333.3, 0], "Chengdu" : [233333333.3, 0], "Beijing" : [233333333.3, 0], "Guangzhou" : [233333333.3, 0], "Shanghai" : [233333333.3, 0], "Wuhan" : [233333333.3, 0]},
                        "Russia" : { "Moscow" : [18125000, 0], "St. Petersburg" : [18125000, 0], "Novosibirsk" : [18125000, 0], "Krasnoyarsk" : [18125000, 0], "Irkutsk" : [18125000, 0], "Arkhangel'sk" : [18125000, 0], "Magadan" : [18125000, 0]},
                        "Pakistan" : { "Islamabad" : [66666666.7, 0], "Karachi" : [66666666.7, 0], "Multan" : [66666666.7, 0]},
                        "UK" : {"London" : [33000000, 0], "Manchester" : [33000000, 0]},
                        "Korea" : {"Pyongyang" : [25000000, 0]}
                            }
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "START"
        pygame.font.init()
        self.player = None
        self.selected = -1
        self.selectedButton = -1


    def mainLoop(self):     ####Runs the function that is the part of the game we want to be running at any given time
        while True:
            if(self.state == "START"):
                self.startLoop()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def startLoop(self):
        b1x = 150
        b2x = 1090
        b2y = 460
        # self.selected = -1
        # self.selectedButton = -1
        pygame.key.set_repeat(1,50)

        music = pygame.mixer.Sound("assets/papers.wav")
        pygame.mixer.Sound.play(music)

        while(self.state == "START"):
            background = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg").convert_alpha(),(640*2+160, 480*2))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            title_img = pygame.transform.smoothscale(pygame.image.load("assets/title_img.jpg").convert_alpha(),(600,400))
            self.screen.blit(title_img, (400,-100))
            font = pygame.font.Font("assets/fonts/titleFont.ttf", 100)

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))


            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # font for buttons
            font = pygame.font.Font("assets/fonts/titleFont.ttf", 40)
            if self.selected == -1 or self.selectedButton == -1:
                pygame.draw.rect(self.screen, (88,88,88), (628,b2y+120,150,50))
            else:
                pygame.draw.rect(self.screen, (80,208,255), (628,b2y+120,150,50))
            self.screen.blit(font.render("Play", True, (0,0,0)), (650,b2y+118))
            if mouse[0] in range(628, 778) and mouse[1] in range(b2y+120,b2y+170):
                if self.selected != -1 and self.selectedButton != -1:
                    pygame.draw.rect(self.screen, (0,192,0), (628,b2y+120,150,50))
                    self.screen.blit(font.render("Play", True, (0,0,0)), (650,b2y+118))

            pygame.draw.rect(self.screen, (80,208,255), (628,b2y+220,150,50))
            self.screen.blit(font.render("Exit", True, (0,0,0)), (650,b2y+219))
            if mouse[0] in range(628, 778) and mouse[1] in range(b2y+220,b2y+270):
                pygame.draw.rect(self.screen, (0,192,0), (628,b2y+220,150,50))
                self.screen.blit(font.render("Exit", True, (0,0,0)), (650,b2y+219))

            pygame.draw.rect(self.screen, (80,208,255), (352,300,150,50))
            self.screen.blit(font.render("Easy", True, (0,0,0)), (375,301))
            if mouse[0] in range(352, 502) and mouse[1] in range(300,350):
                pygame.draw.rect(self.screen, (0,192,0), (352,300,150,50))
                self.screen.blit(font.render("Easy", True, (0,0,0)), (375,301))
                if click[0] == 1:
                    self.selectedButton = 0

            pygame.draw.rect(self.screen, (80,208,255), (608,300,200,50))
            self.screen.blit(font.render("Medium", True, (0,0,0)), (620,301))
            if mouse[0] in range(608, 808) and mouse[1] in range(300,350):
                pygame.draw.rect(self.screen, (0,192,0), (608,300,200,50))
                self.screen.blit(font.render("Medium", True, (0,0,0)), (620,301))
                if click[0] == 1:
                    self.selectedButton = 1

            pygame.draw.rect(self.screen, (80,208,255), (898,300,150,50))
            self.screen.blit(font.render("Hard", True, (0,0,0)), (920,301))
            if mouse[0] in range(898, 1048) and mouse[1] in range(300,350):
                pygame.draw.rect(self.screen, (0,192,0), (898,300,150,50))
                self.screen.blit(font.render("Hard", True, (0,0,0)), (920,301))
                if click[0] == 1:
                    self.selectedButton = 2

            #If button is selected, keep button green
            if self.selectedButton == 0:
                pygame.draw.rect(self.screen, (0,192,0), (352,300,150,50))
                self.screen.blit(font.render("Easy", True, (0,0,0)), (375,301))
            if self.selectedButton == 1:
                pygame.draw.rect(self.screen, (0,192,0), (608,300,200,50))
                self.screen.blit(font.render("Medium", True, (0,0,0)), (620,301))
            if self.selectedButton == 2:
                pygame.draw.rect(self.screen, (0,192,0), (898,300,150,50))
                self.screen.blit(font.render("Hard", True, (0,0,0)), (920,301))


            font = pygame.font.Font("assets/fonts/pixelplay.ttf", 30)
            start_button = font.render('Select Difficulty', True, (0,0,0))
            self.screen.blit(start_button, (605,215))
            quit_button = font.render('Pick a Country', True, (0,0,0))
            self.screen.blit(quit_button, (615,415))
            click = pygame.mouse.get_pressed() #tuple postition


            #I CAN SEE YOUR HALO HALO HALO!!!
            if mouse[0] in range(b1x, b1x + 100) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x-65, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b2y))
                if click[0] == 1:
                    self.selected = 0
            if mouse[0] in range(b1x + 200, b1x + 100 + 200) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x-65 + 200, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
                if click[0] == 1:
                    self.selected = 1
            if mouse[0] in range(b1x + 400, b1x + 100 + 400) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 400, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
                if click[0] == 1:
                    self.selected = 2
            if mouse[0] in range(b1x + 600, b1x + 100 + 600) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 600, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
                if click[0] == 1:
                    self.selected = 3
            if mouse[0] in range(b1x + 800, b1x + 100 + 800) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 800, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
                if click[0] == 1:
                    self.selected = 4
            if mouse[0] in range(b1x + 1000, b1x + 100 + 1000) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 1000, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))
                if click[0] == 1:
                    self.selected = 5

            if self.selected == 0:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x-65, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b2y))
            elif self.selected == 1:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x-65 + 200, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
            elif self.selected == 2:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 400, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
            elif self.selected == 3:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 600, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
            elif self.selected == 4:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 800, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
            elif self.selected == 5:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.jpg").convert_alpha(), (225, 175)), (b1x - 65 + 1000, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))


            if click[0] == 1 and mouse[0] in range(628,778) and mouse[1] in range(b2y+220,b2y+270):
                sys.exit()
            if click[0] == 1 and mouse[0] in range(628,728) and mouse[1] in range(b2y+120,b2y+170) and self.selected != -1 and self.selectedButton != -1:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.jpg").convert_alpha(),(100,100)), (0,0))
                self.state = "GAME"

            pygame.event.wait()
            pygame.display.flip()


    def startHud(self, player, turns):
        font = pygame.font.Font("assets/fonts/pixelplay.ttf", 30)
        self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/hud_final.png").convert_alpha(),(1440,580)), (0,280))

        if self.selected == 0:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/US_hud.jpg").convert_alpha(), (195,195)), (20,685))
        elif self.selected == 1:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/UK_hud.jpg").convert_alpha(), (195,195)), (20,685))
        elif self.selected == 2:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Russia_hud.jpg").convert_alpha(), (195,195)), (20,685))
        elif self.selected == 3:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/China_hud.jpg").convert_alpha(), (195,195)), (20,685))
        elif self.selected == 4:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_hud.jpg").convert_alpha(), (195,195)), (20,685))
        elif self.selected == 5:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/NK_hud.jpg").convert_alpha(), (195,195)), (20,685))

        boxX = 470
        boxY = 740
        # pygame.draw.rect(self.screen, (0,191,0), (boxX,boxY+15,370,83))
        self.screen.blit(font.render(player.name, True, (255,255,255)), (boxX, boxY-45))
        self.screen.blit(font.render(str(player.population), True, (255,255,255)), (boxX+50, boxY+10))
        self.screen.blit(font.render("pop.",True, (255,255,255)), (boxX, boxY+10))
        self.screen.blit(font.render(str(player.cResources), True, (255,255,255)), (boxX+50, boxY+35))
        self.screen.blit(font.render("res.",True, (255,255,255)), (boxX, boxY+35))
        self.screen.blit(font.render(str(player.GDP), True, (255,255,255)), (boxX+50, boxY+60))
        self.screen.blit(font.render("gdp.",True, (255,255,255)), (boxX, boxY+60))
        self.screen.blit(font.render(str(player.fProduction), True, (255,255,255)), (boxX+350, boxY+10))
        self.screen.blit(font.render("food prod.",True, (255,255,255)), (boxX+200, boxY+10))
        self.screen.blit(font.render(str(player.nukes), True, (255,255,255)), (boxX+350, boxY+35))
        self.screen.blit(font.render("nukes",True, (255,255,255)), (boxX+200, boxY+35))
        self.screen.blit(font.render(str(player.faValues[player.name]), True, (255,255,255)), (boxX+350, boxY+60))
        self.screen.blit(font.render("foregn aff.",True, (255,255,255)), (boxX+200, boxY+60))





    def gameLoop(self):
        pygame.key.set_repeat(1,50)
        self.player = PlayerCountry(self.country_values[self.selected][0], self.country_values[self.selected][1], self.country_values[self.selected][2], self.country_values[self.selected][3], self.country_values[self.selected][4], self.country_values[self.selected][5], self.country_values[self.selected][6], self.country_values[self.selected][7], self.country_values[self.selected][8], self.country_values[self.selected][9], self.country_values[self.selected][10], self.country_values[self.selected][11],self.cities[self.country_values[self.selected][0]])
        allPlayers = [self.player]
        for i in range(6):
            if i != self.selected:
                allPlayers.append(PlayerCountry(self.country_values[i][0], self.country_values[i][1], self.country_values[i][2], self.country_values[i][3], self.country_values[i][4], self.country_values[i][5], self.country_values[i][6], self.country_values[i][7], self.country_values[i][8], self.country_values[i][9], self.country_values[i][10], self.country_values[i][11],self.cities[self.country_values[i][0]]))
        turns = 0
        cityselection = -1
        font = pygame.font.Font("assets/fonts/pixelplay.ttf", 30)
        #ayy weed lmao
        while self.state == "GAME":
            background = pygame.transform.smoothscale(pygame.image.load("assets/map.jpg").convert_alpha(),(640*2+160, 480*2))
            self.screen.blit(background, (0,0))
            self.startHud(self.player, turns)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (385,285)) #NYC
            if click[0] == 1 and mouse[0] in range(385,600) and mouse[1] in range(285,600):
                # pygame.draw(rect.screen, (0,0,0), ())
                self.screen.blit(font.render("NYC", True, (0,0,0)), (375,301))
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (333,285)) #Chicago
            if click[0] == 1 and mouse[0] in range(333,346) and mouse[1] in range(220,270):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (363,300)) #DC
            if click[0] == 1 and mouse[0] in range(363,376) and mouse[1] in range(300,313):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (213,300)) #SLC
            if click[0] == 1 and mouse[0] in range(213,226) and mouse[1] in range(300,313):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (183,315)) #LA
            if click[0] == 1 and mouse[0] in range(183,196) and mouse[1] in range(315,328):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (340,335)) #Jacksonville
            if click[0] == 1 and mouse[0] in range(340,353) and mouse[1] in range(335,348):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (180,265)) #Seattle
            if click[0] == 1 and mouse[0] in range(180,193) and mouse[1] in range(265,278):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (180,295)) #SF
            if click[0] == 1 and mouse[0] in range(180,193) and mouse[1] in range(295,308):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (275,335)) #Ausin
            if click[0] == 1 and mouse[0] in range(275,288) and mouse[1] in range(335,348):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (220,320)) #Pheonix
            if click[0] == 1 and mouse[0] in range(220,233) and mouse[1] in range(320,333):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (305,305)) #Saint Louis
            if click[0] == 1 and mouse[0] in range(305,318) and mouse[1] in range(305,318):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (335,300)) #Columbus
            if click[0] == 1 and mouse[0] in range(335,348) and mouse[1] in range(300,313):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (350,310)) #Charolette
            if click[0] == 1 and mouse[0] in range(350,363) and mouse[1] in range(310,323):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (245,305)) #Denver
            if click[0] == 1 and mouse[0] in range(245,258) and mouse[1] in range(305,318):
                print("test")

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1025,288)) #Urumqi
            if click[0] == 1 and mouse[0] in range(1025,1038) and mouse[1] in range(288,301):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1085,340)) #Chendu
            if click[0] == 1 and mouse[0] in range(1085,1098) and mouse[1] in range(340,353):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1145,300)) #Beijing
            if click[0] == 1 and mouse[0] in range(1145,1158) and mouse[1] in range(300,313):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1125,370)) #Guangzhou
            if click[0] == 1 and mouse[0] in range(1125,1138) and mouse[1] in range(370,383):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1155,335)) #Shanghai
            if click[0] == 1 and mouse[0] in range(1155,1168) and mouse[1] in range(335,348):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1120,340)) #Wuhan
            if click[0] == 1 and mouse[0] in range(1120,1133) and mouse[1] in range(340,353):
                print("test")

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1180,300)) #Pyongyang
            if click[0] == 1 and mouse[0] in range(1180,1193) and mouse[1] in range(300,313):
                print("test")

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (668,246)) #London
            if click[0] == 1 and mouse[0] in range(668,681) and mouse[1] in range(246,259):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (655,232)) #Manchester
            if click[0] == 1 and mouse[0] in range(655,668) and mouse[1] in range(232,245):
                print("test")

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (960,330)) #Islamabad
            if click[0] == 1 and mouse[0] in range(960,973) and mouse[1] in range(330,343):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (955,345)) #Multan
            if click[0] == 1 and mouse[0] in range(955,968) and mouse[1] in range(345,358):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (945,365)) #Karachi
            if click[0] == 1 and mouse[0] in range(945,958) and mouse[1] in range(365,378):
                print("test")

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (805,225)) #Moscow
            if click[0] == 1 and mouse[0] in range(805,818) and mouse[1] in range(225,238):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1020,230)) #Novosibirsk
            if click[0] == 1 and mouse[0] in range(1020,1033) and mouse[1] in range(230,243):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (800,210)) #St. Pertersburg
            if click[0] == 1 and mouse[0] in range(800,813) and mouse[1] in range(210,223):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1220,250)) #Khabarovsk
            if click[0] == 1 and mouse[0] in range(1220,1233) and mouse[1] in range(250,263):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1090,240)) #Irkutsk
            if click[0] == 1 and mouse[0] in range(1090,1103) and mouse[1] in range(240,253):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (830,270)) #Krasnodar
            if click[0] == 1 and mouse[0] in range(830,843) and mouse[1] in range(270,283):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (1280,205)) #Magadan
            if click[0] == 1 and mouse[0] in range(1280,1293) and mouse[1] in range(205,218):
                print("test")
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.jpg").convert_alpha(),(13, 13)), (825,205)) #Arkhangel'sk
            if click[0] == 1 and mouse[0] in range(825,838) and mouse[1] in range(205,218):
                print("test")

            if click[0] == 1 and mouse[0] in range(0,100) and mouse[1] in range(0,100):
                sys.exit()
            pygame.event.wait()
            pygame.display.flip()


    def endLoop(self):
        pass
