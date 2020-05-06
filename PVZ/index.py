import pygame as pg
import util as u
import os


class Main():
    def __init__(self):
        # 创建窗口
        self.screen = pg.display.set_mode(u.SCREEN_RECT.size)
        # 创建时钟
        self.clock = pg.time.Clock()

        self.__create_sprites()
        # 创建敌机事件
        pg.time.set_timer(u.Z_ENENT, 1000)
        pg.time.set_timer(u.P_T_ENENT, 500)

    def game_start(self):
        pg.init()

        while True:
            # 设置fps
            self.clock.tick(u.FPS)
            # 事件监听
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            # 更新显示
            pg.display.update()

    @staticmethod
    def __game_over():
        pg.quit()
        exit()

    def __create_sprites(self):
        bg_img = os.path.join(os.path.dirname(__file__), 'src/images/bg_1.png')
        bg = u.BG(bg_img)
        self.bg_group = pg.sprite.Group(bg)
        p4_img = os.path.join(os.path.dirname(__file__), 'src/images/p_4.png')
        p4 = u.P(p4_img)
        self.p = p4
        self.p_group = pg.sprite.Group(p4)
        self.z_group=pg.sprite.Group()
    def __check_collide(self):
        pg.sprite.groupcollide(self.p.t_group,self.z_group,True,True)
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.p_group.update()
        self.p_group.draw(self.screen)
        self.p.t_group.update()
        self.p.t_group.draw(self.screen)
        self.z_group.update()
        self.z_group.draw(self.screen)

    def __event_handler(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                Main.__game_over()
            elif e.type == u.P_T_ENENT:
                self.p.fire()
            elif e.type == u.Z_ENENT:
                z1_img = os.path.join(os.path.dirname(__file__), 'src/images/z_1.png')
                z=u.Z(z1_img)
                self.z_group.add(z)
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT and self.p.coordinate_system[0]>0:
                    self.p.coordinate_system[0]-=1
                    self.p.rect.x = u.ORIGIN[0]+u.UNIT_WIDTH*self.p.coordinate_system[0]
                elif e.key == pg.K_RIGHT and self.p.coordinate_system[0]<2:
                    self.p.coordinate_system[0]+=1
                    self.p.rect.x = u.ORIGIN[0]+u.UNIT_WIDTH*self.p.coordinate_system[0]
                elif e.key == pg.K_UP and self.p.coordinate_system[1]>0:
                    self.p.coordinate_system[1]-=1
                    self.p.rect.y = u.ORIGIN[1]+u.UNIT_HEIGHT*self.p.coordinate_system[1]
                elif e.key == pg.K_DOWN and self.p.coordinate_system[1]<4:
                    self.p.coordinate_system[1]+=1
                    self.p.rect.y = u.ORIGIN[1]+u.UNIT_HEIGHT*self.p.coordinate_system[1]
                
if __name__ == '__main__':
    game = Main()
    game.game_start()
