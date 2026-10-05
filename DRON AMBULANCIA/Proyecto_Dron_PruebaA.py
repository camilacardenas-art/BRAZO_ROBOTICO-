import tkinter as tk
import random

class InterfazUsuarioLlamada:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de llamada de emergencia")
        self.root.configure(bg="black")  # Fondo negro para la ventana principal
        
        # Crear un Canvas para la animación
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black", highlightthickness=0)
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
        self.frame_botones = tk.Frame(self.root, bg="black")
        self.frame_botones.pack()

        # Crear botones de simulación
        self.boton_llamada = self.crear_boton("Llamadas entrantes", self.simular_llamada)
        self.boton_enviar_dron = self.crear_boton("Enviar Dron", self.iniciar_vuelo)
        self.boton_bateria_baja = self.crear_boton("Aviso de Batería Baja", self.bateria_baja)
        self.boton_obstaculo_fijo = self.crear_boton("Obstáculo Fijo", self.obstaculo_fijo)
        self.boton_obstaculo_movil = self.crear_boton("Obstáculo Móvil", self.obstaculo_movil)
        self.boton_localizacion_invalida = self.crear_boton("Localización Inválida", self.localizacion_invalida)
        self.boton_turbulencia = self.crear_boton("Alta Turbulencia", self.turbulencia)
        self.boton_falla_motor = self.crear_boton("Falla en Motor", self.falla_motor)
        self.boton_lugar_libre = self.crear_boton("Lugar Libre para Aterrizar", self.lugar_libre)
        self.boton_ocupacion_lugar = self.crear_boton("Ocupación de Lugar de Aterrizaje", self.ocupacion_lugar)
        self.boton_volver_casa = self.crear_boton("Volver a Casa", self.volver_casa)
        self.boton_otra_emergencia = self.crear_boton("Otra Emergencia", self.otra_emergencia)
        self.boton_signos_vitales = self.crear_boton("Signos Vitales", self.signos_vitales)

    def crear_boton(self, texto, comando):
        """Crea un botón con los colores personalizados."""
        boton = tk.Button(
            self.frame_botones,
            text=texto,
            command=comando,
            bg="black",
            fg="white",
            activebackground="gray",
            activeforeground="white",
            highlightbackground="black"
        )
        boton.pack(pady=2)
        return boton

    def simular_llamada(self):
        """Simula una llamada entrante y muestra un mensaje de alerta en el canvas."""
        self.canvas.delete("all")  # Limpiar el canvas para mostrar el nuevo mensaje
        self.canvas.create_text(300, 150, text="¡Llamada Entrante!", fill="red", font=("Helvetica", 30))

    def iniciar_vuelo(self):
        """Inicia el vuelo del dron."""
        self.canvas.delete("all")  # Limpia el canvas para iniciar el vuelo
        self.canvas.create_text(300, 150, text="Dron en vuelo", fill="white", font=("Helvetica", 30))

    def bateria_baja(self):
        """Simula una baja batería en el dron."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="¡Batería Baja!", fill="red", font=("Helvetica", 30))

    def obstaculo_fijo(self):
        """Simula la presencia de un obstáculo fijo."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Obstáculo Fijo", fill="orange", font=("Helvetica", 30))

    def obstaculo_movil(self):
        """Simula un obstáculo móvil en el camino del dron."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Obstáculo Móvil", fill="orange", font=("Helvetica", 30))

    def localizacion_invalida(self):
        """Simula que el dron ha perdido su localización."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Localización Inválida", fill="red", font=("Helvetica", 30))

    def turbulencia(self):
        """Simula que el dron está experimentando turbulencia."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Turbulencia", fill="yellow", font=("Helvetica", 30))

    def falla_motor(self):
        """Simula una falla en el motor del dron."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Falla en Motor", fill="red", font=("Helvetica", 30))

    def lugar_libre(self):
        """Simula que hay un lugar libre para aterrizar."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Lugar Libre para Aterrizar", fill="green", font=("Helvetica", 30))

    def ocupacion_lugar(self):
        """Simula que el lugar de aterrizaje está ocupado."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Lugar Ocupado", fill="red", font=("Helvetica", 30))

    def volver_casa(self):
        """Simula que el dron está regresando a casa."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Volviendo a Casa", fill="blue", font=("Helvetica", 30))

    def otra_emergencia(self):
        """Simula una nueva emergencia para el dron."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Otra Emergencia", fill="red", font=("Helvetica", 30))

    def signos_vitales(self):
        """Muestra los signos vitales en el canvas."""
        self.canvas.delete("all")
        self.canvas.create_text(300, 150, text="Signos Vitales: OK", fill="green", font=("Helvetica", 30))

# Configuración de la interfaz de usuario
root = tk.Tk()
ui = InterfazUsuarioLlamada(root)
root.mainloop()
