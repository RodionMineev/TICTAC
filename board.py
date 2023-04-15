import pygame as pg


class Board:
    def __init__(self, w, h, size):
        self.w, self.h = w, h
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def render(self, screen):
        pg.draw.line(screen, "red", (0, 200), (self.w, 200))
        pg.draw.line(screen, "red", (0, 400), (self.w, 400))
        pg.draw.line(screen, "red", (200, 0), (200, self.h))
        pg.draw.line(screen, "red", (400, 0), (400, self.h))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    self.draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    self.draw_circle(screen, x, y, self.size)

    @staticmethod
    def draw_circle(sc, x, y, size):
        x = (x + .5) * size
        y = (y + .5) * size
        pg.draw.circle(sc, "blue", (x, y), (size - 3) // 2, 3)

    @staticmethod
    def draw_cross(sc, x, y, size):
        x = x * size + 3
        y = y * size + 3
        pg.draw.line(sc, "yellow", (x, y), (x + size - 3, y + size - 3), 3)
        pg.draw.line(sc, "yellow", (x + size - 3, y - 3), (x, y + size - 3), 3)

    def clear(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

