import sys
from player_input import*

width = 1040
height = 380

win = pygame.display.set_mode((width, height))
bg = background()
bg = pygame.transform.scale(bg, (width, height))

clock = pygame.time.Clock()


class RunnerGame(object):
    def __init__(self):
        global width
        global height
        self.title = pygame.display.set_caption("Fish Runner")
        self.screen = win.blit(bg,(0,0))

    def create_sprites(self):
        self.player = Player()
        self.enemy_group = pygame.sprite.Group()
        shark = Enemy1()
        self.enemy_group.add(shark)

    def game_start(self):
        while True:
            self.clock.tick(60)
            self.event_handler()
            self.check_collide()
            self.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Runner.Game.game_over()
            elif event.type == SPAWN_ENEMY:
                shark = Enemy1()
                self.enemy_group.add(shark)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K]:
            pass

    def check_collide(self):
        enemies = pygame.sprite.groupcollide(self.player, self.enemy_group, True, False)
        if len(enemies) > 0:
            self.player.kill()

    def game_over(self):
        pygame.quit()
        exit()

if __name__ == "__main__":
    game = RunnerGame()
    game.start_game()