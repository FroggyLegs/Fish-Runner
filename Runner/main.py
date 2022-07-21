# 导入所需数据。
import sys
import pygame

# 定义背景的长宽，及方位。
width = 1040
height = 380
i = 0

# 生成背景及窗口
window = pygame.display.set_mode((width,height))
background = pygame.image.load("6.jpg").convert()
background = pygame.transform.scale(background,(width, height))

# 窗口标题
pygame.display.set_caption("Fish Runner")

# 导入素材。
obstacles = [pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png"),
             pygame.image.load("5.png")]
fish = pygame.image.load("1.png")
gameover = pygame.image.load("7.png")

# 计时器
clock = pygame.time.Clock()

# 玩家默认 (x,y) 坐标。
fish_x = 46
fish_y = 245
# 玩家跳跃高度。
jumpheight = 18
# 玩家默认处于非跳跃动作。
isjump = False

# 游戏结束。
def game_over():
    pass

#for obstacle in sprite.spritecollide(player, obstacle, 1):
    #game_over()

gamerunning = True
# 游戏进行时。
while gamerunning:
    # 无图像地方自动填黑。
    window.fill((0, 0, 0))
    # 每秒60帧的显示。
    clock.tick(60)
    # 显示并向右移动背景。
    window.blit(background,(i,0))
    window.blit(background,(width+i,0))
    if (i==-width):
        window.blit(background,(width+i,0))
        i=0
    i-=10
    # 根据 (x,y) 坐标显示玩家。
    window.blit(fish, (fish_x, fish_y))
    # 让程序查看用户输入。
    for event in pygame.event.get(): 
        # KEYUP 查看玩家是否松开任何按键。
        if event.type == pygame.KEYUP:
            # 松开 Esc 则退出游戏。
            if event.key == pygame.K_ESCAPE:
                gamerunning = False
        # 检测玩家是否按下按键。
        if event.type == pygame.KEYDOWN:
            # 若玩家不处于跳跃状态。
            if not isjump:
                # 按下空格键或者上方向键，触发跳跃状态。
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    isjump = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not isjump:
                if event.button == 1:
                    isjump = True
        # 点击窗口右上端的 x 则退出游戏。
        if event.type == pygame.QUIT:
            sys.exit()
            gamerunning = False
    # 若玩家处于跳跃状态。
    if isjump:
        # 玩家y轴方位的变化。
        fish_y -= jumpheight
        # 跳跃高度随着时间推移而减小。
        jumpheight = jumpheight - 1
        # 若玩家达到原本最低高度。
        if fish_y >= 245:
                # 玩家不再处于跳跃状态
                isjump = False
                jumpheight = 18
        # creates time delay of 10ms
    print(fish_y)
    pygame.time.delay(10)
    pygame.display.update()

#def Player(object):
    pass

class Obstacle(object):
    # 定义障碍物类型物体的特征
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
    

