import pygame  
import time  

# Inicializar Pygame  
pygame.init()  

# Variables de configuración  
screen_width, screen_height = 800, 600  
WHITE = (255, 255, 255)  
BLUE = (0, 0, 255)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
GRAY = (200, 200, 200)  

# Crear la ventana  
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption("Simulación de Dron")  

# Fuente para el mensaje  
font = pygame.font.Font(None, 36)  

# Clase Robot  
class Dron:  
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
        self.message = f"Aterrizando: {item.tipo}"  

    def drop_item(self):  
        if self.item_picked:  
            dropped_item = self.item_picked.tipo  
            self.message = f"Direccion Recibida: {dropped_item}"  
            self.item_picked = None  

    def draw(self):  
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 50, 50))  

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

# Clase paciente  
class paciente:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  

    def draw(self):  
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 50, 50))  

# Crear instancias  
robot = Dron()  
items = [    
    Item(500, 150, "Direccion de Encontrada ")
]  

containers = [  
    paciente(500, 100),  
]  

# Bucle de simulación  
running = True  
while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  

    # Borrar pantalla  
    screen.fill(WHITE)  

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

    # Dibujar
        # Dibujar ítems, contenedores y el robot  
    for item in items:  
        item.draw()  
    for container in containers:  
        container.draw()  
    robot.draw()  

    # Mostrar mensajes sobre los ítems recogidos y estado actual  
    if robot.message:  
        texto = font.render(robot.message, True, (0, 0, 0))  
        screen.blit(texto, (20, 20))  


    # Mostrar qué objetos ha recogido el robot  
    collected_text = font.render(f"Ubicacion del Paciente: {', '.join(robot.collected_items)}", True, (0, 0, 0))  
    screen.blit(collected_text, (20, 100))  

    # Actualizar pantalla  
    pygame.display.flip()  

    # Controlar la velocidad de fotogramas  
    pygame.time.Clock().tick(60)  

# Cerrar Pygame correctamente  
pygame.quit()