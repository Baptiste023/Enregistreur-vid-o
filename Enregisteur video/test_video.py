import os
import pygame

from Enregistreur import Enregistreur
from Constante import*


os.environ["SDL_VIDEODRIVER"]="dummy"
pygame.init()
screen = pygame.display.set_mode((Largeur,Hauteur))

print(screen.get_size())


enregistreur=Enregistreur(Hauteur=Hauteur,Largeur=Largeur,FPS=FPS,chemin="test_video.mp4",duree_min=4)

running=True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((255, 255, 255))
    x = 50 + 5 * cpt_frame
    pygame.draw.rect(screen, (0, 0, 0), (x, 50, 150, 100))
    enregistreur.ajouter_image(screen)



    pygame.display.flip()
    if cpt_frame>=FPS*3:
        running=False
    cpt_frame+=1
enregistreur.pause(duree=2)
test1=enregistreur.exporter()
print(test1)



pygame.quit()


