import tkinter as tk 
from tkinter import messagebox, simpledialog
from modulo_de_clases import Dron, Operador, ActividadesDron, Llamada, Persona, Camara, Altavoz
from Dron_interfaz import *  # Importar la función para iniciar la interfaz desde el nuevo módulo

class InterfazUsuarioLlamada:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de llamada de emergencia")
        
        # Crear un botón para simular las llamadas entrantes
        self.boton_llamada = tk.Button(self.root, text="Llamadas entrantes", command=self.simular_llamada)
        self.boton_llamada.pack()

        # Crear un botón para enviar el dron, pero inicialmente oculto
        self.boton_enviar_dron = tk.Button(self.root, text="Enviar dron", command=self.terminar_simulacion)
        self.boton_enviar_dron.pack()
        self.boton_enviar_dron.pack_forget()  # Ocultar el botón inicialmente

    def simular_llamada(self):
        # Solicitar nombre y ubicación a través de cuadros de diálogo
        nombre_persona = simpledialog.askstring("Nombre", "Introduce el nombre de la persona que llama:")
        ubicacion = simpledialog.askstring("Ubicación", "Introduce la ubicación de la persona que llama (formato: x,y,z):")
        
        # Convertir la ubicación a una lista de enteros
        ubicacion = [int(coordenada) for coordenada in ubicacion.split(',')]

        # Crear instancias de las clases
        camara = Camara()
        altavoz = Altavoz()
        dron1 = Dron("Dron ", ubicacion, camara, altavoz, True, True)  # Primer dron
        operador = Operador()
        operador.drones = [dron1, dron2]  # Asignar los drones al operador
        persona = Persona(nombre_persona)
        llamada = Llamada(persona.nombre, ubicacion)

        # Crear actividad de dron
        actividades = ActividadesDron(dron1)
        
        # Verificar las coordenadas antes de continuar
        if actividades.verificar_coordenadas(ubicacion):
            # Simular la llamada
            llamada.simular_llamada(operador, dron1)
            operador.dar_instrucciones(persona)
            persona.colocar_almohadillas()

            # Simular fallo del dron (batería o motores)
            if not dron1.bateria or not dron1.motores:
                messagebox.showwarning("Emergencia", "El dron ha fallado. Enviando otro dron.")
                operador.manejar_fallo(dron1, ubicacion)

            # Comunicar desde el altavoz del dron
            dron1.altavoz.comunicar("Instrucciones del operador")

            # Mostrar mensaje de que el dron ha sido enviado
            messagebox.showinfo("Dron enviado", "El dron se ha enviado a las coordenadas del paciente.")

            # Verificar que todo esté en su lugar con la cámara
            if camara.observar():
                # Añadir el botón para iniciar la desfibrilación
                self.boton_desfibrilacion = tk.Button(self.root, text="Iniciar desfibrilación", command=actividades.Iniciar_desfibrilacion)
                self.boton_desfibrilacion.pack()

            messagebox.showinfo("Simulación completada", "La simulación de la llamada de emergencia ha sido completada.")
        else:
            messagebox.showwarning("Error", "Las coordenadas proporcionadas son inválidas. Por favor, proporciona tres números separados por comas.")
        
        # Mostrar el botón para enviar el dron una vez terminada la simulación
        self.boton_enviar_dron.pack()

    def terminar_simulacion(self):
        # Llamar la función para iniciar la interfaz desde el nuevo módulo
        iniciar_interfaz_estados()

# Crear la ventana principal y ejecutar la interfaz
root = tk.Tk()
app = InterfazUsuarioLlamada(root)
root.mainloop()