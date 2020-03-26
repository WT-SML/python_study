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
        pygame.time.set_timer(util.CREATE_ENEMY_ENENT,1000)


    """
    游戏开始
    """

    def start(self):
        pygame.init()
        while True:
            # 设置fps
            self.clock.tick(util.FPS)
            # 事件监听
            Game.__event_handler()
            
            # 碰撞检测

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

    """
    更新精灵组
    """

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

    """
    事件处理
    """
    def __event_handler():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.__game_over()
            elif event.type==util.CREATE_ENEMY_ENENT:

                
                print('敌机出场')

if __name__ == "__main__":
    game = Game()
    game.start()

# pygame.init()
# 创建游戏窗口
# 窗口大小 480*700
# screen = pygame.display.set_mode((480, 700))
# bg = pygame.image.load('./src/images/background.png')
# screen.blit(bg, (0, 0))
# # 绘制飞机
# hero = pygame.image.load('./src/images/me1.png')
# screen.blit(hero, (189, 500))
# # 更新显示
# pygame.display.update()
# # 定义英雄矩形对象
# hero_react = pygame.Rect(189, 500, 102, 126)
# # 定义时钟
# clock = pygame.time.Clock()
# # 游戏循环
# while True:
#     clock.tick(60)  # 设置帧数 60
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     event_list = pygame.event.get()
#     if len(event_list) > 0:
#         print(event_list)
#     hero_react.y -= 1
#     if hero_react.y < -126:
#         hero_react.y = 700
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_react)
#     pygame.display.update()
