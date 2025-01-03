from player import *

class FloorEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=2, left_limit=50, right_limit=750):
        """
        x, y          = Posición inicial
        speed         = Velocidad horizontal
        left_limit    = Límite izquierdo de movimiento
        right_limit   = Límite derecho de movimiento
        """
        super().__init__()
        # Representación gráfica
        self.image_right = pygame.image.load("figures/floor_enemy_r.png").convert_alpha()
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image_right = pygame.transform.scale(self.image_right, (50, 30))
        self.image_left = pygame.transform.scale(self.image_left, (50, 30))

        # Arrancamos mirando a la derecha
        self.image = self.image_right
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Movimiento
        self.speed = speed
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.direction = 1  # 1 = derecha, -1 = izquierda

    def update(self):
        # Mover horizontalmente
        self.rect.x += self.speed * self.direction
        
        # Si llegamos al límite derecho, invertimos dirección
        if self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction = -1
        # Si llegamos al límite izquierdo, invertimos dirección
        elif self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction = 1

        # Escoger imagen según dirección
        if self.direction > 0:
            self.image = self.image_right
        else:
            self.image = self.image_left

    def on_collision(self, player):
        """
        Logica cuando se detecta que este enemigo colisiona con el jugador
        """
        # Revisar si el jugador viene 'desde arriba'
        if (player.rect.bottom <= self.rect.top + 20) and player.vel_y >= 0:
            self.kill()
            player.vel_y = -10

        else:

            # Se daña el jugador
            player.lives -= 1
            
            # Podrías aplicar knockback:
            if player.rect.centerx < self.rect.centerx:
                player.rect.x -= 35  # empujarlo a la izquierda
            else:
                player.rect.x += 35  # empujarlo a la derecha

class SkyEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=2, left_limit=50, right_limit=55, up_limit = 50, down_limit=70):
        """
        x, y          = Posición inicial
        speed         = Velocidad horizontal
        left_limit    = Límite izquierdo de movimiento
        right_limit   = Límite derecho de movimiento
        """
        super().__init__()
        original_image = pygame.image.load("figures/sky_enemy.png").convert_alpha()
        scaled_image = pygame.transform.scale(original_image, (45, 40))
        self.image = scaled_image
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Movimiento
        self.speed = speed
        self.left_limit = x-left_limit
        self.right_limit = x+right_limit
        self.up_limit = y-up_limit
        self.down_limit = y+down_limit
        self.direction_x = 1  # 1 = derecha, -1 = izquierda
        self.direction_y = 1  # 1 = abajo, -1 = arriba

    def update(self):
        # Mover horizontalmente
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        
        # Si llegamos al límite derecho, invertimos dirección
        if self.rect.right >= self.right_limit:
            self.rect.right = self.right_limit
            self.direction_x = -1
        # Si llegamos al límite izquierdo, invertimos dirección
        elif self.rect.left <= self.left_limit:
            self.rect.left = self.left_limit
            self.direction_x = 1

        # Si llegamos al límite superior, invertimos dirección
        if self.rect.top <= self.up_limit:
            self.rect.top = self.up_limit
            self.direction_y = 1
        # Si llegamos al límite inferior, invertimos dirección
        elif self.rect.bottom >= self.down_limit:
            self.rect.bottom = self.down_limit
            self.direction_y = -1

    def on_collision(self, player):
        """
        Logica cuando se detecta que este enemigo colisiona con el jugador
        """
        # Revisar si el jugador viene 'desde arriba'
        if (player.rect.bottom <= self.rect.top + 20) and player.vel_y >= 0:
            self.kill()
            player.vel_y = -10

        else:

            # Se daña el jugador
            player.lives -= 1
            
            # Podrías aplicar knockback:
            if player.rect.centerx < self.rect.centerx:
                player.vel_y -= 5
                player.rect.x -= 35  # empujarlo a la izquierda
                
            else:
                player.vel_y -= 5
                player.rect.x += 35  # empujarlo a la derecha

