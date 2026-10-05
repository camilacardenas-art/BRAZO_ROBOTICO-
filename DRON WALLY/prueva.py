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

        screen.fill(WHITE)

        # Mostrar información sobre el robot
        title_text = font_big.render("Descripción del Robot Wally", True, BLACK)
        control_text = font.render("Controles:", True, BLACK)
        control_info_text1 = font.render("Flechas: Moverse", True, BLACK)
        control_info_text2 = font.render("Espacio: Abrir/Cerrar Garra", True, BLACK)
        qualities_text = font.render("Cualidades:", True, BLACK)
        qualities_info_text_1 = font.render("1. Autónomo", True, BLACK)
        qualities_info_text_2 = font.render("2. Recolector de Basura", True, BLACK)
        qualities_info_text_3 = font.render("3. Detección de Humanos", True, BLACK)
        items_text = font.render("Objetos que puede recoger:", True, BLACK)
        items_info_text = font.render("Plástico, Metal, Vidrio, Papel, Cartón", True, BLACK)
        not_items_text = font.render("Objetos que NO recoge:", True, BLACK)
        not_items_info_text = font.render("Humanos, Animales", True, BLACK)
        return_text = font.render("Presiona ESC para volver", True, RED)

        # Dibujar texto en pantalla
        screen.blit(title_text, (150, 50))
        screen.blit(control_text, (50, 150))
        screen.blit(control_info_text1, (50, 190))
        screen.blit(control_info_text2, (50, 230))
        screen.blit(qualities_text, (50, 270))
        screen.blit(qualities_info_text_1, (50, 310))
        screen.blit(qualities_info_text_2, (50, 350))
        screen.blit(qualities_info_text_3, (50, 390))
        screen.blit(items_text, (50, 430))
        screen.blit(items_info_text, (50, 470))
        screen.blit(not_items_text, (50, 510))
        screen.blit(not_items_info_text, (50, 550))
        screen.blit(return_text, (50, 590))

        pygame.display.update()

# Clase Robot
class Robot:
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
            pygame.draw.rect(screen, RED, (self.x, self.y, 20, 20))

# Clase Container
class Container:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 50, 50))

# Función de la simulación automática (video)
def run_video_simulation():
    robot = Robot()
    items = [
        Item(100, 100, "Botella plástica"),
        Item(200, 200, "Lata"),
        Item(300, 300, "Recipiente plástico"),
        Item(400, 100, "Papel"),
        Item(500, 150, "Vidrio")
    ]
    containers = [
        Container(500, 100),
        Container(600, 200),
        Container(700, 300),
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
        screen.fill(WHITE)

        # Movimiento del robot
        if robot.item_picked is None:
            target_item = next((item for item in items if not item.recogido), None)
            if target_item:
                if abs(robot.x - target_item.x) > 25 or abs(robot.y - target_item.y) > 25:
                    robot.move_towards(target_item.x, target_item.y)
                else:
                    robot.pick_item(target_item)
                    time.sleep(1)  # Simula el tiempo de recogida
        else:
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
            texto = font.render(robot.message, True, BLACK)
            screen.blit(texto, (20, 20))

        # Mostrar cuántos objetos quedan por recoger
        remaining_items = [item for item in items if not item.recogido]
        remaining_text = font.render(f"Objetos Restantes: {len(remaining_items)}", True, BLACK)
        screen.blit(remaining_text, (20, 60))

        # Mostrar qué objetos ha recogido el robot
        collected_text = font.render(f"Objetos Recogidos: {', '.join(robot.collected_items)}", True, BLACK)
        screen.blit(collected_text, (20, 100))

        # Mostrar coordenadas del robot
        coords_text = font.render(f"Coordenadas: X={robot.x}, Y={robot.y}", True, BLACK)
        screen.blit(coords_text, (20, 140))

        # Actualizar pantalla
        pygame.display.flip()

        # Controlar la velocidad de fotogramas
        pygame.time.Clock().tick(60)

# Clase Robot para simulación interactiva
class RobotActivity:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.velocidad = 5
        self.claw_open = False
        self.items = [Item(100, 100, "Botella plástica"), Item(200, 200, "Lata")]
        self.collected_items = []

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def toggle_claw(self):
        self.claw_open = not self.claw_open

    def draw(self):
        pygame.draw.rect(screen, VIOLET, (self.x, self.y, 50, 50))  # Robot
        claw_text = "Abierta" if self.claw_open else "Cerrada"
        claw_info = font.render(f"Garra: {claw_text}", True, BLACK)
        screen.blit(claw_info, (self.x, self.y - 20))

# Función principal
def main_menu():
    buttons = [
        Button("Iniciar Simulación Automática", 250, 200, 300, 50, GREEN, run_video_simulation),
        Button("Iniciar Simulación Interactiva", 250, 300, 300, 50, GREEN, interactive_simulation),
        Button("Ver Descripción del Robot", 250, 400, 300, 50, GREEN, show_robot_description),
        Button("Salir", 250, 500, 300, 50, RED, pygame.quit),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event.pos):
                        if button.action:
                            button.action()  # Ejecutar la acción del botón

        screen.fill(WHITE)
        for button in buttons:
            button.draw()

        pygame.display.update()

# Simulación interactiva
def interactive_simulation():
    robot = RobotActivity()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    robot.move(-robot.velocidad, 0)
                if event.key == pygame.K_RIGHT:
                    robot.move(robot.velocidad, 0)
                if event.key == pygame.K_UP:
                    robot.move(0, -robot.velocidad)
                if event.key == pygame.K_DOWN:
                    robot.move(0, robot.velocidad)
                if event.key == pygame.K_SPACE:
                    robot.toggle_claw()

        screen.fill(WHITE)
        robot.draw()
        
        # Mostrar información adicional
        remaining_text = font.render(f"Objetos: {len(robot.items)}", True, BLACK)
        screen.blit(remaining_text, (20, 20))

        pygame.display.update()
        pygame.time.Clock().tick(60)

# Iniciar el menú principal
main_menu()
