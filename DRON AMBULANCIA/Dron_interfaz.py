import tkinter as tk
from threading import Thread
from modulo_maquina_estados_clases import *  # Asegúrate de que el sistema de máquinas de estado esté bien definido
from modulo_de_clases import *  # Asegúrate de que las clases como Dron, Operador, etc., estén importadas correctamente

class InterfazEstados:
    def __init__(self, root):
        self.root = root

        # Crear marcos para cada grupo de botones
        self.frame_error = tk.Frame(self.root)
        self.frame_correcto = tk.Frame(self.root)

        # Crear títulos para cada grupo de botones
        self.titulo_error = tk.Label(self.frame_error, text="Simulación Error")
        self.titulo_correcto = tk.Label(self.frame_correcto, text="Simulación Correcta")

        # Crear botones para cada evento
        # Los primeros 5 botones van en el marco 'frame_error'
        self.btn_enviardrone = tk.Button(self.frame_error, text="Enviar dron", command=self.iniciar_dron)
        self.btn_avisobateria = tk.Button(self.frame_error, text="Batería baja", command=self.avisobateria)
        self.btn_llegoahome = tk.Button(self.frame_error, text="Emergencia", command=self.llegoahome)
        self.btn_localizar = tk.Button(self.frame_error, text="Comenzar vuelo", command=self.comenzar_vuelo)
        self.btn_coordenadas = tk.Button(self.frame_error, text="Obstáculos en el vuelo", command=self.Coordenadas_validas)
        self.btn_detectar = tk.Button(self.frame_error, text="Turbulencia", command=self.error)
        
        # El resto de los botones van en el marco 'frame_correcto'
        self.btn_identificar = tk.Button(self.frame_correcto, text="Comenzar vuelo", command=self.enviar_drone2)
        self.btn_aterrizar = tk.Button(self.frame_correcto, text="Sin problemas", command=self.sin_fallos)
        self.btn_final = tk.Button(self.frame_correcto, text="Obstáculos detectados", command=self.obstaculos)
        self.btn_obstaculos = tk.Button(self.frame_correcto, text="Esquivar", command=self.esquivando)
        self.btn_vida = tk.Button(self.frame_correcto, text="Vida", command=self.vida)
        self.btn_permiso = tk.Button(self.frame_correcto, text="Permiso", command=self.permiso)
        self.btn_llegarahome = tk.Button(self.frame_correcto, text="Llegó a casa", command=self.llegarahome)

        # Añadir los títulos y botones a los marcos
        self.titulo_error.pack()
        self.btn_localizar.pack()
        self.btn_avisobateria.pack()
        self.btn_coordenadas.pack()
        self.btn_detectar.pack()
        self.btn_llegoahome.pack()
        self.btn_enviardrone.pack()

        self.titulo_correcto.pack()
        self.btn_identificar.pack()
        self.btn_aterrizar.pack()
        self.btn_final.pack()
        self.btn_obstaculos.pack()
        self.btn_vida.pack()
        self.btn_permiso.pack()
        self.btn_llegarahome.pack()

        # Añadir los marcos a la ventana
        self.frame_error.pack()
        self.frame_correcto.pack()

    # Funciones para los botones que interactúan con el sistema de máquina de estado
    def iniciar_dron(self):
        # Activa el trigger para el envío del dron
        drone_ambulancia.trigger('enviardrone')

    def avisobateria(self):
        # Activa el trigger para el aviso de batería baja
        drone_ambulancia.trigger('avisobateria')

    def llegoahome(self):
        # Activa el trigger cuando el dron ha llegado a casa
        drone_ambulancia.trigger('llegoahome')

    def comenzar_vuelo(self):
        # Activa el trigger para iniciar el vuelo
        drone_ambulancia.trigger('comenzar_vuelo')

    def Coordenadas_validas(self):
        # Activa el trigger para validar las coordenadas
        drone_ambulancia.trigger('Coordenadas_validas')

    def error(self):
        # Activa el trigger para indicar un error
        drone_ambulancia.trigger('error')

    def enviar_drone2(self):
        # Activa el trigger para enviar el segundo dron
        drone_ambulancia.trigger('enviar_drone2')

    def sin_fallos(self):
        # Activa el trigger cuando no hay fallos
        drone_ambulancia.trigger('sin_fallos')

    def obstaculos(self):
        # Activa el trigger cuando se detectan obstáculos
        drone_ambulancia.trigger('obstaculos')

    def esquivando(self):
        # Activa el trigger para esquivar obstáculos
        drone_ambulancia.trigger('esquivando')

    def vida(self):
        # Activa el trigger para verificar la vida
        drone_ambulancia.trigger('vida')

    def permiso(self):
        # Activa el trigger para verificar permiso
        drone_ambulancia.trigger('permiso')

    def llegarahome(self):
        # Activa el trigger cuando el dron llega a casa
        drone_ambulancia.trigger('llegarahome')

def iniciar_interfaz_estados():
    # Crear un thread que gestiona el estado del sistema
    state_checker = Thread(target=check_state)  # Aquí se asume que tienes una función 'check_state' definida
    state_checker.start()

    # Crear la ventana principal de la interfaz
    root = tk.Tk()

    # Crear la aplicación de la interfaz de estados
    app = InterfazEstados(root)

    # Iniciar el bucle principal de la interfaz
    root.mainloop()

    # Esperar a que el thread de gestión de estado termine
    app.state_checker.join()

