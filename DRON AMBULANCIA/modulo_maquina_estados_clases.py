import time
from transitions import Machine, State  # type: ignore
from modulo_maquina_estados_clases import *  # Asegúrate de que todas las clases están aquí
from modulo_de_clases import Camara, Altavoz, Dron, ActividadesDron, eventos_drone

# Creación de instancias
coor_emergencia = 0,0,0
direccion = 1,8,5
camara = Camara()
altavoz = Altavoz()
dron1 = Dron("Dron 1", coor_emergencia, camara, altavoz, True, True)
dron2 = Dron("Dron 2", coor_emergencia, camara, altavoz, True, True)
drone_ambulancia = ActividadesDron(dron1)  # Se comienza con el dron1
eventos = eventos_drone('bateriabaja', False)

# Definición de estados y transiciones
states_drones_updated = [
    State(name='home', on_enter=['apagar']),
    State(name='navegando', on_enter=['Emergencia']),
    State(name='bateriabaja', on_enter=['ahorrar_bateria'], on_exit=['recargar']),
    State(name='iniciando_2vuelo', on_enter=['encender']),
    State(name='vuelo', on_enter=['iniciar', 'encender']),
    State(name='Deteccion', on_enter=['Obstaculos'], on_exit=['esquivar']),
    State(name='turbulencia', on_enter=['notificar']),
    State(name='ocupacion', on_enter=['Detectar']),
    State(name='Signos_vitales', on_enter=['mirar']),
    State(name='perfecto', on_enter=['viajar']),
    State(name='descarga_electrica', on_enter=['Iniciar_desfibrilacion'])
]

transitions_drone = [
    {'trigger': 'enviardrone', 'source': 'home', 'dest': 'navegando'},
    {'trigger': 'llegoahome', 'source': 'navegando', 'dest': 'home'},
    {'trigger': 'comenzar_vuelo', 'source': 'home', 'dest': 'vuelo'},
    {'trigger': 'avisobateria', 'source': 'vuelo', 'dest': 'bateriabaja'},
    {'trigger': 'Coordenadas_validas', 'source': 'bateriabaja', 'dest': 'Deteccion'},
    {'trigger': 'error', 'source': 'Deteccion', 'dest': 'turbulencia'},
    {'trigger': 'llegoahome', 'source': 'turbulencia', 'dest': 'navegando'},
    {'trigger': 'enviar_drone2', 'source': 'home', 'dest': 'iniciando_2vuelo'},
    {'trigger': 'sin_fallos', 'source': 'iniciando_2vuelo', 'dest': 'perfecto'},
    {'trigger': 'obstaculos', 'source': 'perfecto', 'dest': 'Deteccion'},
    {'trigger': 'esquivando', 'source': 'Deteccion', 'dest': 'ocupacion'},
    {'trigger': 'vida', 'source': 'ocupacion', 'dest': 'Signos_vitales'},
    {'trigger': 'permiso', 'source': 'Signos_vitales', 'dest': 'descarga_electrica'},
    {'trigger': 'llegarahome', 'source': 'descarga_electrica', 'dest': 'home'}
]

# Crear la máquina de estados
machine_drone = Machine(model=drone_ambulancia, states=states_drones_updated, transitions=transitions_drone, initial='home')

# Función para verificar el estado
def check_state():
    global drone_ambulancia
    while True:
        print(f"Estado actual: {drone_ambulancia.state}")
        
        if drone_ambulancia.state == "navegando":
            drone_ambulancia.navegar(coordenadas=coor_emergencia)
            drone_ambulancia.validar(ubicacion=direccion)
            
            if eventos.atendido == False and eventos.Tipo == 'bateriabaja':
                drone_ambulancia.trigger("llegoahome")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'vuelo':
                drone_ambulancia.trigger("comenzar_vuelo")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'Deteccion':
                drone_ambulancia.trigger("Coordenadas_validas")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'turbulencia':
                drone_ambulancia.trigger("error")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'navegando':
                drone_ambulancia.trigger("llegoahome")
                eventos.atendido = True
            
            # Cambio a otro dron
            if eventos.atendido == True and eventos.Tipo == 'home':
                drone_ambulancia = ActividadesDron(dron2)  # Cambiar a dron2
                drone_ambulancia.trigger("enviar_drone2", ubicacion=direccion)
                eventos.atendido = True
            
            elif eventos.atendido == True and eventos.Tipo == 'perfecto':
                drone_ambulancia.trigger("sin_fallos")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'Deteccion':
                drone_ambulancia.trigger("obstaculos")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'ocupacion':
                drone_ambulancia.trigger("esquivando")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'Signos_vitales':
                drone_ambulancia.trigger("vida")
                eventos.atendido = True
            elif eventos.atendido == True and eventos.Tipo == 'descarga_electrica':
                drone_ambulancia.trigger("permiso")
                eventos.atendido = True
            
        time.sleep(1)  # Pausa para evitar un loop sin control
