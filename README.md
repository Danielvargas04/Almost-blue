# Almost-blue
## Juego de Plataformas 

¡Bienvenido/a a nuestro **Juego de Plataformas**! Este proyecto busca demostrar cómo, a partir de funciones y clases, se pueden crear niveles y enemigos con diferentes mecánicas de manera **flexible** y **escalable**.

---

## Tabla de Contenidos
1. [Características Principales](#características-principales)  
2. [Requerimientos](#requerimientos)  
3. [Controles](#controles)  
4. [Cómo Jugar](#cómo-jugar)  
5. [Construcción Modular de Niveles](#construcción-modular-de-niveles)  
6. [Enemigos y Clases](#enemigos-y-clases)  

---

## Características Principales

1. **Construcción Modular:** Los niveles se generan a partir de funciones que permiten reutilizar y combinar elementos de forma rápida.  
2. **Enemigos con Diferentes Mecánicas:** Gracias al enfoque orientado a objetos, es sencillo crear nuevas clases que extiendan o modifiquen el comportamiento de los enemigos.  
3. **Controles Simples:** Solo se requiere el uso de las teclas de flechas para moverse y la barra espaciadora para saltar.  
4. **Mecánica de Combate Básica:** Para eliminar a un enemigo, basta con caerle encima.

---

## Requerimientos

- **Lenguaje de Programación:** Python (versión 3.8 o superior recomendada).  
- **Librerías / Frameworks:**  
  - [Pygame](https://www.pygame.org/news) (Para la parte gráfica y de eventos).  
- **Sistema Operativo:** Probado en Windows y Linux. En macOS también debería funcionar, pero no ha sido probado exhaustivamente.

*Asegúrate de instalar todas las dependencias necesarias antes de ejecutar el proyecto.*

---

## Controles

- **Flecha Izquierda / Derecha**: Mover al personaje horizontalmente.  
- **Flecha Arriba** (o **Barra Espaciadora**): Saltar.  
- **Flecha Abajo**: Agacharse (si existe esa mecánica).  
- **Teclas numéricas (1, 2 o 3)**: Seleccionar nivel (si está habilitado en el menú).  
- **Esc**: Regresar al menú o salir, dependiendo de la pantalla.

---

## Cómo Jugar

1. **Menú Principal**: Al iniciar, verás un fondo o interfaz sencilla que te permite elegir el nivel a jugar (usando las teclas 1, 2 o 3, por ejemplo).  
2. **Selección de Nivel**: Escoge el nivel deseado y automáticamente se cargará la escena correspondiente (plataformas, enemigos, etc.).  
3. **Acción**: Muévete con las flechas del teclado. Salta sobre los enemigos para derrotarlos. Evita caer al vacío, ya que perderás vidas.  
4. **Game Over**: Si te quedas sin vidas, aparecerá una pantalla de fin de juego. Presiona la tecla indicada (por ejemplo, Esc) para volver al menú principal y reintentar.

---

## Construcción Modular de Niveles

Este juego implementa un **sistema de generación de niveles** basado en funciones. Cada nivel está definido en una función separada (por ejemplo, `level1()`, `level2()`, `level3()`), la cual:
- Crea las plataformas (superficies o “tiles”).  
- Instancia los enemigos en sus posiciones iniciales.  
- Devuelve los grupos de sprites (`platforms_group`, `enemies_group`, `all_sprites`) y el `player` configurado para ese nivel.

Esto facilita enormemente **reiniciar** o **cambiar de nivel** sin reescribir lógica de colisiones ni manejo de sprites. Solo se llama a la función del nivel deseado y se inicia el bucle de juego.

---

## Enemigos y Clases

El juego utiliza un **enfoque orientado a objetos** para manejar distintos tipos de enemigos y sus comportamientos:
- **Enemigo terrestre** (`GroundEnemy`): Se mueve horizontalmente, daña al jugador si colisiona de lado y muere si el jugador le cae encima.  
- **Enemigo volador** (`FlyingEnemy` o `SkyEnemy`): Se desplaza por el aire siguiendo límites definidos (puede moverse en X e Y).  
- **Fácil Extensión**: Para añadir un nuevo enemigo con mecánicas distintas (disparo, patrullaje inteligente, etc.), solo necesitas crear una nueva clase que herede de `pygame.sprite.Sprite` e implemente su método `update()` y su lógica de colisión.

---

¡Disfruta de **Almost-blue** y explora la construcción modular de niveles y enemigos!  
