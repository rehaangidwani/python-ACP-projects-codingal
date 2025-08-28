import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Color Changer")
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
sprite1_color = colors[0]
sprite2_color = colors[1]
sprite1 = pygame.Rect(200, 250, 100, 100)
sprite2 = pygame.Rect(500, 250, 100, 100)
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            sprite1_color = random.choice(colors)
            sprite2_color = random.choice(colors)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)
    pygame.display.flip()
pygame.quit()
sys.exit()
