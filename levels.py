from enemies import *

def level1():
    # Definicion de grupos
    platforms_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()


    # Creacion de plataformas
    floor = Platform(25, 400 - 25, 800-50, 25)      # Piso que ocupa todo el ancho

    # Agregar las plataformas al grupo
    platforms_group.add(floor)

    #Inicializacion de enemigos
    enemy_floor = FloorEnemy(600, 400-25-30, speed=2, left_limit= 25, right_limit=800-25)
    enemy_sky = SkyEnemy(400, 200)
    enemies_group.add(enemy_floor, enemy_sky)

    # Inicializacion de jugador
    player = Player(100, 200)

    # Incluimos elementos al sprites
    all_sprites.add(enemy_floor, player, floor, enemy_sky)
    
    return player, platforms_group, enemies_group, all_sprites

def level2():
    # Definicion de grupos
    platforms_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()


    # Creacion de plataformas
    floor = Platform(25, 400 - 25, 800-50, 25)      # Piso que ocupa todo el ancho
    platform1 = Platform(350, 180, 150, 10)          
    platform2 = Platform(120, 280, 100, 10)
    platform3 = Platform(600, 280, 100, 10)

    # Agregar las plataformas al grupo
    platforms_group.add(floor)
    platforms_group.add(platform1, platform2, platform3)

    # Inicializacion de jugador
    player = Player(100, 100)

    #Inicializacion de enemigos
    enemy_floor = FloorEnemy(600, 250, speed=2, left_limit= 600, right_limit=700)

    enemies_group.add(enemy_floor)

    # Incluimos elementos al sprites
    all_sprites.add(player, enemy_floor)
    all_sprites.add(floor, platform1, platform2, platform3)

    return player, platforms_group, enemies_group, all_sprites