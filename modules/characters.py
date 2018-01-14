#!/usr/bin/env python

import pygame

class Player:
    '''
    Class to represent the player.
    '''
    def __init__(self, surface, color, position, dimensions):
        self.rect = pygame.rect.Rect(position, dimensions)
        self.surface = surface
        self.color = color
        self.position = position
        self.dimensions = dimensions
        pygame.draw.rect(surface, color, self.rect)

    def move(self, offsetX, offsetY):
        pygame.draw.rect(self.surface, (0,0,0), self.rect)
        self.rect.move_ip(offsetX, offsetY)
        pygame.draw.rect(self.surface, self.color, self.rect)

class Sparx:
    '''
    Class to represent a sparx.
    '''
    def __init__(self, position):
        self.position = position

    def move(self):
        raise NotImplementedError('Sparx.move has not been implemented.')

class Qix:
    '''
    Class to represent a qix.
    '''
    def __init__(self):
        raise NotImplementedError('Qix class has not been implemented.')

