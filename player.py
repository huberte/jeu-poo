import pygame
import animation


# crer une première classe qui va représenter notre joueur
class Player(animation.AnimateSprite):

    #on crée une première méthode
    def __init__(self):
        #on initialise la super classe
        super().__init__("player")
        self._status='idle'
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10
        #self.image = pygame.transform.scale(pygame.image.load('assets/player/idle/playerIdle_000.png'),(200,200))
        #on veut récuérer les coordonnées de l'image pour pouvoir la déplacer
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 550
        self.start_animation('idle')

    def _get_status(self):
        return self._status

    def _set_status(self,status):
        self._status = status

    def move_right(self):
        self.rect.x += self.velocity
        self.start_animation('run')

    def move_left(self):
        self.rect.x -= self.velocity

    def update_animation(self,dt):
        self.animate(dt)
