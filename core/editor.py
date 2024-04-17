import pygame as pg
import sys
from core import settings

from pygame.math import Vector2 as vec


class Editor:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        self.origin = vec()
        self.pain_active = False

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.pain(event)

    def pain(self, event):
        mouses = pg.mouse.get_pressed()
        if event.type == pg.MOUSEBUTTONDOWN and mouses[0]:
            self.pain_active = True
            self.pan_offest = vec(pg.mouse.get_pos()) - self.origin
        if not mouses[0]:
            self.pain_active = False
        if self.pain_active:
            self.origin = vec(pg.mouse.get_pos()) - self.pan_offest

    def draw_lines(self):
        cols = settings.WINDOW_WIDTH // settings.TILE_SIZE
        rows = settings.WINDOW_HEIGHT // settings.TILE_SIZE
        offset = vec(
            x=self.origin.x
            - int(self.origin.x / settings.TILE_SIZE) * settings.TILE_SIZE,
            y=self.origin.y
            - int(self.origin.y / settings.TILE_SIZE) * settings.TILE_SIZE,
        )
        for col in range(cols + 1):
            x = offset.x + col * settings.TILE_SIZE
            pg.draw.line(
                self.display_surface,
                settings.LINE_COLOR,
                (x, 0),
                (x, settings.WINDOW_HEIGHT),
            )

    def run(self, dt):
        self.display_surface.fill("white")
        self.event_loop()
        self.draw_lines()
        pg.draw.circle(self.display_surface, "red", self.origin, 10)
