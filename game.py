import pygame

from creature import Creature

pygame.init()

window = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
clock = pygame.time.Clock()
run = True

creature = Creature()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    creature.draw(window)
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
exit()
