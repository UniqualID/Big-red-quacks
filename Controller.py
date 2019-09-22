import sys
import pygame
import time



class Controller:
    selected = -1
    def __init__(self, width=640*2+160, height=480*2):
        pygame.init()
        # IN ORDER:             Name, population, cReasources , GDP, nukes, antiair, missile creation, food production, anti radiation, education, [allies/enemyies]
        self.country_values = [["USA", 350000000, 350000000, 1000000, 0, 0, 0, 0, 0, 0, [-1, 1, 0, 0, 0, 0]],
                               ["UK", 66000000, 66250000, 250000, 0, 0, 0, 0, 0, 0, [1, -1, 0, 0, 0, 0]],
                               ["Russia", 145000000, 144500000, 800000, 0, 0, 0, 0, 0, 0, [0, 0, -1, 1, 0, 0]],
                               ["Korea", 25000000, 24750000, 100000, 0, 0, 0, 0, 0, 0, [0, 0, 1, -1, 0, 0]],
                               ["China", 1400000000, 1400000000, 700000, 0, 0, 0, 0, 0, 0, [0, 0, 0, 0, -1, 1]],
                               ["Pakistan", 200000000, 200000000, 300000, 0, 0, 0, 0, 0, 0, [0, 0, 0, 0, 1, -1]]]
        self.cities = { "USA" : { "Chicago" : [23333333.3, 0], "Salt Lake" : [23333333.3, 0], "Los Angeles" : [23333333.3, 0], "Jacksonville" : [23333333.3, 0], "Seattle" : [23333333.3, 0], "San Fransisco" : [23333333.3, 0], "Houston" : [23333333.3, 0], "Austin" : [23333333.3, 0], "Washington DC" : [23333333.3, 0], "Pheonix" : [23333333.3, 0], "St. Louis" : [23333333.3, 0], "Columbus" : [23333333.3, 0], "Charlotte" : [23333333.3, 0], "Denver" : [23333333.3, 0]},
                        "China" : { "Urumqi" : [233333333.3, 0], "Chengdu" : [233333333.3, 0], "Beijing" : [233333333.3, 0], "Guangzhou" : [233333333.3, 0], "Shanghai" : [233333333.3, 0], "Wuhan" : [233333333.3, 0]},
                        "Russia" : { "Moscow" : [18125000, 0], "St. Petersburg" : [18125000, 0], "Novosibirsk" : [18125000, 0], "Krasnoyarsk" : [18125000, 0], "Irkutsk" : [18125000, 0], "Arkhangel'sk" : [18125000, 0], "Magadan" : [18125000, 0]},
                        "Pakistan" : { "Islamabad" : [66666666.7, 0], "Karachi" : [66666666.7, 0], "Multan" : [66666666.7, 0]},
                        "UK" : {"London" : [33000000, 0], "Manchester" : [33000000, 0]},
                        "North Korea" : {"Pyongyang" : [25000000, 0]}
                        }
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "GAME"
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
            font = pygame.font.Font("assets/fonts/titleFont.TTF", 40)
            title = font.render('Cold War!', True, (250,250,250))
            self.screen.blit(title, (630,100))
            pygame.draw.rect(self.screen, (0,192,0), (b1x,b1y,200,100)) #quit ((RGB)(x, y, length x, length y))
            pygame.draw.rect(self.screen, (0,192,0), (b2x,b2y,200,100)) #play
            font = pygame.font.Font("assets/fonts/pixelplay.TTF", 45)
            start_button = font.render('PLAY', True, (0,0,0))
            self.screen.blit(start_button, (b2x+57,b2y+35))
            quit_button = font.render('QUIT', True, (0,0,0))
            self.screen.blit(quit_button, (b1x+57,b2y+35))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            if mouse[0] in range(b2x,b2x+200) and mouse[1] in range(b2y,b2y+100):
                pygame.draw.rect(self.screen, (80,208,255), (b2x,b2y,200,100)) #play
                start_button = font.render('PLAY', True, (0,0,0))
                self.screen.blit(start_button, (b2x+57,b2y+35))
            if mouse[0] in range(b1x,b1x+200) and mouse[1] in range(b1y,b1y+100):
                pygame.draw.rect(self.screen, (80,208,255), (b1x,b1y,200,100)) #exit
                quit_button = font.render('QUIT', True, (0,0,0))
                self.screen.blit(quit_button, (b1x+57,b2y+35))
            if click[0] == 1 and mouse[0] in range(b1x,b1x+200) and mouse[1] in range(b1y,b1y+100):
                sys.exit()
            if click[0] == 1 and mouse[0] in range(b2x,b2x+200) and mouse[1] in range(b2y,b2y+100):
                self.state = "START2"
            pygame.display.flip()


    def startLoop2(self):
        b1x = 150
        b2x = 1090
        b2y = 460
        selected = -1
        selectedButton = -1
        pygame.key.set_repeat(1,50)

        music = pygame.mixer.Sound("assets/papers.wav")
        pygame.mixer.Sound.play(music)

        while(self.state == "START2"):
            background = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg").convert_alpha(),(640*2+160, 480*2))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            title_img = pygame.transform.smoothscale(pygame.image.load("assets/title_img.png").convert_alpha(),(600,400))
            self.screen.blit(title_img, (400,-100))
            font = pygame.font.Font("assets/fonts/titleFont.ttf", 100)
            # title = font.render('Cold War!', True, (0,0,0))
            # self.screen.blit(title, (400,100))
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
            pygame.draw.rect(self.screen, (80,208,255), (628,b2y+120,150,50))
            self.screen.blit(font.render("Play", True, (0,0,0)), (650,b2y+118))
            if mouse[0] in range(628, 778) and mouse[1] in range(b2y+120,b2y+170):
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

            pygame.draw.rect(self.screen, (80,208,255), (608,300,200,50))
            self.screen.blit(font.render("Medium", True, (0,0,0)), (620,301))
            if mouse[0] in range(628, 823) and mouse[1] in range(300,350):
                pygame.draw.rect(self.screen, (0,192,0), (608,300,195,50))
                self.screen.blit(font.render("Medium", True, (0,0,0)), (620,301))
                if click[0] == 1:
                    selectedButton = 1

            pygame.draw.rect(self.screen, (80,208,255), (898,300,150,50))
            self.screen.blit(font.render("Hard", True, (0,0,0)), (920,301))
            if mouse[0] in range(898, 1048) and mouse[1] in range(300,350):
                pygame.draw.rect(self.screen, (0,192,0), (898,300,150,50))
                self.screen.blit(font.render("Hard", True, (0,0,0)), (920,301))
                if click[0] == 1:
                    selectedButton = 2

            #If button is selected, keep button green
            if selectedButton == 0:
                pygame.draw.rect(self.screen, (0,192,0), (352,300,150,50))
                self.screen.blit(font.render("Easy", True, (0,0,0)), (375,301))
            if selectedButton == 1:
                pygame.draw.rect(self.screen, (0,192,0), (623,300,195,50))
                self.screen.blit(font.render("Medium", True, (0,0,0)), (640,301))
            if selectedButton == 2:
                pygame.draw.rect(self.screen, (0,192,0), (898,300,150,50))
                self.screen.blit(font.render("Hard", True, (0,0,0)), (925,301))


            font = pygame.font.Font("assets/fonts/pixelplay.ttf", 30)
            start_button = font.render('Select Difficulty', True, (0,0,0))
            self.screen.blit(start_button, (605,215))
            quit_button = font.render('Pick a Country', True, (0,0,0))
            self.screen.blit(quit_button, (615,415))
            click = pygame.mouse.get_pressed() #tuple postition


            #I CAN SEE YOUR HALO HALO HALO!!!
            if mouse[0] in range(b1x, b1x + 100) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x-65, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b2y))
                if click[0] == 1:
                    selected = 0
            if mouse[0] in range(b1x + 200, b1x + 100 + 200) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x-65 + 200, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
                if click[0] == 1:
                    selected = 1
            if mouse[0] in range(b1x + 400, b1x + 100 + 400) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x - 65 + 400, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
                if click[0] == 1:
                    selected = 2
            if mouse[0] in range(b1x + 600, b1x + 100 + 600) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x - 65 + 600, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
                if click[0] == 1:
                    selected = 3
            if mouse[0] in range(b1x + 800, b1x + 100 + 800) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x - 65 + 800, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
                if click[0] == 1:
                    selected = 4
            if mouse[0] in range(b1x + 1000, b1x + 100 + 1000) and mouse[1] in range(b2y, b2y + 100):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(), (225, 175)), (b1x - 65 + 1000, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))
                if click[0] == 1:
                    selected = 5

            if selected == 0:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x-65, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/us_flag.jpg").convert_alpha(),(100, 100)), (b1x,b2y))
            elif selected == 1:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x-65 + 200, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/uk_flag.jpg").convert_alpha(),(100, 100)), (b1x+200,b2y))
            elif selected == 2:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x - 65 + 400, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/russia_flag.jpg").convert_alpha(),(100, 100)), (b1x+400,b2y))
            elif selected == 3:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x - 65 + 600, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/china_flag.jpg").convert_alpha(),(100, 100)), (b1x+600,b2y))
            elif selected == 4:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x - 65 + 800, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_flag.jpg").convert_alpha(),(100, 100)), (b1x+800,b2y))
            elif selected == 5:
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/selected.png").convert_alpha(), (225, 175)), (b1x - 65 + 1000, b2y-38))
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/nk_flag.jpg").convert_alpha(),(100, 100)), (b1x+1000,b2y))


            if click[0] == 1 and mouse[0] in range(628,778) and mouse[1] in range(b2y+220,b2y+270):
                sys.exit()
            if click[0] == 1 and mouse[0] in range(628,728) and mouse[1] in range(b2y+120,b2y+170):
                self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/halo.png").convert_alpha(),(100,100)), (0,0))
                self.state = "GAME"

            self.selected = selected
            pygame.display.flip()


    def startHud(self):
        if self.selected == 0:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/US_hud.png").convert_alpha(), (195,195)), (20,785))
        elif self.selected == 1:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/UK_hud.png").convert_alpha(), (195,195)), (20,785))
        elif self.selected == 2:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Russia_hud.png").convert_alpha(), (195,195)), (20,785))
        elif self.selected == 3:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/China_hud.png").convert_alpha(), (195,195)), (20,785))
        elif self.selected == 4:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/Pakistan_hud.png").convert_alpha(), (195,195)), (20,785))
        elif self.selected == 5:
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/NK_hud.png").convert_alpha(), (195,195)), (20,785))
        self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/hud.png").convert_alpha(),(1440,630)), (0,330))


    def gameLoop(self):
        pygame.key.set_repeat(1,50)
        background = pygame.transform.smoothscale(pygame.image.load("assets/map.jpg").convert_alpha(),(640*2+160, 480*2))
        self.screen.blit(background, (0,0))
        self.startHud()

        while self.state == "GAME":
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (385,285)) #NYC
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (333,285)) #Chicago
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (363,300)) #DC
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (213,300)) #SLC
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (183,315)) #LA
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (340,335)) #Jacksonville
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (180,265)) #Seattle
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (180,295)) #SF
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (275,335)) #Ausin
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (220,320)) #Pheonix
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (305,305)) #Saint Louis
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (335,300)) #Columbus
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (350,310)) #Charolette
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (245,305)) #Denver

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1025,288)) #Urumqi
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1085,340)) #Chendu
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1145,300)) #Beijing
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1125,370)) #Guangzhou
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1155,335)) #Shanghai
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1120,340)) #Wuhan

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1180,300)) #Pyongyang

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (668,246)) #London
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (655,232)) #Manchester

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1180,300)) #Pyongyang

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (960,330)) #Islamabad
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (955,345)) #Multan
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (945,365)) #Karachi

            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (805,225)) #Moscow
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1020,230)) #Novosibirsk
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (800,210)) #St. Pertersburg
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1220,250)) #Khabarovsk
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1090,240)) #Irkutsk
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (830,270)) #Krasnodar
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (1280,205)) #Magadan
            self.screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/dot.png").convert_alpha(),(13, 13)), (825,205)) #Arkhangel'sk



            pygame.display.flip()
            time.sleep(10)
            sys.exit()
    def endLoop(self):
        pass
