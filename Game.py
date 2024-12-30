import pygame
import sys
from player import *
from enemies import *
from levels import *

#Game_name

# Inicializacion de Pygame
pygame.init()

# Definicion de dimensiones de la ventana
wigth, heigth = 800, 400
screen = pygame.display.set_mode((wigth, heigth))
pygame.display.set_caption("Game_name")

# Definicion de reloj para controlar FPS
clock = pygame.time.Clock()

# Fuente para dibujar texto (vidas, menús, etc.)
font = pygame.font.SysFont(None, 36)

# Definicion de grupos
platforms_group = None
all_sprites = None
enemies_group = None

# Definicion de nivel
nivel = level1()

player, platforms_group, enemies_group, all_sprites = level1()

# Estado inicial del juego
state_menu = "menu"
state_playing = "playing"
state_game_over = "game_over"

game_state = state_menu
game_over_flag = False
# Loop principal
running = True
while running:
    # Limitacion de los FPS a 60
    clock.tick(60)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manejo  para cambiar de estado con teclas:
        if game_state == state_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Con Esc pasamos a jugar
                game_state = state_playing

        elif game_state == state_game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Reiniciar todo
                player, platforms_group, enemies_group, all_sprites = level1()
                player.lives = 3
                player.rect.topleft = (player.spawn_x, player.spawn_y)
                game_state = state_menu
                game_over_flag = False

    if game_state==state_playing:
        game_over_flag = player.update(platforms_group)
        enemies_group.update()
        collisions = pygame.sprite.spritecollide(player, enemies_group, False)

        for enemy in collisions:
            enemy.on_collision(player)

    if game_over_flag:
        game_state = state_game_over

    # Dibujado
    screen.fill((0, 0, 0))          # Fondo negro
    
    if game_state == state_menu:
            # Dibujamos un menú sencillo
            draw_text(screen, "MENU PRINCIPAL", 300, 150, font, (255, 255, 255))
            draw_text(screen, "Pulsa Esc para JUGAR", 280, 200, font, (255, 255, 255))

    elif game_state == state_playing:
        # Dibujamos el escenario
        all_sprites.draw(screen)
        # Dibujar las vidas en la esquina
        draw_text(screen, f"Vidas: {player.lives}", 10, 10, font, (255, 255, 255))

    elif game_state == state_game_over:
        draw_text(screen, "GAME OVER", 330, 150, font, (255, 0, 0))
        draw_text(screen, "Pulsa Esc para volver al MENU", 240, 200, font, (255, 255, 255))

    # Actualizamos la ventana
    pygame.display.flip()

# Cerramos Pygame
pygame.quit()
sys.exit()
