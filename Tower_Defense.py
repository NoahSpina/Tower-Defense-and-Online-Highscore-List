import pygame as pg
import constants as c

#initialize pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defense")
run = True
while run:

    clock.tick(c.FPS)
    #event handler
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False


pg.quit()