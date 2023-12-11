import sys
import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN

def run():
    pygame.init()
    pygame.display.set_mode((640,480))
    pygame.display.set_caption("Еще один Пакман")

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT or ( evt.type == KEYDOWN and evt.key == K_ESCAPE ) :
                sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    run()