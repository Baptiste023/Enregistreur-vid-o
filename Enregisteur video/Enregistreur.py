import numpy as np , pygame, imageio, os



class Enregistreur:
    def __init__(self,Hauteur,Largeur,FPS,chemin,duree_min):
        self.Hauteur = Hauteur
        self.Largeur = Largeur
        self.FPS = FPS
        self.writer = imageio.get_writer(chemin, fps=self.FPS,macro_block_size=1)
        self.dernière_image=None
        self.compteur=0
        self.duree_min=duree_min
        self.chemin=chemin

    def ajouter_image(self, screen):
        if screen.get_size()!=(self.Largeur,self.Hauteur):
            raise ValueError("taille de fentre differente, valeur pygame",screen.get_size(),"et valeur enregistreur",self.Largeur,self.Hauteur)
        image = pygame.surfarray.array3d(screen)
        image=np.swapaxes(image,0,1)
        self.writer.append_data(image)
        self.dernière_image=image
        self.compteur+=1


    def exporter(self):

        self.writer.close()
        temps=self.compteur/self.FPS
        print("Temps d'enregistreur : ",temps)
        if temps<=self.duree_min:
            os.remove(self.chemin)
            return False
        elif temps>=self.duree_min+30:
            os.remove(self.chemin)
            return False
        else:
            return True


    def pause(self,duree):
        fin=int(self.FPS*duree)
        image_fin=self.dernière_image
        for i in range(fin):
            self.writer.append_data(image_fin)
            self.compteur+=1





