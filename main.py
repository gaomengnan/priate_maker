import pygame as pg
from core import settings
from core.editor import Editor


class Engine:
    def __init__(self) -> None:
        pg.init()
        self.display_surface = pg.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        self.clock = pg.time.Clock()

        self.editor = Editor()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         sys.exit()

            self.editor.run(dt)
            pg.display.update()


if __name__ == "__main__":
    engine = Engine()
    engine.run()
