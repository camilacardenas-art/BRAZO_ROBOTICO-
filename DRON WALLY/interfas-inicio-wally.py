import pygame
import time
import sys

# Inicializar Pygame
pygame.init()

# Variables de configuración
screen_width, screen_height = 800, 600
WHITE = (255, 255, 255)
VIOLET = (148, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


# Crear la ventana
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Robot Wally")

# Fuente para el mensaje
font = pygame.font.Font(None, 36)
font_big = pygame.font.Font(None, 48)

# Clase Botón
class Button:
    def __init__(self, text, x, y, width, height, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font_big.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Función para mostrar la descripción del robot
def show_robot_description():
    description_running = True
    while description_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                description_running = False  # Volver al menú principal

        screen.fill(BLACK)

        # Mostrar información sobre el robot
        title_text = font_big.render("Descripción del Robot Wally", True, WHITE)
        control_text = font.render("Controles:", True, WHITE)
        control_info_text1 = font.render("Flechas: Moverse", True, WHITE)
        control_info_text2 = font.render("Espacio: Abrir/Cerrar Garra", True, WHITE)
        qualities_text = font.render("Cualidades:", True, WHITE)
        qualities_info_text_1 = font.render("1. Autónomo", True, WHITE)
        qualities_info_text_2 = font.render("2. Recolector de Basura: AZUL(PP), AMARILLO(ALU) Y VERDE(V)", True, WHITE)
        qualities_info_text_3 = font.render("3. Detección de Humanos y Animales", True, WHITE)
        items_text = font.render("Objetos que puede recoger:", True, WHITE)
        items_info_text = font.render("Plástico AZUL(PP), Metal AMARILLO(ALU) y Vidrio VERDE(V)", True, WHITE)
        not_items_text = font.render("Objetos que NO recoge:", True, WHITE)
        not_items_info_text = font.render("Humanos ROJOS y Animales NARANJAS", True, WHITE)
        return_text = font.render("Presiona ESC para volver", True, RED)

        # Dibujar texto en pantalla
        screen.blit(title_text, (150, 50))
        screen.blit(control_text, (30, 150))
        screen.blit(control_info_text1, (30, 190))
        screen.blit(control_info_text2, (30, 230))
        screen.blit(qualities_text, (30, 270))
        screen.blit(qualities_info_text_1, (30, 310))
        screen.blit(qualities_info_text_2, (30, 350))
        screen.blit(qualities_info_text_3, (30, 390))
        screen.blit(items_text, (30, 430))
        screen.blit(items_info_text, (30, 470))
        screen.blit(not_items_text, (30, 510))
        screen.blit(not_items_info_text, (30, 550))
        screen.blit(return_text, (30, 580))

        pygame.display.update()

# Función de la simulación del "video" (automático)
def run_video_simulation():
    # Clase Robot
    class RobotIA:
        def __init__(self):
            self.x = 50
            self.y = 50
            self.item_picked = None  # Almacena el ítem recogido
            self.collected_items = []  # Lista de objetos recogidos
            self.message = ""  # Mensaje actual en pantalla
            self.speed = 1  # Velocidad de movimiento

        def move_towards(self, target_x, target_y):
            if self.x < target_x:
                self.x += self.speed
            elif self.x > target_x:
                self.x -= self.speed

            if self.y < target_y:
                self.y += self.speed
            elif self.y > target_y:
                self.y -= self.speed

        def pick_item(self, item):
            item.recogido = True
            self.item_picked = item
            self.collected_items.append(item.tipo)  # Agrega el ítem a la lista de recogidos
            self.message = f"Recogido: {item.tipo}"

        def drop_item(self):
            if self.item_picked:
                dropped_item = self.item_picked.tipo
                self.message = f"Objeto Soltado: {dropped_item}"
                self.item_picked = None

        def draw(self):
            pygame.draw.rect(screen, VIOLET, (self.x, self.y, 50, 50))

    # Clase Item
    class Item:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self):
            if not self.recogido:
                pygame.draw.rect(screen, BLUE, (self.x, self.y, 20, 20))
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

    # Clase Container
    class Container_1:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self):
            pygame.draw.rect(screen, BLUE, (self.x, self.y, 50, 50))
    class Container_2:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self):
            pygame.draw.rect(screen, GREEN, (self.x, self.y, 50, 50))
    class Container_3:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self):
            pygame.draw.rect(screen, YELLOW, (self.x, self.y, 50, 50))

    # Crear instancias
    robot = RobotIA()
    items = [
        Item(100, 100, "Botella plástica"),
        Item(200, 200, "Plato plastico"),
        Item(300, 300, "Recipiente plástico"),
        Item(400, 100, "Tapas plasticas"),
        Item(500, 150, "Bolsa plastica")
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
    containers = [
        Container_1(500, 100),
        Container_2(600, 200),
        Container_3(700, 300),
    ]

    # Bucle de simulación
    running_sim = True
    while running_sim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running_sim = False  # Salir de la simulación

        # Borrar pantalla
        screen.fill(BLACK)

        # Movimiento del robot
        if robot.item_picked is None:
            # Intentar recoger un ítem
            target_item = next((item for item in items if not item.recogido), None)
            if target_item:
                if abs(robot.x - target_item.x) > 25 or abs(robot.y - target_item.y) > 25:
                    robot.move_towards(target_item.x, target_item.y)
                else:
                    robot.pick_item(target_item)
                    time.sleep(1)  # Simula el tiempo de recogida
        else:
            # Intentar dejar el ítem en el contenedor
            target_container = next((container for container in containers), None)
            if target_container:
                if abs(robot.x - target_container.x) > 25 or abs(robot.y - target_container.y) > 25:
                    robot.move_towards(target_container.x, target_container.y)
                else:
                    robot.drop_item()
                    time.sleep(1)  # Simula el tiempo de dejar el ítem

        # Dibujar ítems, contenedores y el robot
        for item in items:
            item.draw()
        for container in containers:
            container.draw()
        robot.draw()

        # Mostrar mensajes sobre los ítems recogidos y estado actual
        if robot.message:
            texto = font.render(robot.message, True, WHITE)
            screen.blit(texto, (20, 20))

        # Mostrar cuántos objetos quedan por recoger
        remaining_items = [item for item in items if not item.recogido]
        remaining_text = font.render(f"Objetos Restantes: {len(remaining_items)}", True, WHITE)
        screen.blit(remaining_text, (20, 60))

        # Mostrar qué objetos ha recogido el robot
        collected_text = font.render(f"Objetos Recogidos: {', '.join(robot.collected_items)}", True, WHITE)
        screen.blit(collected_text, (20, 100))

        # *** Adición: Mostrar coordenadas del robot ***
        coords_text = font.render(f"Coordenadas: X={robot.x}, Y={robot.y}", True, WHITE)
        screen.blit(coords_text, (20, 140))

        # Actualizar pantalla
        pygame.display.flip()

        # Controlar la velocidad de fotogramas
        pygame.time.Clock().tick(60)

# Función de la simulación interactiva (la que enviaste originalmente)
def run_interactive_simulation():
    class RobotActivity:
        def __init__(self):
            self.x = screen_width // 2
            self.y = screen_height // 2
            self.velocidad = 5
            self.claw_open = False
            self.item_picked = None
            self.collected_items = []  # Lista de objetos recogidos
            self.message = ""  # Mensaje actual en pantalla

        def move(self, dx, dy, obstacles):
            new_x = self.x + dx * self.velocidad
            new_y = self.y + dy * self.velocidad
            if not self.collide_with_obstacles(new_x, self.y, obstacles):
                self.x = new_x
            if not self.collide_with_obstacles(self.x, new_y, obstacles):
                self.y = new_y

        def collide_with_obstacles(self, new_x, new_y, obstacles):
            robot_rect = pygame.Rect(new_x - 25, new_y - 25, 50, 50)
            for obstacle in obstacles:
                obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.get_width(), obstacle.get_height())
                if robot_rect.colliderect(obstacle_rect):
                    return True
            return False

        def open_claw(self):
            self.claw_open = True

        def close_claw(self):
            self.claw_open = False

        def pick_item(self, item):
            if self.claw_open and not self.item_picked:
                if item.tipo in ["Humano", "Animal"]:
                    self.message = f"{item.tipo.capitalize()} Detectado: No es basura"
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

        def draw(self):
            pygame.draw.rect(screen, VIOLET, (self.x - 25, self.y - 25, 50, 50))

    class Item_1:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self, offset_x, offset_y):
            if not self.recogido:
                color = YELLOW if self.tipo in ["Metal"] else YELLOW
                pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))
    class Item_2:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self, offset_x, offset_y):
            if not self.recogido:
                color = BLUE if self.tipo in ["Basura", "Metal", "Papel"] else BLUE
                pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))
    class Item_3:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self, offset_x, offset_y):
            if not self.recogido:
                color = GREEN if self.tipo in ["Basura", "Metal", "Papel"] else GREEN
                pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))
    class Item_4:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self, offset_x, offset_y):
            if not self.recogido:
                color = RED if self.tipo in ["Basura", "Metal", "Papel"] else RED
                pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))
    class Item_5:
        def __init__(self, x, y, tipo):
            self.x = x
            self.y = y
            self.tipo = tipo
            self.recogido = False

        def draw(self, offset_x, offset_y):
            if not self.recogido:
                color = ORANGE if self.tipo in ["Basura", "Metal", "Papel"] else ORANGE
                pygame.draw.rect(screen, color, (self.x - offset_x, self.y - offset_y, 20, 20))

    class Container_1:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def draw(self, offset_x, offset_y):
            pygame.draw.rect(screen, GREEN, (self.x - offset_x, self.y - offset_y, 50, 50))
    class Container_2:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def draw(self, offset_x, offset_y):
            pygame.draw.rect(screen, YELLOW, (self.x - offset_x, self.y - offset_y, 50, 50))
    class Container_3:
        def __init__(self, x, y):
            self.x = x
            self.y = y                 

        def draw(self, offset_x, offset_y):
            pygame.draw.rect(screen, BLUE, (self.x - offset_x, self.y - offset_y, 50, 50))

    class Obstacle:
        def __init__(self, x, y, largo=False):
            self.x = x
            self.y = y
            self.largo = largo

        def get_width(self):
            return 100 if self.largo else 40

        def get_height(self):
            return 20 if self.largo else 40

        def draw(self, offset_x, offset_y):
            pygame.draw.rect(screen, GRAY, (self.x - offset_x, self.y - offset_y, self.get_width(), self.get_height()))

    robot = RobotActivity()

    items = [
        Item_2(360, 710, "Botella plástica"),
        Item_1(210, 290, "Lata"),
        Item_2(340, 350, "Recipiente plástico"),
        Item_3(420, 120, "Trosos de ventana"),
        Item_3(510, 160, "Botella de vidrio"),
        Item_1(610, 270, "LLaves de metal"),
        Item_3(750, 410, "Vidrio roto"),
        Item_2(520, 555, "Bolsa plástica"),
        Item_1(820, 480, "Trosos de metal")
    ]

    organismos_vivos = [
        Item_4(100, 400, "Humano"),
        Item_5(200, 500, "Animal"),
        Item_4(300, 450, "Humano"),
        Item_5(600, 150, "Animal"),
        Item_4(450, 500, "Humano"),
        Item_5(700, 550, "Animal"),
        Item_4(800, 400, "Humano"),
        Item_5(900, 500, "Animal"),
        Item_4(1000, 450, "Humano"),
        Item_5(1200, 150, "Animal"),
        Item_4(1300, 500, "Humano"),
        Item_5(1400, 550, "Animal"),
    ]

    containers = [
        Container_1(500, 100),
        Container_2(600, 200),
        Container_3(700, 300),
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
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_running = False  # Salir de la simulación

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        robot.move(dx, dy, obstacles)

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
        screen.fill(BLACK)

        # Dibujar artículos, organismos vivos, contenedores y obstáculos en función de la posición del robot
        offset_x, offset_y = robot.x - screen_width // 2, robot.y - screen_height // 2

        for item in items:
            item.draw(offset_x, offset_y)
        for organismo in organismos_vivos:
            organismo.draw(offset_x, offset_y)
        for container in containers:
            container.draw(offset_x, offset_y)
        for obstacle in obstacles:
            obstacle.draw(offset_x, offset_y)

        # Dibujar el campo de visión del robot
        pygame.draw.rect(screen, VIOLET, (screen_width // 2 - 25, screen_height // 2 - 25, 50, 50))

        # Mostrar mensajes sobre los ítems recogidos y estado actual
        if robot.message:
            texto = font.render(robot.message, True, WHITE)
            screen.blit(texto, (40, 500))

        # Mostrar cuántos objetos quedan por recoger
        remaining_items = [item for item in items if not item.recogido]
        remaining_text = font.render(f"Objetos Restantes: {len(remaining_items)}", True, WHITE)
        screen.blit(remaining_text, (40, 80))

        # *** Adición: Mostrar coordenadas del robot en la simulación interactiva ***
        coords_text = font.render(f"Coordenadas: X={robot.x}, Y={robot.y}", True, WHITE)
        screen.blit(coords_text, (90, 60))

        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)

# Crear botones en la pantalla inicial
button_interactive_simulation = Button("Iniciar Simulación", 250, 200, 310, 50, VIOLET, run_interactive_simulation)
button_video_simulation = Button("Ver Video de Simulación", 200, 300, 410, 50, VIOLET, run_video_simulation)
button_robot_description = Button("Descripción del Robot", 210, 400, 380, 50, VIOLET, show_robot_description)
button_exit = Button("Salir", 250, 500, 300, 50, RED, sys.exit)

# Bucle principal de la interfaz
running = True
while running:
    screen.fill(BLACK)

    # Título principal
    title_text = font_big.render("Robot Wally", True, WHITE)
    screen.blit(title_text, (300, 100))
     # Nombres de grupo
    title_text = font_big.render("Sharon, Junior y Martin:  Proyecto Wally", True, WHITE)
    screen.blit(title_text, (50, 560))

    # Dibujar los botones
    button_interactive_simulation.draw()
    button_video_simulation.draw()
    button_robot_description.draw()
    button_exit.draw()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Verificar si se ha hecho clic en algún botón
            if button_interactive_simulation.is_clicked(mouse_pos):
                run_interactive_simulation()  # Inicia la simulación interactiva
            if button_video_simulation.is_clicked(mouse_pos):
                run_video_simulation()  # Inicia la simulación automática (video)
            if button_robot_description.is_clicked(mouse_pos):
                show_robot_description()  # Muestra la descripción del robot
            if button_exit.is_clicked(mouse_pos):
                running = False

    pygame.display.update()

pygame.quit()
