import pygame

#https://stackoverflow.com/questions/45178397/how-do-i-make-it-so-that-my-walking-animation-plays-at-a-set-speed-python-pyg
# definir une classe qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):

    #definir les choses à faire à la création de l'entitié
    def __init__(self,sprite_name):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'assets/{sprite_name}.png'),(200,200))
        self.current_image = 0 # commencer l'animation à l'image 0
        self.frame=0 #index du cadre de l'animation
        self.timer = 0 #le temps en seconde
        self.images = animations.get(sprite_name)
        self.animation = False

    #defnir une méthode pour démarrer l'animation
    def start_animation(self,status):
        self.animation = True


    #definir une methode pour animer le sprite
    def animate(self,dt):

        #verifier si l'animation est active
        if self.animation:
            self.timer +=dt # on incrémente le timer
            #Si let imer est au desssu de la limite désirée
            if self.timer >=0.05:
                self.timer = 0 # on repasse le timer à 0
                self.frame += 1 # # on incrémente l'index du cadre
                self.frame%= len(self.images) # on garde l'index dans le range
                #passer à l'image suivante
                self.current_image +=1
                #verifier si on a atteint la fin de l'animation
                if self.current_image >=len(self.images):
                    #remettre l'animation au départ
                    self.current_image=0
                    #self.animation = False

                #modifier l'image précédente par la suivante
                self.image = self.images[self.current_image]



# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name,status):
    # charger les images de ce sprite dans le dossier
    images = []
    #name=sprite_name.split("_")[0]
    #name=sprite_name
    #status='idle'
    #status=sprite_name.split("_")[1]
    #recupérer le chemin du dossier de ce sprite
    path = f"assets/{sprite_name}/{status}/"

    #boucler sur chaque image dans ce dossier
    for num in range(0,8):
        image_path = path + sprite_name+status+'_'+ str(f"{num:03d}") + '.png'
        images.append(pygame.transform.scale(pygame.image.load(image_path),(200, 200)))
        #images.append(pygame.image.load(image_path))


    #print(images)

    #renvoyer le contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenir les images chargées
animations = {
    'player' : load_animation_images('player','idle'),
    'player_run' : load_animation_images('player','run')
}
