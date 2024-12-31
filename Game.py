import pygame
import sys
from player import *
from enemies import *
from levels import *

#---------------------------
#       Almost Blue
#---------------------------

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

player, platforms_group, enemies_group, all_sprites = level2()

# Estado inicial del juego
state_menu = "menu"
state_playing = "playing"
state_game_over = "game_over"
state_victory = "victory"

game_state = state_menu
game_over_flag = False


### Imagenes

bg_image = pygame.image.load("figures/background.png").convert()
bg_image = pygame.transform.scale(bg_image, (800, 400))

victory_image = pygame.image.load("figures/medallav2.png").convert_alpha()
victory_image = pygame.transform.scale(victory_image, (200, 200))

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
            if event.type == pygame.KEYDOWN:
                # El jugador elige qué nivel jugar
                if event.key == pygame.K_1:
                    player, platforms_group, enemies_group, all_sprites = level1()
                    game_state = state_playing
                elif event.key == pygame.K_2:
                    player, platforms_group, enemies_group, all_sprites = level2()
                    game_state = state_playing
                elif event.key == pygame.K_3:
                    player, platforms_group, enemies_group, all_sprites = level3()
                    game_state = state_playing

        elif game_state == state_game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Reiniciar todo
                game_state = state_menu
                game_over_flag = False

        elif game_state == state_victory:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Reiniciar todo
                game_state = state_menu
                game_over_flag = False    

    # Logica del estado playing

    if game_state==state_playing:
        game_over_flag = player.update(platforms_group)
        enemies_group.update()
        collisions = pygame.sprite.spritecollide(player, enemies_group, False)

        for enemy in collisions:
            enemy.on_collision(player)

        if len(enemies_group) == 0:
            game_state = state_victory
            pass

    if game_over_flag:
        game_state = state_game_over

    # Dibujado
    screen.fill((0, 0, 0))          # Fondo negro
    
    if game_state == state_menu:
            # Dibujamos un menú sencillo
            screen.blit(bg_image, (0, 0))
            draw_text(screen, "Almost Blue", 300, 250, font, (50, 50, 100))
            draw_text(screen, "Pulsa 1, 2 o 3 para elegir nivel", 240, 275, font, (50, 50, 200))

    elif game_state == state_playing or game_state == state_victory:
        # Dibujamos el escenario
        screen.blit(bg_image, (0, 0))
        all_sprites.draw(screen)
        # Dibujar las vidas en la esquina
        draw_text(screen, f"Vidas: {player.lives}", 10, 10, font, (255, 255, 255))

        if len(enemies_group) == 0:
            screen.blit(victory_image, (300, 100))  # Ajusta la posición
            draw_text(screen, "¡Nivel completado!", 300, 300, font, (20,20,255))
            draw_text(screen, "Pulsa Esc para volver al MENU", 240, 350, font, (50, 50, 200))

    elif game_state == state_game_over:
        screen.blit(bg_image, (0, 0))
        draw_text(screen, "GAME OVER", 330, 150, font, (255, 0, 0))
        draw_text(screen, "Pulsa Esc para volver al MENU", 240, 200, font, (255, 255, 255))

    # Actualizamos la ventana
    pygame.display.flip()

# Cerramos Pygame
pygame.quit()
sys.exit()
