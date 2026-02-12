import time
import pygame
import random
from os import*
img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 600
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()


background = pygame.image.load(path.join(img_dir, "фон.png")).convert_alpha()
background1= pygame.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background1.get_rect()
p = pygame.image.load(path.join(img_dir, "перед.png")).convert_alpha()
ship_img = pygame.image.load(path.join(img_dir, "шип.png")).convert_alpha()
dirt_img = pygame.image.load(path.join(img_dir, "земля.png")).convert_alpha()
dirt1_img = pygame.image.load(path.join(img_dir, "земля1.png")).convert_alpha()
dirt2_img = pygame.image.load(path.join(img_dir, "земля2.png")).convert_alpha()
dirt3_img = pygame.image.load(path.join(img_dir, "земля3.png")).convert_alpha()
dirt4_img = pygame.image.load(path.join(img_dir, "земля4.png")).convert_alpha()
pli1 = pygame.image.load(path.join(img_dir, "ли1.png")).convert_alpha()
pli2 = pygame.image.load(path.join(img_dir, "ли2.png")).convert_alpha()
pli3 = pygame.image.load(path.join(img_dir, "ли3.png")).convert_alpha()
pls = pygame.image.load(path.join(img_dir, "лс.png")).convert_alpha()
ppi1 = pygame.image.load(path.join(img_dir, "пи1.png")).convert_alpha()
ppi2 = pygame.image.load(path.join(img_dir, "пи2.png")).convert_alpha()
ppi3 = pygame.image.load(path.join(img_dir, "пи3.png")).convert_alpha()
pps = pygame.image.load(path.join(img_dir, "пс.png")).convert_alpha()
coin_img = pygame.image.load(path.join(img_dir, "Койн.png")).convert_alpha()
pila_img = pygame.image.load(path.join(img_dir, "Пила.png")).convert_alpha()


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.storona = 0
        self.speedx = 0
        self.speedy = 10
        if self.storona == 0:
            self.image = pygame.transform.scale(p, (21 * 2, 37 * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.a = -1


    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speedx = -6
            self.storona = 1
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 6
            self.storona = 2


        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.speedx == 0:
            if self.storona == 1:
                self.image = pygame.transform.scale(pls, (21 * 2, 37 * 2))
            if self.storona == 2:
                self.image = pygame.transform.scale(pps, (21 * 2, 37 * 2))

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = 0


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ship_img, (9*2, 9*2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Dirt(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        if n == 0:
            self.image = pygame.transform.scale(dirt_img, (25 * 3, 22 * 3))
        elif n == 1:
            self.image = pygame.transform.scale(dirt1_img, (25 * 3, 8 * 3))
        elif n == 2:
            self.image = pygame.transform.scale(dirt2_img, (25 * 3, 8 * 3))
        elif n == 3:
            self.image = pygame.transform.scale(dirt3_img, (25 * 3, 8 * 3))
        elif n == 4:
            self.image = pygame.transform.scale(dirt4_img, (25 * 3, 8 * 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pila(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pila_img, (20*1, 20*1))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(0, 600)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coin_img, (12 * 2, 16 * 2))
        self.rect = self.image.get_rect()
        self.x = random.randrange(1, 8)
        if self.x == 1:
            self.rect.x = 50
            self.rect.y = 100
        elif self.x == 2:
            self.rect.x = 200
            self.rect.y = 100
        elif self.x == 3:
            self.rect.x = 500
            self.rect.y = 250
        elif self.x == 4:
            self.rect.x = 200
            self.rect.y = 400
        elif self.x == 5:
            self.rect.x = 500
            self.rect.y = 500
        elif self.x == 6:
            self.rect.x = 50
            self.rect.y = 400
        elif self.x == 7:
            self.rect.x = 350
            self.rect.y = 500


all_sprites = pygame.sprite.Group()
dirts = pygame.sprite.Group()
ships = pygame.sprite.Group()
coins = pygame.sprite.Group()
pils = pygame.sprite.Group()
for i in range(3):
    c = Coin()
    coins.add(c)
    all_sprites.add(c)
player = Player(290, 200)
ship = Ship(0, 535)
ship1 = Ship(18, 535)
ship2 = Ship(36, 535)
ship3 = Ship(54, 535)
ship4 = Ship(72, 535)
ship5 = Ship(90, 535)
ship6 = Ship(108, 535)
ship7 = Ship(126, 535)
ship8 = Ship(144, 535)
ship9 = Ship(162, 535)
ship10 = Ship(180, 535)
ship11 = Ship(198, 535)
ship12 = Ship(216, 535)
ship13 = Ship(234, 535)
ship14 = Ship(252, 535)
dirt = Dirt(0, 550, 0)
dirt1 = Dirt(75, 550, 0)
dirt2 = Dirt(150, 550, 0)
dirt3 = Dirt(225, 550, 0)
dirt4 = Dirt(300, 550, 0)
dirt5 = Dirt(375, 550, 0)
dirt6 = Dirt(450, 550, 0)
dirt7 = Dirt(525, 550, 0)
dirt8 = Dirt(600, 550, 0)
dirt9 = Dirt(275, 300, 2)
dirt10 = Dirt(350, 300, 1)
dirt11 = Dirt(425, 300, 1)
dirt12 = Dirt(500, 300, 1)
dirt13 = Dirt(575, 300, 1)
dirt14 = Dirt(200, 150, 3)
dirt15 = Dirt(125, 150, 1)
dirt16 = Dirt(50, 150, 1)
dirt17 = Dirt(-25, 150, 1)
dirt18 = Dirt(200, 450, 3)
dirt19 = Dirt(125, 450, 1)
dirt20 = Dirt(50, 450, 1)
dirt21 = Dirt(-25, 450, 1)
all_sprites.add(dirt, dirt1, dirt2, dirt3, dirt4, dirt5, dirt6, dirt7, dirt8, dirt9, dirt10, dirt11, dirt12, dirt13, dirt14, dirt15, dirt16, dirt17, dirt18, dirt19, dirt20, dirt21,  ship, ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10, ship11, ship12, ship13, ship14, player)
dirts.add(dirt, dirt1, dirt2, dirt3, dirt4, dirt5, dirt6, dirt7, dirt8, dirt9, dirt10, dirt11, dirt12, dirt13, dirt14, dirt15, dirt16, dirt17, dirt18, dirt19, dirt20, dirt21)
ships.add(ship, ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10, ship11, ship12, ship13, ship14)

start = 0
time = 0

running = True
while running:
    clock.tick(FPS)
    time += 1
    if time == 61:
        time = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = pygame.time.get_ticks()
                player.speedy = -0.1


    if player.speedx > 0:
        if player.speedy == 0:
            if time < 16:
                player.image = pygame.transform.scale(ppi1, (21 * 2, 37 * 2))
            if 15< time < 31:
                player.image = pygame.transform.scale(ppi2, (21 * 2, 37 * 2))
            if 30 < time < 46:
                player.image = pygame.transform.scale(ppi3, (21 * 2, 37 * 2))
            if 45< time < 61:
                player.image = pygame.transform.scale(ppi2, (21 * 2, 37 * 2))
        else:
            player.image = pygame.transform.scale(ppi3, (21 * 2, 37 * 2))
    elif player.speedx < 0:
        if player.speedy == 0:
            if time < 16:
                player.image = pygame.transform.scale(pli1, (21 * 2, 37 * 2))
            if 15< time < 31:
                player.image = pygame.transform.scale(pli2, (21 * 2, 37 * 2))
            if 30 < time < 46:
                player.image = pygame.transform.scale(pli3, (21 * 2, 37 * 2))
            if 45< time < 61:
                player.image = pygame.transform.scale(pli2, (21 * 2, 37 * 2))
        else:
            player.image = pygame.transform.scale(pli3, (21 * 2, 37 * 2))


    player.speedy += 1.1

    if player.speedy > 15:
        player.speedy = 5


    hits = pygame.sprite.spritecollide(player, dirts, False)
    for hit in hits:
        if player.speedy > 0:
            player.speedy = 0


    hits = pygame.sprite.spritecollide(player, ships, False)
    for hit in hits:
        running = False

    keystate = pygame.key.get_pressed()
    if player.speedy == 0:
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            player.speedy = -20


    hits = pygame.sprite.spritecollide(player, coins, True)
    for hit in hits:
        p = Pila()
        all_sprites.add(p)
        pils.add(p)
        hits = pygame.sprite.spritecollide(player, pils, False)
        for hit in hits:
            p.kill()
            p = Pila()
            all_sprites.add(p)
            pils.add(p)
            hits = pygame.sprite.spritecollide(player, pils, False)
        c = Coin()
        coins.add(c)
        all_sprites.add(c)


    hits = pygame.sprite.spritecollide(player, pils, False)
    for hit in hits:
        player.kill()
        running = False



    screen.blit(background1, background_rect)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()