import pygame

spawn_x = 980


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=0):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed


class Background(GameSprite, 8):
    def __init__(self):
        super().__init__("./images/background.jpg")

    def update(self):
        super().update()
        if self.rect.x > width:
            self.rect.x = -self.rect.width
    #def bg_move(self):
        #global i
        #win.blit(bg, (i, 0))
        #win.blit(bg, (width + i, 0))
        #if i == -width:
        #    win.blit(bg, (width + i, 0))
        #    i = 0
        #i -= 8


class Player(GameSprite):
    def __init__(self):
        super().__init__("./images/fish.png")
        self.x = 46
        self.y = 245
        self.jumpheight = 22
        self.fallspeed = 1.08
        self.duck = 5.9
        self.divedepth = 1
        self.buoyancy = 1
        self.isjump = False
        self.isdive = False


class Enemy1(GameSprite):
    def __init__(self):
        super().__init__("./images/shark.png", 10)
        self.x = spawn_x
        self.y = random.randrange(30,260,40)
        self.width = random.randrange(300,500,50)
        self.height = self.width

    def update(self):
        super().update()



