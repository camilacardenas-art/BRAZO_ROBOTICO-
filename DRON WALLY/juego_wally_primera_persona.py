import pygame
import random

# Inicializar Pygame
pygame.init()

# Establecer resolución de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Título del juego
pygame.display.set_caption("Robot Explorador Autónomo (Primera Persona)")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)  # Color para obstáculos

# Fuente de texto
font = pygame.font.SysFont(None, 36)

# Clase RobotActivity con detección de colisiones
class RobotActivity:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.velocidad = 5
        self.claw_open = False
        self.item_picked = None
        self.collected_items = []
        self.message = ""  # Mensaje actual en pantalla

    def move(self, dx, dy, obstacles):
        # Calcula la nueva posición potencial del robot
        new_x = self.x + dx * self.velocidad
        new_y = self.y + dy * self.velocidad
        
        # Verifica colisión antes de mover
        if not self.collide_with_obstacles(new_x, self.y, obstacles):
            self.x = new_x
        if not self.collide_with_obstacles(self.x, new_y, obstacles):
            self.y = new_y

    def collide_with_obstacles(self, new_x, new_y, obstacles):
        robot_rect = pygame.Rect(new_x - 25, new_y - 25, 50, 50)  # Rectángulo del robot
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.get_width(), obstacle.get_height())
            if robot_rect.colliderect(obstacle_rect):
                return True  # Colisión detectada
        return False  # No hay colisión

    def open_claw(self):
        self.claw_open = True

    def close_claw(self):
        self.claw_open = False

    def pick_item(self, item):
        if self.claw_open and not self.item_picked:
            if item.tipo in ["humano", "animal"]:
                self.message = f"{item.tipo.capitalize()} detectado: No es basura"
            else:
                self.item_picked = item
                item.recogido = True
                self.message = f"Recogido: {item.tipo}"

    def drop_item(self, container):
        if self.item_picked:
            self.item_picked.x = container.x + 15
            self.item_picked.y = container.y + 15
            self.message = f"Objeto soltado en el contenedor: {container.x}, {container.y}"
            self.item_picked = None

# Clase Item (basura, humanos, animales)
class Item:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.recogido = False

    def draw(self, offset_x, offset_y):
        if not self.recogido:
            color = RED if self.tipo in ["basura", "metal", "papel"] else BLUE
            pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))

# Clase Container
class Container:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, offset_x, offset_y):
        pygame.draw.rect(screen, GREEN, (self.x - offset_x, self.y - offset_y, 50, 50))

# Clase Obstacle con detección de tamaño
class Obstacle:
    def __init__(self, x, y, largo=False):
        self.x = x
        self.y = y
        self.largo = largo  # Si el obstáculo es largo o pequeño

    def get_width(self):
        return 100 if self.largo else 40

    def get_height(self):
        return 20 if self.largo else 40

    def draw(self, offset_x, offset_y):
        pygame.draw.rect(screen, GRAY, (self.x - offset_x, self.y - offset_y, self.get_width(), self.get_height()))

# Crear instancia del robot
robot = RobotActivity()

# Crear artículos, humanos, animales, contenedores y obstáculos
items = [
    Item(100, 100, "botella plástica"),
    Item(200, 200, "lata"),
    Item(300, 300, "recipiente plástico"),
    Item(400, 100, "papel"),
    Item(500, 150, "vidrio"),
    Item(600, 250, "metal"),
    Item(700, 300, "plástico"),
    Item(750, 400, "cartón"),
    Item(50, 550, "bolsa plástica"),
    Item(120, 480, "metal")
]

organismos_vivos = [
    Item(100, 400, "humano"),
    Item(200, 500, "animal"),
    Item(300, 450, "humano"),
    Item(600, 150, "animal"),
    Item(450, 500, "humano"),
    Item(700, 550, "animal"),
]

containers = [
    Container(500, 100),
    Container(600, 200),
    Container(700, 300),
    Container(400, 400),
    Container(100, 200)
]

obstacles = [
    Obstacle(350, 150, largo=True),
    Obstacle(450, 250),
    Obstacle(550, 350, largo=True),
    Obstacle(300, 300),
    Obstacle(100, 50, largo=True),
    Obstacle(200, 150),
    Obstacle(400, 500, largo=True),
    Obstacle(600, 450),
    Obstacle(700, 200, largo=True),
]

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Control del robot con teclas de flechas
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    robot.move(dx, dy, obstacles)  # Pasar obstáculos al método move

    # Abrir y cerrar garra con la tecla espacio
    if keys[pygame.K_SPACE]:
        robot.open_claw()
    else:
        robot.close_claw()

    # Recoger objetos cercanos
    for item in items + organismos_vivos:
        if not item.recogido and abs(robot.x - item.x) < 20 and abs(robot.y - item.y) < 20:
            robot.pick_item(item)

    # Soltar objetos en contenedores cercanos
    for container in containers:
        if robot.item_picked and abs(robot.x - container.x) < 50 and abs(robot.y - container.y) < 50:
            robot.drop_item(container)

    # Dibujar fondo (blanco)
    screen.fill(WHITE)

    # Dibujar artículos, organismos vivos, contenedores y obstáculos en función de la posición del robot
    offset_x, offset_y = robot.x - SCREEN_WIDTH // 2, robot.y - SCREEN_HEIGHT // 2

    for item in items:
        item.draw(offset_x, offset_y)
    for organismo in organismos_vivos:
        organismo.draw(offset_x, offset_y)
    for container in containers:
        container.draw(offset_x, offset_y)
    for obstacle in obstacles:
        obstacle.draw(offset_x, offset_y)

    # Dibujar el campo de visión del robot
    pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 2 - 25, 50, 50))

    # Mostrar el mensaje actual en pantalla
    if robot.message:
        texto = font.render(robot.message, True, (0, 0, 0))
        screen.blit(texto, (20, 20))

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

# Cerrar Pygame correctamente
pygame.quit()
