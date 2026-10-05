# clases.py

class Camara:
    def __init__(self):
        pass

    def observar(self):
        print("Verificando que todo esté en su lugar")
        return True

class Altavoz:
    def __init__(self):
        pass

    def comunicar(self, mensaje):
        print("Ahora lleva el dron donde está tu padre")
        print("Coloca las almohadillas que están en el compartimento del dron a tu padre")
        print("Aléjate de tu padre")

class Dron:
    def __init__(self, nombre, coor_emergencia, camara, altavoz, bateria, motores):
        self.nombre = nombre
        self.coor_emergencia = coor_emergencia
        self.camara = camara
        self.altavoz = altavoz
        self.bateria = bateria
        self.motores = motores
        self.state = None

class ActividadesDron:
    def __init__(self, dron):
        self.dron = dron

    def verificar_coordenadas(self, coordenadas):
        if len(coordenadas) != 3:
            return False
        else:
            return True
    
    def volar(self, ubicacion):
        if self.verificar_coordenadas(ubicacion):
            print(f"{self.dron.nombre}: Dirigiéndose a las coordenadas {ubicacion}")
        else:
            print("Coordenadas inválidas")

    def apagar(self):
        print(f"{self.dron.nombre}: Apagando")

    def encender(self):
        print(f"{self.dron.nombre}: Encendiendo...")

    def Emergencia(self):
        print(f"{self.dron.nombre}: EMERGENCIA...")

    def ahorrar_bateria(self):
        print(f"{self.dron.nombre}: Ahorrando batería")

    def recargar(self):
        print(f"{self.dron.nombre}: Recargando")

    def navegar(self, coordenadas):
        print(f"{self.dron.nombre}: Navegando a las coordenadas de EMERGENCIA {coordenadas}")

    def iniciar(self):
        print("Iniciando vuelo")

    def validar(self, ubicacion):
        print(f"{self.dron.nombre}: sin errores en las coordenadas :D {ubicacion}")

    def Obstaculos(self):
        print("Se ha detectado obstaculos durante el vuelo")
    
    def esquivar(self):
        print("Esquivando obstaculos")

    def viajar(self):
        print(f"{self.dron.nombre}: Viajando uwu")

    def notificar(self):
        print("¡Turbulencia!")

    def mirar(self):
        print("Mostrando signos vitales")

    def Detectar(self):
        print("Un espacio cerca de la ubicación")

    def Iniciar_desfibrilacion(self):
        print("Iniciando descarga")

class Operador:
    def __init__(self):
        self.llamadas = []
        self.drones = []

    def atender_llamada(self, llamada):
        self.llamadas.append(llamada)
        print(f"Operador: ¿Cuál es tu nombre?")
        print(f"{llamada.nombre}: Mi nombre es {llamada.nombre}.")
        print(f"Operador: ¿Por qué estás llamando?")
        print(f"{llamada.nombre}: Mi padre está sufriendo un ataque al corazón.")
        print(f"Operador: ¿Dónde estás ubicado?")
        print(f"{llamada.nombre}: Estoy en {llamada.ubicacion}.")
        print(f"Operador: Envío un dron a tu ubicación.")

    def enviar_dron(self, ubicacion):
        actividades_dron = ActividadesDron(self.drones[0])  # Asumiendo que solo hay un dron disponible
        actividades_dron.volar(ubicacion)
        actividades_dron.validar(ubicacion)

    def dar_instrucciones(self, persona):
        print(f"Operador: {persona.nombre}, desabrocha la camisa de tu padre.")
        print(f"Operador: Ahora, recoge el dron.")
        print(f"Operador: Puedes colgar la llamada. Te daré instrucciones desde el altavoz del dron.")

    def manejar_fallo(self, dron_fallido, coordenadas_emergencia):
        print(f"Operador: Dron fallido, vuelve a las coordenadas de emergencia.")
        for dron in self.drones:
            if dron != dron_fallido and dron.verificar_estado():
                print(f"Operador: Enviando otro dron.")
                actividades_dron = ActividadesDron(dron)
                actividades_dron.volar(coordenadas_emergencia)
                break

class Llamada:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def simular_llamada(self, operador, dron):
        print(f"{self.nombre} llama al operador.")
        operador.atender_llamada(self)
        print(f"El operador obtiene la ubicación de {self.nombre}.")
        operador.enviar_dron(self.ubicacion)

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def colocar_almohadillas(self):
        print("Listo")

class eventos_drone:
    def __init__(self, Tipo, atendido):
        self.Tipo = Tipo
        self.atendido = atendido
