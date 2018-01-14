#!/usr/bin/env python

########## NATIVE IMPORTS ##########
import sys
import pygame

########## CUSTOM IMPORTS ##########
from modules import colors
from modules.characters import Player
from modules.characters import Sparx
# from modules.characters import Qix # Not ready yet

def main():
    ########## DISPLAY SETTINGS ##########
    SCREEN_SIZE = (650,700) # ( WIDTH , HEIGHT )
    BORDER_PAD = 50         # distance from edge of screen to border

    TITLE_FONT = 'couriernew'
    TITLE_SIZE = 48
    TITLE_BOLD = False
    TITLE_ITALIC = False
    TITLE_COLOR = colors.white
    TITLE_POSITION = (BORDER_PAD,10)

    BORDER = [(BORDER_PAD,BORDER_PAD), \
              (SCREEN_SIZE[0]-BORDER_PAD,BORDER_PAD), \
              (SCREEN_SIZE[0]-BORDER_PAD,SCREEN_SIZE[1]-BORDER_PAD), \
              (BORDER_PAD, SCREEN_SIZE[1]-BORDER_PAD)]
    BORDER_COLOR = colors.white
    BORDER_THICKNESS = 1 # pixel(s)

    SCORE_FONT = 'couriernew'
    SCORE_SIZE = 32
    SCORE_BOLD = False
    SCORE_ITALIC = False
    SCORE_COLOR = colors.yellow
    SCORE_POSITION = (round(SCREEN_SIZE[0]/2) - BORDER_PAD, 10)

    PLAYER_WIDTH = 10
    PLAYER_HEIGHT = 10
    PLAYER_COLOR = colors.red

    ###################################

    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE) # set screen size
    pygame.display.set_caption('QIX')
    title_font = pygame.font.SysFont(TITLE_FONT, TITLE_SIZE, bold=TITLE_BOLD, italic=TITLE_ITALIC)
    title = title_font.render('QIX', False, TITLE_COLOR)
    screen.blit(title, TITLE_POSITION)
    score_font = pygame.font.SysFont(SCORE_FONT, SCORE_SIZE, bold=SCORE_BOLD, italic=SCORE_ITALIC)
    score = score_font.render('00000    QIX', False, SCORE_COLOR)
    screen.blit(score, SCORE_POSITION)
    pygame.draw.lines(screen, BORDER_COLOR, True, BORDER, BORDER_THICKNESS)
    
    start_pos = (round(SCREEN_SIZE[0]/2)-round(PLAYER_WIDTH/2), SCREEN_SIZE[1]-BORDER_PAD-round(PLAYER_HEIGHT/2)) 
    player = Player(screen, PLAYER_COLOR, start_pos, (PLAYER_WIDTH,PLAYER_HEIGHT)) # instantiate player object

    GAMEOVER = False # flag to exit main loop

    clock = pygame.time.Clock() # controls framerate

    while not GAMEOVER:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMEOVER = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and player.rect.centery != BORDER_PAD: 
            player.move(0,-1)
        if pressed[pygame.K_DOWN] and player.rect.centery != SCREEN_SIZE[1]-BORDER_PAD: 
            player.move(0,1)
        if pressed[pygame.K_LEFT] and player.rect.centerx != BORDER_PAD: 
            player.move(-1,0)
        if pressed[pygame.K_RIGHT] and player.rect.centerx != SCREEN_SIZE[0]-BORDER_PAD: 
            player.move(1,0)
        
        # redraw border in case the player erases it    
        pygame.draw.lines(screen, BORDER_COLOR, True, BORDER, BORDER_THICKNESS)
        
        pygame.display.flip() # update changes

        clock.tick(60)

########## ENTRY POINT ##########

if __name__ == '__main__':
    main()
