# Imports.
import sys
import pygame
import random

# Width, height and position of window and background
width = 1040
height = 380
i = 0

# Spawning window and background.
win = pygame.display.set_mode((width,height))
bg = pygame.image.load("6.jpg").convert()
bg = pygame.transform.scale(bg,(width, height))

# Setting the title for the window.
pygame.display.set_caption("Fish Runner")

# Importing images.
obstacles = [pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png"),
             pygame.image.load("5.png")]
fish_sprite = pygame.image.load("1.png")
shark_sprite = pygame.image.load("5.png")
shark_sprite = pygame.transform.scale(shark_sprite, (100,100))
gameover = pygame.image.load("7.png")


# Player.
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumpheight = 22
        self.fallspeed = 1.08
        self.duck = 5.9
        self.divedepth = 1
        self.buoyancy = 1
        self.isjump = False
        self.isdive = False


# Enemy.
class enemy(object):
    def __init__(self,width,height):
        self.x = 980
        self.y = random.randrange(30,260,40)
        self.width = width
        self.height = height
        self.velocity = 10

def quit():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                gamerunning = False
        if event.type == pygame.QUIT:
            gamerunning = False

def jump():
        if not fish.isjump:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP\
                    or event.key == pygame.K_RIGHT:
                    fish.isjump = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fish.isjump = True

def duck():
        if fish.isjump:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN\
                    or event.key == pygame.K_LEFT:
                    fish.fallspeed = fish.duck
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    fish.fallspeed = fish.duck

def dive():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN\
                or event.key == pygame.K_LEFT:
                fish.isdive = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                fish.isdive = False
        if fish.isjump:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN\
                    or event.key == pygame.K_LEFT:
                    fish.fallspeed = fish.duck
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    fish.fallspeed = fish.duck
        if not fish.isjump:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN\
                    or event.key == pygame.K_LEFT:
                    fish.isdive = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    fish.fallspeed = fish.duck



# Fish.
fish = player(46,245,88,88)
# Shark.
shark = enemy(300, 300)
# Timer.
clock = pygame.time.Clock()
# Starts the loop.
gamerunning = True

# Loop.
while gamerunning:
    # 无图像地方自动填黑。
    win.fill((0, 0, 0))
    # 每秒60帧的显示。
    clock.tick(60)
    # 显示并向右移动背景。
    win.blit(bg,(i,0))
    win.blit(bg,(width+i,0))
    if (i==-width):
        win.blit(bg,(width+i,0))
        i=0
    i-=8
    # 根据 (x,y) 坐标显示玩家。
    win.blit(fish_sprite, (fish.x, fish.y))
    win.blit(shark_sprite, (shark.x, shark.y))
    shark.x -= shark.velocity
    if shark.x == -width:
        pass
    for event in pygame.event.get():
        jump()
        duck()
        dive()
        quit()
    # 让程序查看用户输入。
    # 若玩家处于跳跃状态。
    if fish.isjump:
        # 玩家y轴方位的变化。
        fish.y -= fish.jumpheight
        # 跳跃高度随着时间推移而减小。
        fish.jumpheight = fish.jumpheight - fish.fallspeed
    if fish.isdive:
        fish.y += fish.divedepth
        fish.divedepth = fish.divedepth - fish.buoyancy
        # 若玩家达到原本最低高度。
    if fish.isdive:
        if fish.y <= 313:
            fish.y = 313
    if not fish.isdive:
        if fish.y >= 245:
                # 玩家不再处于跳跃状态
                fish.y = 245
                fish.isjump = False
                fish.isdive = False
                fish.jumpheight = 22
                fish.fallspeed = 1.08
                fish.divedepth = 1
                fish.buoyancy = 1
    print(fish.y)
    # creates time delay of 10ms
    pygame.time.delay(10)
    pygame.display.update()

#def Player(object):
    pass

class Obstacle(object):
    # 定义障碍物类型物体的特征

    def distance_square(a, b):
        return (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - b.y)

    def init_enemy(min_distance):
        while True:
            object.x = random.randrange(2, 502, 20)
            object.y = random.randrange(2, 502, 20)
            if min_distance.distance_square(object, fish) > (min_distance * min_distance):
                break

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


        self.x = random.randrange(2, 502, 20)
        self.y = random.randrange(2, 502, 20)
        bg.blit("2.png", (obstacles.x, obstacles.y))

