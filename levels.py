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
    enemy_sky = SkyEnemy(400, 275, up_limit=70 , down_limit= 100)
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
    platform1 = Platform(350, 180, 150, 18)          
    platform2 = Platform(120, 280, 120, 18)
    platform3 = Platform(600, 280, 100, 18)

    # Agregar las plataformas al grupo
    platforms_group.add(floor)
    platforms_group.add(platform1, platform2, platform3)

    # Inicializacion de jugador
    player = Player(50, 100)

    #Inicializacion de enemigos
    enemy_floor = FloorEnemy(600, 250, speed=2, left_limit= 600, right_limit=700)
    enemy2_floor = FloorEnemy(180, 250, speed=2, left_limit= 120, right_limit=240)

    enemy_sky = SkyEnemy(600, 100, up_limit=90 , down_limit= 90, left_limit=100, right_limit=80)
    enemy2_sky = SkyEnemy(200, 100, up_limit=70 , down_limit= 100)

    enemies_group.add(enemy_floor, enemy2_floor, enemy_sky, enemy2_sky)

    # Incluimos elementos al sprites
    all_sprites.add(player, enemy_floor, enemy2_floor, enemy_sky, enemy2_sky)
    all_sprites.add(floor, platform1, platform2, platform3)

    return player, platforms_group, enemies_group, all_sprites

def level3():
    # Definicion de grupos
    platforms_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    enemies_group = pygame.sprite.Group()


    # Creacion de plataformas
    floor = Platform(25, 400 - 25, 800-50, 25)      # Piso que ocupa todo el ancho
    platform1 = Platform(350, 180, 150, 18)          
    platform2 = Platform(120, 280, 120, 18)

    # Agregar las plataformas al grupo
    platforms_group.add(floor)
    platforms_group.add(platform1, platform2)

    # Inicializacion de jugador
    player = Player(50, 100)

    #Inicializacion de enemigos
    enemy2_floor = FloorEnemy(180, 250, speed=2, left_limit= 120, right_limit=240)
    enemy3_floor = FloorEnemy(600, 400-25-30, speed=2, left_limit= 25, right_limit=800-25)
    enemy4_floor = FloorEnemy(400, 400-25-30, speed=1, left_limit= 25, right_limit=800-25)

    enemy_sky = SkyEnemy(600, 100, up_limit=90 , down_limit= 90, left_limit=100, right_limit=80)
    enemy2_sky = SkyEnemy(200, 100, up_limit=70 , down_limit= 100, speed=4)
    enemy3_sky = SkyEnemy(600, 200, up_limit=70 , down_limit= 100, speed=4)

    enemies_group.add(enemy2_floor, enemy3_floor, enemy4_floor, enemy_sky, enemy2_sky, enemy3_sky)

    # Incluimos elementos al sprites
    all_sprites.add(player, enemy2_floor, enemy3_floor, enemy4_floor, enemy_sky, enemy2_sky, enemy3_sky)
    all_sprites.add(floor, platform1, platform2)

    return player, platforms_group, enemies_group, all_sprites