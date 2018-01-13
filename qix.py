#!/usr/bin/env python

from time import sleep

# Main
def main():
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((640,488)) # set screen size
    background = pygame.Surface(screen.get_size()) # create empty pygame surface
    background.fill((255,255,255)) # fill background white
    background = background.convert() # convert surface for blitting (painting)
    screen.blit(background, (0,0))

    endgame_flag = False
    while not endgame_flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame_flag = True
                print("QUIT")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("THERE IS NO ESCAPE")

if __name__ == '__main__':
    main()
