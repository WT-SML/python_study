import pygame
import util


class Game():
    """
    初始化
    """

    def __init__(self):
        # 创建窗口
        self.screen = pygame.display.set_mode(util.SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 创建精灵组
        self.__create_sprites()
        # 创建敌机事件
        pygame.time.set_timer(util.CREATE_ENEMY_ENENT, 1000)
        pygame.time.set_timer(util.HERO_FIRE_ENENT, 200)

    """
    游戏开始
    """

    def start(self):
        pygame.init()
        while True:
            # 设置fps
            self.clock.tick(util.FPS)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    """
    游戏结束
    """
    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

    """
    创建精灵组
    """

    def __create_sprites(self):
        bg1 = util.BG()
        bg2 = util.BG(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = util.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    """
    更新精灵组
    """

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)


    """
    碰撞检测
    """
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            Game.__game_over()

    """
    事件处理
    """

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.__game_over()
            elif event.type == util.CREATE_ENEMY_ENENT:
                # 创建敌机精灵
                enemy = util.Enemy()
                self.enemy_group.add(enemy)
            elif event.type == util.HERO_FIRE_ENENT:
                self.hero.fire()

        kets_pressed = pygame.key.get_pressed()
        if kets_pressed[pygame.K_RIGHT]:
            if self.hero.speed != 5:
                self.hero.speed = 5
        elif kets_pressed[pygame.K_LEFT]:
            if self.hero.speed != -5:
                self.hero.speed = -5
        else:
            self.hero.speed = 0


if __name__ == "__main__":
    game = Game()
    game.start()