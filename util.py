import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FPS = 60
CREATE_ENEMY_ENENT = pygame.USEREVENT  # 敌机定时器常量

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
        super().__init__('./src/images/background.png')
        if isTop:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
