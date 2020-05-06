import pygame as pg
from pygame.display import list_modes
import os
import random

GAME_NAME = 'wutong pvz'
SCREEN_RECT = pg.Rect(0, 0, 1360, 768)
FPS = 60
Z_ENENT = pg.USEREVENT
P_T_ENENT = pg.USEREVENT+1
RESOLUTION_RATIO = (1360, 768)
ORIGIN = (356, 203)
UNIT_HEIGHT = 99
UNIT_WIDTH = 84
P_RECT = (75, 75)
T_RECT = (25, 25)
Z_RECT = (80, 200)


class BG(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), RESOLUTION_RATIO)
        self.rect = self.image.get_rect()


class P(pg.sprite.Sprite):
    coordinate_system = [0, 2]

    def __init__(self, image):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), P_RECT)
        self.rect = self.image.get_rect()
        self.coordinate_system = [0, 2]
        self.rect.x = ORIGIN[0]+UNIT_WIDTH*self.coordinate_system[0]
        self.rect.y = ORIGIN[1]+UNIT_HEIGHT*self.coordinate_system[1]
        self.t_group = pg.sprite.Group()

    def fire(self):
        t_img = os.path.join(os.path.dirname(__file__), 'src/images/t_4.png')
        t = T(t_img)
        t.rect.x = self.rect.x+self.rect.width+5
        t.rect.y = self.rect.y+15
        self.t_group.add(t)


class T(pg.sprite.Sprite):
    speed = 5

    def __init__(self, image):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), T_RECT)
        self.rect = self.image.get_rect()

    def update(self):
        super().update()
        self.rect.x += self.speed
        if self.rect.x > RESOLUTION_RATIO[0]:
            self.kill()


class Z(pg.sprite.Sprite):
    speed = 1

    def __init__(self, image, speed=1):
        super().__init__()
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), Z_RECT)
        self.rect = self.image.get_rect()
        self.rect.x = ORIGIN[0]+UNIT_WIDTH*8
        r=random.randint(0, 4)
        print(r)
        self.rect.y = ORIGIN[1]+UNIT_HEIGHT*random.randint(1, 5)-self.rect.height

    def update(self):
        super().update()
        self.rect.x -= self.speed
