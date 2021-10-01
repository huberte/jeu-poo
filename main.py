# Créé par Svend, le 21/09/2021 avec EduPython
import pygame
from game import Game
pygame.init()
clock = pygame.time.Clock()
dt = 0

#generer la fenetre de notre jeu
pygame.display.set_caption("Mon jeu de Prof")
screen = pygame.display.set_mode((1080,720))

#importer image arrière plan
background = pygame.image.load('assets/bg.png')

#charger le joueur
#player = Player()

#charger notrte jeu
game = Game()

running = True

#boucle tant que c'est vrai

while running:

    #appliquer l'arrière plan sur surface
    screen.blit(background, (0,0))
    print(game.player.__dict__)

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    #on passe dt dans l'update des animations
    game.player.update_animation(dt)

    #vérifier si le joueur veut aller à droite ou à ga uche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width< screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()
    # dt est le temps qui est passé depuis la dernier appel clock.tick
    # on divise par 1000 pour convertir les ms en s
    dt = clock.tick(30) / 1000

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fentre
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
            print("c'est fermé")
        #detecter si un joueur, lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False










