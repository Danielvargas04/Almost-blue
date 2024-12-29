import pygame
import sys
from player import Player
from player import Platform

#Game_name

# Inicializacion de Pygame
pygame.init()

# Definicion de dimensiones de la ventana
wigth, heigth = 800, 400
screen = pygame.display.set_mode((wigth, heigth))
pygame.display.set_caption("Game_name")

clock = pygame.time.Clock()


# Definicion de reloj para controlar FPS
clock = pygame.time.Clock()

# Definicion de plataformas
platforms_group = pygame.sprite.Group()

floor = Platform(25, heigth - 25, wigth-50, 25)      # Piso que ocupa todo el ancho
platform1 = Platform(350, 180, 100, 10)          # Plataforma en (200,300)
platform2 = Platform(120, 280, 100, 10)
platform3 = Platform(600, 280, 100, 10)

# 3) Agregar las plataformas al grupo
platforms_group.add(floor)
platforms_group.add(platform1, platform2, platform3)



# Iinicializacion de jugador
player = Player(100, 100)

all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(floor)
all_sprites.add(floor, platform1, platform2, platform3)

# Loop principal
running = True
while running:
    # Limitacion de los FPS a 60
    clock.tick(60)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Lógica del juego (movimientos, colisiones, etc.)
    player.update(platforms_group)
     
    # Dibujado
    screen.fill((0, 0, 0))          # Fondo negro
    all_sprites.draw(screen)        # Dibujamos jugador y plataformas
    pygame.display.flip()
    
    # Actualizamos la ventana
    pygame.display.flip()

# Cerramos Pygame
pygame.quit()
sys.exit()
