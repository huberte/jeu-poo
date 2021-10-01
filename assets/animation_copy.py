import pygame


# definir une classe qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):

    #definir les choses à faire à la création de l'entitié
    def __init__(self,sprite_name):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'assets/{sprite_name}.png'),(200,200))
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #defnir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True


    #definir une methode pour animer le sprite
    def animate(self):
        #verifier si l'aniamtion est active
        if self.animation:
            #passer à l'image suivante
            self.current_image +=1
            #verifier si on a attetint la find e l'animation
            if self.current_image >=len(self.images):
                #remettre l'animation au départ
                self.current_image=0
                #self.animation = False

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]



# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images de ce sprite dans le dossier
    images = []
    #recupérer le chemin du dossier de ce sprite
    path = f"assets/{sprite_name}/idle/"

    #boucler sur chaque image dans ce dossier
    for num in range(0,8):
        image_path = path + sprite_name+'idle_'+ str(f"{num:03d}") + '.png'
        images.append(pygame.transform.scale(pygame.image.load(image_path),(200, 200)))
        #images.append(pygame.image.load(image_path))


        #print(images)

    #renvoyer le contenu de la liste d'images
    return images

#definir un dictionnaire qui va contenir les images chargées
animations = {
    'player' : load_animation_images('player')
}
