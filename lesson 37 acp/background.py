import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  
pygame.display.set_caption("Space Invader - Level Up")
background = pygame.image.load("background.png")  


pygame.mixer.music.load("background.mp3")  
pygame.mixer.music.play(-1) 
laser_sound = pygame.mixer.Sound("laser.wav") 
running = True
while running:
    screen.blit(background, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_sound.play()

    pygame.display.update()
pygame.quit()
