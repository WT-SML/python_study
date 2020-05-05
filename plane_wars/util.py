import random
import pygame
import os


SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FPS = 60
CREATE_ENEMY_ENENT = pygame.USEREVENT  # 敌机定时器常量
HERO_FIRE_ENENT = pygame.USEREVENT+1  # 敌机定时器常量

"""
精灵
"""


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


"""
背景
"""


class BG(Sprite):
    def __init__(self, isTop=False):
        # super().__init__('./src/images/background.png')
        super().__init__(os.path.join(os.path.dirname(__file__),'src/images/background.png'))
        if isTop:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(Sprite):
    # 敌机精灵
    def __init__(self):
        # super().__init__('./src/images/enemy1.png')
        super().__init__(os.path.join(os.path.dirname(__file__),'src/images/enemy1.png'))
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(Sprite):
    def __init__(self):
        # super().__init__('./src/images/me1.png', 0)
        super().__init__(os.path.join(os.path.dirname(__file__),'src/images/me1.png'))
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-100
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        w = self.rect.width/2
        self.rect.x += self.speed
        if self.rect.x < -w:
            self.rect.x = -w
        elif self.rect.right > SCREEN_RECT.right+w:
            self.rect.right = SCREEN_RECT.right+w

    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y-20
        bullet.rect.centerx = self.rect.centerx
        self.bullet_group.add(bullet)


class Bullet(Sprite):
    def __init__(self):
        # super().__init__('./src/images/bullet1.png', -10)
        super().__init__(os.path.join(os.path.dirname(__file__),'src/images/bullet1.png'),-10)


    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
