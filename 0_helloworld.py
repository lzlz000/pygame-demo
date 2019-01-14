import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("pygame-哈哈哈")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    pygame.display.update()
