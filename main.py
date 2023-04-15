import pygame as pg
from board import Board
pg.init()
screen = pg.display.set_mode((600, 600))

board = Board(600, 600, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill('white')
    board.render(screen)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        board.clear()