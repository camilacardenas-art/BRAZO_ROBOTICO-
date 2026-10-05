import tkinter as tk
import random

class InterfazUsuarioLlamada:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de llamada de emergencia")
        
        # Crear un Canvas para la animación
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="skyblue")
        self.canvas.pack()

        # Inicializar el dron
        self.dron_img = None
        self.dron_x = 250  # Coordenada x del dron
        self.dron_y = 200  # Coordenada y del dron
        self.dron_speed = 5  # Velocidad del dron
        self.dron_direction = 0  # Dirección del dron (0 = arriba, 90 = derecha, 180 = abajo, 270 = izquierda)
        self.is_turbulent = False  # Para controlar si la turbulencia está activa
        self.is_landing = False  # Para saber si el dron está aterrizando

        # Crear marcos para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack()

        # Crear botones de simulación
        self.boton_llamada = tk.Button(self.frame_botones, text="Llamadas entrantes", command=self.simular_llamada)
        self.boton_llamada.pack()

        self.boton_enviar_dron = tk.Button(self.frame_botones, text="Enviar Dron", command=self.iniciar_vuelo)
        self.boton_enviar_dron.pack()

        self.boton_bateria_baja = tk.Button(self.frame_botones, text="Aviso de Batería Baja", command=self.bateria_baja)
        self.boton_bateria_baja.pack()

        self.boton_obstaculo_fijo = tk.Button(self.frame_botones, text="Obstáculo Fijo", command=self.obstaculo_fijo)
        self.boton_obstaculo_fijo.pack()

        self.boton_obstaculo_movil = tk.Button(self.frame_botones, text="Obstáculo Móvil", command=self.obstaculo_movil)
        self.boton_obstaculo_movil.pack()

        self.boton_localizacion_invalida = tk.Button(self.frame_botones, text="Localización Inválida", command=self.localizacion_invalida)
        self.boton_localizacion_invalida.pack()

        self.boton_turbulencia = tk.Button(self.frame_botones, text="Alta Turbulencia", command=self.turbulencia)
        self.boton_turbulencia.pack()

        self.boton_falla_motor = tk.Button(self.frame_botones, text="Falla en Motor", command=self.falla_motor)
        self.boton_falla_motor.pack()

        self.boton_lugar_libre = tk.Button(self.frame_botones, text="Lugar Libre para Aterrizar", command=self.lugar_libre)
        self.boton_lugar_libre.pack()

        self.boton_ocupacion_lugar = tk.Button(self.frame_botones, text="Ocupación de Lugar de Aterrizaje", command=self.ocupacion_lugar)
        self.boton_ocupacion_lugar.pack()

        self.boton_volver_casa = tk.Button(self.frame_botones, text="Volver a Casa", command=self.volver_casa)
        self.boton_volver_casa.pack()

        self.boton_otra_emergencia = tk.Button(self.frame_botones, text="Otra Emergencia", command=self.otra_emergencia)
        self.boton_otra_emergencia.pack()

        # Botón para los signos vitales
        self.boton_signos_vitales = tk.Button(self.frame_botones, text="Signos Vitales", command=self.signos_vitales)
        self.boton_signos_vitales.pack()

    def simular_llamada(self):
        """Simula una llamada entrante y muestra un mensaje de alerta en el canvas."""
        self.canvas.delete("all")  # Limpiar el canvas para mostrar el nuevo mensaje
        self.canvas.create_text(300, 150, text="¡Llamada Entrante!", fill="red", font=("Helvetica", 30))

    def animar_dron(self, estado):
        """Actualiza la animación del dron según el estado actual."""
        self.canvas.delete("all")  # Limpiar el canvas antes de cada nueva animación

        # Crear el suelo (parte verde)
        self.canvas.create_rectangle(0, 350, 600, 400, fill="green")  # Suelo

        if estado == "en_vuelo":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron en vuelo
            self.mover_dron(5, 0)  # Mover el dron hacia la derecha

        elif estado == "bateria_baja":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron en vuelo
            self.canvas.create_rectangle(50, 50, 550, 70, fill="gray")  # Barra de batería
            self.canvas.create_rectangle(50, 50, 150, 70, fill="red")  # Barra de batería baja
            self.mover_dron(0, 10)  # Mover el dron hacia abajo para aterrizar

        elif estado == "obstaculo_fijo":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron
            # Obstáculo fijo en la parte inferior
            self.canvas.create_rectangle(200, 300, 400, 400, fill="gray")  # Edificio (obstáculo)
            self.mover_dron(10, 0)  # Mover el dron hacia adelante (evitar obstáculos)
            self.girar_dron()  # Girar el dron para esquivar el obstáculo

        elif estado == "obstaculo_movil":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron
            self.canvas.create_oval(400, 150, 500, 250, fill="orange")  # Obstáculo móvil
            self.mover_dron(10, 0)  # Mover el dron hacia adelante (evitar obstáculos)
            self.girar_dron()  # Girar el dron para esquivar el obstáculo

        elif estado == "localizacion_invalida":
            self.canvas.create_rectangle(0, 0, 600, 400, fill="lightgray")  # Fondo de señal perdida
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron parado
            self.canvas.create_text(300, 50, text="Sin dirección existente", fill="red", font=("Helvetica", 20))

        elif estado == "turbulencia":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron
            self.vibrar_dron()  # Simular vibración debido a turbulencia

        elif estado == "falla_motor":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron aterrizando
            self.mover_dron(0, 10)  # Mover el dron hacia abajo para aterrizar

        elif estado == "lugar_libre":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron aterrizando
            self.canvas.create_rectangle(0, 300, 600, 400, fill="green")  # Suelo verde sólido
            self.mover_dron(0, 10)  # Mover el dron hacia abajo para aterrizar

        elif estado == "ocupacion_lugar":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron aterrizando
            self.canvas.create_rectangle(0, 300, 600, 400, fill="lightgray")  # Suelo ocupado
            self.mover_dron(0, 10)  # Mover el dron hacia abajo para aterrizar

        elif estado == "volviendo_a_casa":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron volviendo a casa
            self.mover_dron(10, -10)  # Mover el dron hacia arriba y luego hacia la derecha

        elif estado == "otra_emergencia":
            self.dron_img = self.canvas.create_oval(self.dron_x, self.dron_y, self.dron_x + 100, self.dron_y + 100, fill="green")  # Dron en vuelo
            self.mover_dron(-5, 0)  # Mover el dron hacia la izquierda

    def signos_vitales(self):
        """Muestra los signos vitales en el canvas."""
        self.canvas.delete("all")  # Limpiar el canvas
        self.canvas.create_text(300, 150, text="Signos Vitales: OK", fill="green", font=("Helvetica", 30))

    def iniciar_vuelo(self):
        """Inicia el vuelo del dron."""
        self.animar_dron("en_vuelo")

    def bateria_baja(self):
        """Simula una baja batería en el dron."""
        self.animar_dron("bateria_baja")

    def obstaculo_fijo(self):
        """Simula la presencia de un obstáculo fijo."""
        self.animar_dron("obstaculo_fijo")

    def obstaculo_movil(self):
        """Simula un obstáculo móvil en el camino del dron."""
        self.animar_dron("obstaculo_movil")

    def localizacion_invalida(self):
        """Simula que el dron ha perdido su localización."""
        self.animar_dron("localizacion_invalida")

    def turbulencia(self):
        """Simula que el dron está experimentando turbulencia."""
        self.animar_dron("turbulencia")

    def falla_motor(self):
        """Simula una falla en el motor del dron."""
        self.animar_dron("falla_motor")

    def lugar_libre(self):
        """Simula que hay un lugar libre para aterrizar."""
        self.animar_dron("lugar_libre")

    def ocupacion_lugar(self):
        """Simula que el lugar de aterrizaje está ocupado."""
        self.animar_dron("ocupacion_lugar")

    def volver_casa(self):
        """Simula que el dron está regresando a casa."""
        self.animar_dron("volviendo_a_casa")

    def otra_emergencia(self):
        """Simula una nueva emergencia para el dron."""
        self.animar_dron("otra_emergencia")

    def vibrar_dron(self):
        """Simula la vibración del dron por turbulencia."""
        if self.is_turbulent:
            dx = random.choice([-5, 0, 5])
            dy = random.choice([-5, 0, 5])
            self.mover_dron(dx, dy)
            self.root.after(50, self.vibrar_dron)

    def girar_dron(self):
        """Gira el dron para esquivar el obstáculo."""
        self.dron_direction = (self.dron_direction + 90) % 360  # Giro de 90 grados
        self.canvas.itemconfig(self.dron_img, angle=self.dron_direction)

    def mover_dron(self, dx, dy):
        """Mueve el dron en el canvas con un cambio en las coordenadas x e y."""
        if self.is_landing:  # Detener movimiento si está aterrizando
            return
        self.canvas.move(self.dron_img, dx, dy)
        self.root.after(100, self.mover_dron, dx, dy)  # Movimiento continuo para animar el dron

# Configuración de la interfaz de usuario
root = tk.Tk()
ui = InterfazUsuarioLlamada(root)
root.mainloop() 