import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Carga de imagen inicial o spritesheet
        #self.image = pygame.image.load("figures/player/stick_man_stand.png").convert_alpha()
        #self.rect = self.image.get_rect()
        #self.rect.topleft = (x, y)

        self.image = pygame.Surface((20, 40))
        self.image.fill((0, 0, 150))  
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Vidas y daños
        self.lives = 3
        self.spawn_x = x
        self.spawn_y = y
        self.damage = 1

        # Velocidades
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        
        # Configuraciones para salto
        self.jump_speed = -18
        self.gravity = 1

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
        
        if keys[pygame.K_SPACE]:
            # Lógica para saltar
            if self.on_floor() or self.is_on_ground: 
                self.vel_y = self.jump_speed

    def on_floor(self):
        # Retornar True si está tocando el suelo

        if self.rect.bottom >= 375:
            return True
        else:
            return False
    
    def on_wall(self):
        # Retornar True si está tocando una pared

        if self.rect.left <= 0:
            return 'left'
        elif self.rect.right >= 800:
            return 'right'
        else:
            return 'none'

    def apply_gravity(self):
        # Aplicamos gravedad
        self.vel_y += self.gravity
        # Limitamos la velocidad de caída o ajustamos por colisión
        if self.vel_y > 15:
            self.vel_y = 15

    def update(self, platforms_group):
        # Procesar input
        self.handle_input()
        
        # Aplicar gravedad
        self.apply_gravity()
        
        # Actualizar posición
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        #self.rect.y += self.vel_y

        # Checar colisiones verticales
        collided_platforms = pygame.sprite.spritecollide(self, platforms_group, False)
        self.is_on_ground = False  # asumimos que no está en el suelo
        for platform in collided_platforms:
            # Si estamos cayendo
            if self.vel_y > 0 and self.rect.bottom >= platform.rect.top:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.is_on_ground = True
            # Si estamos saltando y chocamos con el techo de la plataforma
            elif self.vel_y < 0 and self.rect.top <= platform.rect.bottom:
                self.rect.top = platform.rect.bottom
                self.vel_y = 0

        # Coliciones horizontales
        collided_platforms = pygame.sprite.spritecollide(self, platforms_group, False)
        for platform in collided_platforms:
            if self.vel_x > 0 and not self.on_floor():  # yendo a la derecha
                self.rect.right = platform.rect.left
            elif self.vel_x < 0 and not self.on_floor():  # yendo a la izquierda
                self.rect.left = platform.rect.right

        # Verificar si el jugador se "cayo" del escenario
        if self.rect.top > 400:
            self.lives -= 1
            # Si aún hay vidas, reubicar al jugador en (spawn_x, spawn_y)
            if self.lives > 0:
                self.rect.topleft = (self.spawn_x, self.spawn_y)
                self.vel_y = 0
            else:
                # Manejar game over, por ejemplo
                return True
        #Jugador se quedo sin vidas
        if self.lives <=0:
            return True
        
        # False == Playing
        return False

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 50, 0))  
        self.rect = self.image.get_rect(topleft=(x, y))

def draw_text(surface, text, x, y, font, color=(255,255,255)):
    """Función de utilidad para dibujar texto."""
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect()
    rect.topleft = (x, y)
    surface.blit(text_surf, rect)