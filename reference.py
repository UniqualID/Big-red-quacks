import sys
import pygame
import random
import pickle
from src import Hero
from src import enemy_1
from src import enemy_2
from src import enemy_3
from src import heroBullet
from src import enemyBullet

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()
        self.enemy1_freq = 3
        self.enemy2_freq = 2
        self.enemy3_freq = 1
        """Load the sprites that we need"""
        self.enemies1 = pygame.sprite.Group()
        self.enemies2 = pygame.sprite.Group()
        self.enemies3 = pygame.sprite.Group()
        num_enemies = random.randrange(3,5)
        for i in range(num_enemies):
            y = random.randrange(30, 400)
            x = random.randrange(550, 600)
            self.enemies1.add(enemy_1.enemy_1(x, y, 3, 'assets/enemy.png' ))
        self.heroBullet = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group()
        self.hero = (Hero.hero("phil", 3, 80, 3, "assets/hero.png"))
        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
        self.state = "START"
        pygame.mixer.init()
        sound = pygame.mixer.music.load("assets/spacemusic.wav")
        pygame.mixer.music.play(-1,0)


    def mainLoop(self):
        while True:
            if(self.state == "START"):
                self.startLoop()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    def startLoop(self):
        pygame.key.set_repeat(1,50)
        while self.state == "START":
            background = pygame.transform.smoothscale(pygame.image.load("assets/background_3.jpg").convert_alpha(),(640,480))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            font = pygame.font.SysFont("arial", 40, True)
            title = font.render('Welcome to Galaxy Shooter!', True, (250,250,250))
            self.screen.blit(title, (100,100))
            font = pygame.font.SysFont("arial", 20, True)
            instruct1 = font.render('Move with the UP/DOWN/LEFT/RIGHT keys', True, (250,250,250))
            instruct2 = font.render('Shoot with SPACE', True, (250,250,250))
            instruct3 = font.render('Press x to turn off sound', True, (250,250,250))
            instruct4 = font.render('Press s to turn on sound', True, (250,250,250))
            instruct5 = font.render('Good Luck!~', True, (250,250,250))
            self.screen.blit(instruct1, (150,165))
            self.screen.blit(instruct2, (230,205))
            self.screen.blit(instruct3, (207,245))
            self.screen.blit(instruct4, (207,285))
            self.screen.blit(instruct5, (245,325))
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

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        #for heroBullet killing
        hero_bullet = self.heroBullet.sprites()
        #for determining when the enemies respawn
        time_elapsed_1 = 0
        time_elapsed_2 = 0
        time_elapsed_3 = 0
        #intermidiary variables
        enemy1_accum = 0
        enemy2_accum = 0
        enemy3_accum = 0
        #for increacing enemy frequency
        enemy_time = 0
        #for score tracking
        e1_killcount = 0
        e2_killcount = 0
        e3_killcount = 0
        clock = pygame.time.Clock()
        other_clock = pygame.time.Clock()
        while self.state == "GAME":
            background = pygame.transform.smoothscale(pygame.image.load("assets/background_3.jpg").convert_alpha(),(640,480))
            self.screen.blit(background, (0,0))
            #sets the enemies to fire periodaically
            new_time = clock.tick()
            time_elapsed_1 += new_time
            time_elapsed_2 += new_time
            time_elapsed_3 += new_time
            enemy1_accum += new_time
            enemy2_accum += new_time
            enemy3_accum += new_time
            #groups of enemy types
            enemies_one = self.enemies1.sprites()
            enemies_two = self.enemies2.sprites()
            enemies_three = self.enemies3.sprites()
            if (time_elapsed_1 > 3000):
                if len(enemies_one) >= 1:
                    fire = random.randrange(0, len(enemies_one))
                    self.enemy_1 = enemies_one[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_1.rect.centerx, self.enemy_1.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_1 = 0
            if (time_elapsed_2 > 3000):
                if len(enemies_two) >= 1:
                    fire = random.randrange(0, len(enemies_two))
                    self.enemy_2 = enemies_two[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_2.rect.centerx, self.enemy_2.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_2 = 0
            if (time_elapsed_3 > 3000):
                if len(enemies_three) >= 1:
                    fire = random.randrange(0, len(enemies_three))
                    self.enemy_3 = enemies_three[fire]
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "up"))
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "reg"))
                    self.enemyBullet.add(enemyBullet.enemyBullet(self.enemy_3.rect.centerx, self.enemy_3.rect.centery, 'assets/enemybullet.png', 6, "down"))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    time_elapsed_3 = 0
            #creates new enemies periodaically
            if enemy1_accum > 6000:
                for i in range(self.enemy1_freq):
                    y = random.randrange(30, 450)
                    x = random.randrange(550, 650)
                    self.enemies1.add(enemy_1.enemy_1(x, y, 3, 'assets/enemy.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                    enemy1_accum = 0
            if (enemy2_accum >= 20000):
                if (enemy_time > 4):
                    enemy2_accum = 15000
                else:
                    enemy2_accum = 10000
                enemy_time += 1
                for i in range(self.enemy2_freq):
                    y = random.randrange(30, 450)
                    x = random.randrange(550, 650)
                    self.enemies2.add(enemy_2.enemy_2(x, y, 3, 'assets/enemy2.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            if (enemy3_accum >= 40000):
                if (enemy_time > 8):
                    enemy3_accum = 35000
                else:
                    enemy3_accum = 30000
                for i in range(self.enemy3_freq):
                    y = random.randrange(30, 440)
                    x = random.randrange(550, 650)
                    self.enemies3.add(enemy_3.enemy_3(x, y, 3, 'assets/enemy3.png' ))
                    self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
            #makes the hero lose a health if the enmies reach the other side
            for i in range(len(enemies_one)):
                if (enemies_one[i].rect.x < 0):
                    self.hero.health -= 1
                    enemies_one[i].kill()
            for i in range(len(enemies_two)):
                if (enemies_two[i].rect.x < 0):
                    self.hero.health -= 1
                    enemies_two[i].kill()
            for i in range(len(enemies_three)):
                if (enemies_three[i].rect.x < 0):
                    self.hero.health -= 1
                    enemies_three[i].kill()
            #self.background.fill((250, 250, 250)) #white
            musicPlaying = True
            # checks the user controlled buttons
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        if (self.hero.rect.y > 0):
                            self.hero.move("up")
                    elif(event.key == pygame.K_DOWN):
                        if (self.hero.rect.y < 420):
                            self.hero.move("down")
                    elif(event.key == pygame.K_LEFT):
                        if (self.hero.rect.x > 0):
                            self.hero.move("left")
                    elif(event.key == pygame.K_RIGHT):
                        if (self.hero.rect.x < 500):
                            self.hero.move("right")
                    elif(event.key == pygame.K_SPACE):
                        self.heroBullet.add(heroBullet.heroBullet(self.hero.rect.x + 50, self.hero.rect.y + 20, 12, 'assets/herobullet.png'))
                        self.all_sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies1)+tuple(self.enemies2)+tuple(self.enemies3)+tuple(self.enemyBullet)+tuple(self.heroBullet))
                        pygame.mixer.init()
                        shoot=pygame.mixer.Sound("assets/shooternoise.wav")
                        pygame.mixer.Sound.play(shoot)
                    elif event.key == ord('x'):
                       if musicPlaying:
                           pygame.mixer.music.stop()
                       else:
                           pygame.mixer.music.play(-1, 0.0)
                       musicPlaying = not musicPlaying
                    elif event.key == ord('s'):
                       if musicPlaying:
                           pygame.mixer.music.play(-1, 0.0)
                       else:
                           pygame.mixer.music.stop()
                       musicPlaying = not musicPlaying
            #check for number of heroBullets
            # for bullet in range(len(hero_bullet)):
            #     if self.heroBullet[bullet].rect.centerx > 100:
            #         hero_bullet[bullet].kill()
            #check for heroBullet collisions with enemy
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies1, True, True):
                e1_killcount += 1
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies2, True, True):
                e2_killcount += 1
            if pygame.sprite.groupcollide(self.heroBullet, self.enemies3, True, True):
                e3_killcount += 1
            # check for heroship collisions with emeny ships
            ship_collide1 = pygame.sprite.spritecollide(self.hero, self.enemies1, True) != []
            if ship_collide1:
                self.hero.health -= 1
                print(self.hero.health)
                e1_killcount += 1
                collision=pygame.mixer.Sound("assets/explosion.wav")
                pygame.mixer.Sound.play(collision)
            ship_collide2 = pygame.sprite.spritecollide(self.hero, self.enemies2, True) != []
            if ship_collide2:
                self.hero.health -= 1
                print(self.hero.health)
                e2_killcount += 1
                collision=pygame.mixer.Sound("assets/explosion.wav")
                pygame.mixer.Sound.play(collision)
            ship_collide3 = pygame.sprite.spritecollide(self.hero, self.enemies3, True) != []
            if ship_collide3:
                self.hero.health -= 1
                print(self.hero.health)
                e3_killcount += 1
                collision=pygame.mixer.Sound("assets/explosion.wav")
                pygame.mixer.Sound.play(collision)
            #check for enemyBullet collisions with hero
            collide = pygame.sprite.spritecollide(self.hero, self.enemyBullet, True) != []
            if collide:
                self.hero.health -= 1
                print(self.hero.health)
                collision=pygame.mixer.Sound("assets/explosion.wav")
                pygame.mixer.Sound.play(collision)
            #saving killcounts into pickle file to load in game over state
            with open('killcounts.pkl', 'wb') as f:
                pickle.dump((e1_killcount, e2_killcount, e3_killcount), f)
            #redraw the entire screen
            self.all_sprites.update()
            if(self.hero.health <= 0):
                self.state = "GAMEOVER"

            #display the text
            font = pygame.font.SysFont("arial", 30, True)
            lives = font.render('Health: ' + str(self.hero.health), True, (250,0,0))
            self.screen.blit(lives, (500,450))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def gameOver(self):
        self.hero.kill()
        with open('killcounts.pkl', 'rb') as f:
            e_killcount = pickle.load(f)
        while self.state == "GAMEOVER":
            background = pygame.transform.smoothscale(pygame.image.load("assets/background_3.jpg").convert_alpha(),(640,480))
            self.screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #for high score check
            score = int(e_killcount[0]) + (int(e_killcount[1] * 3)) + (int(e_killcount[2] * 5))
            fptr = open("highscore.txt", "r")
            highscore = fptr.readline()
            fptr.close()
            if score > int(highscore):
                fptr = open("highscore.txt", "w")
                fptr.write(str(score))
                fptr.close()
            #display the PLayer's results
            myfont = pygame.font.SysFont("arial", 40, True)
            message = myfont.render('High Score:  ' + str(highscore), False, (250,250,250))
            self.screen.blit(message, (200,350))
            message = myfont.render('Your Score:  ' + str(score), False, (250,250,250))
            self.screen.blit(message, (200,300))
            message = myfont.render('Game Over', False, (250,250,250))
            self.screen.blit(message, (200,50))
            self.end_enemies1 = pygame.sprite.Group()
            self.end_enemies2 = pygame.sprite.Group()
            self.end_enemies3 = pygame.sprite.Group()
            self.end_enemies1.add(enemy_1.enemy_1(130, 145, 0, 'assets/enemy.png' ))
            self.end_enemies2.add(enemy_2.enemy_2(130, 185, 0, 'assets/enemy2.png' ))
            self.end_enemies3.add(enemy_3.enemy_3(130, 225, 0, 'assets/enemy3.png' ))
            self.end_sprites = pygame.sprite.Group(self.end_enemies1, self.end_enemies2, self.end_enemies3)
            myfont = pygame.font.SysFont("arial", 30, True)
            message1 = myfont.render('=     ' + str(e_killcount[0]), False, (250,250,250))
            message2 = myfont.render('=     ' + str(e_killcount[1]), False, (250,250,250))
            message3 = myfont.render('=     ' + str(e_killcount[2]), False, (250,250,250))
            message1_2 = myfont.render('x1    =  ' + str(e_killcount[0]), False, (250,250,250))
            message2_2 = myfont.render('x3    =  ' + str(e_killcount[1]), False, (250,250,250))
            message3_2 = myfont.render('x5    =  ' + str(e_killcount[2]), False, (250,250,250))
            self.screen.blit(message1, (220,160))
            self.screen.blit(message2, (220,200))
            self.screen.blit(message3, (220,240))
            self.screen.blit(message1_2, (310,160))
            self.screen.blit(message2_2, (310,200))
            self.screen.blit(message3_2, (310,240))
            self.end_sprites.draw(self.screen)
            #play again nad quit buttons
            pygame.draw.rect(self.screen, (80,208,255), (50,400,150,50)) #quit
            pygame.draw.rect(self.screen, (0,192,0), (440,400,150,50)) #start
            font = pygame.font.SysFont("arial", 25, True)
            replay_button = font.render('PLAY AGAIN', True, (0,0,0))
            self.screen.blit(replay_button, (455,415))
            exit_button = font.render('QUIT', True, (0,0,0))
            self.screen.blit(exit_button, (100,415))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #tuple postition
            if click[0] == 1 and mouse[0] in range(440,590) and mouse[1] in range(400,450):
                self.state = "START"
                Controller.__init__(self, width=640, height=480)
            if click[0] == 1 and mouse[0] in range(50,200) and mouse[1] in range(400,450):
                sys.exit()
            pygame.display.flip()
