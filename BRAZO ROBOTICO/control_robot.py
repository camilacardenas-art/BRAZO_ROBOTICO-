import os
import time
import math
import pybullet as p
import pybullet_data

# 1. Inicializar PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")

# 2. Cargar URDF del brazo
DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_URDF = os.path.join(DIR_ACTUAL, "brazo.urdf")
robot_id = p.loadURDF(RUTA_URDF, [0, 0, 0], useFixedBase=True)

# Mapear articulaciones y desactivar el freno predeterminado
num_joints = p.getNumJoints(robot_id)
joint_map = {}

print("\n=============================================", flush=True)
print("   ARTICULACIONES DETECTADAS EN BRAZO.URDF   ", flush=True)
print("=============================================", flush=True)

for i in range(num_joints):
    info = p.getJointInfo(robot_id, i)
    nombre = info[1].decode('utf-8')
    tipo = info[2]  # 0: REVOLUTE, 1: PRISMATIC, 4: FIXED
    joint_map[nombre] = i
    print(f" -> Índice {i}: '{nombre}' | Tipo: {tipo}", flush=True)
    
    # Liberar el motor de velocidad por defecto
    p.setJointMotorControl2(robot_id, i, p.VELOCITY_CONTROL, force=0)

print("=============================================\n", flush=True)

p.resetDebugVisualizerCamera(cameraDistance=2.0, cameraYaw=45, cameraPitch=-30, cameraTargetPosition=[0, 0, 0.5])

# Función directa de control de posición
def mover_joint_directo(nombre_joint, valor, es_radial=True):
    if nombre_joint in joint_map:
        idx = joint_map[nombre_joint]
        target_pos = math.radians(valor) if es_radial else valor
        
        p.setJointMotorControl2(
            bodyUniqueId=robot_id,
            jointIndex=idx,
            controlMode=p.POSITION_CONTROL,
            targetPosition=target_pos,
            force=2000,
            maxVelocity=10.0,
            positionGain=0.3
        )

# 3. Bucle de movimiento fluido continuo (60 FPS)
t = 0.0
while True:
    t += 0.03
    
    # Generar trayectoria de movimiento
    j1 = 90.0 * math.sin(t)
    j2 = 45.0 * math.cos(t * 0.8)
    gripper = 0.02 + 0.015 * math.sin(t * 1.5)

    # Aplicar a las articulaciones confirmadas del URDF
    mover_joint_directo('joint_1', j1, es_radial=True)
    mover_joint_directo('joint_2', j2, es_radial=True)
    mover_joint_directo('joint_gripper', gripper, es_radial=False)
    mover_joint_directo('joint_dedo_izq', gripper, es_radial=False)
    mover_joint_directo('joint_dedo_der', -gripper, es_radial=False)

    p.stepSimulation()
    time.sleep(1.0 / 60.0)