import pygame as pg
import sys

pg.init()

size = width, height = 600, 400
screen = pg.display.set_mode(size)
pg.display.set_caption('wutong')
bg = (0, 0, 0)
font = pg.font.Font(None, 20)
line_height = font.get_linesize()
position = 0
screen.fill(bg)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
        screen.blit(font.render(str(e), True, (0, 255, 0)), (0, position))
        position += line_height

        if(position > height):
            position = 0
            screen.fill(bg)
    pg.display.flip()
