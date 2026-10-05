# BRAZO_ROBOTICO-
# Sistema de Control para Brazo Robótico (ESP32 + PyBullet)

## 1. Descripción

En esta actividad se desarrolló e implementó un sistema de control de telemetría en tiempo real para un brazo robótico utilizando un microcontrolador ESP32 como dispositivo de adquisición de datos y control.

La ESP32 adquiere las señales analógicas provenientes de dos potenciómetros y procesa las pulsaciones de un teclado matricial. Estos datos son transmitidos mediante comunicación serial UART (vía puerto USB/COM) hacia un script de control desarrollado en Python. El programa en Python recibe la trama de datos en tiempo real, calcula la conversión a radianes y desplazamientos en metros, y actualiza la simulación cinemática del brazo robótico dentro del entorno **PyBullet**, utilizando el modelo cargado desde el archivo `brazo.urdf`.

---

## 2. Objetivos

* Programar la ESP32 para realizar la lectura de dos potenciómetros mediante sus canales ADC.
* Configurar la lectura de un teclado matricial para la captura de eventos de apertura y cierre.
* Transmitir los datos codificados desde la ESP32 hacia la PC mediante comunicación serial UART.
* Recibir y decodificar el flujo de datos en Python a través de `pySerial`.
* Mapear y controlar las articulaciones revolutas del brazo robótico en el simulador PyBullet.
* Implementar el control directo de las articulaciones prismáticas (gripper/pinza) mediante comandos del teclado.
* Validar la sincronización, respuesta cinemática y comunicación en tiempo real entre la ESP32 y PyBullet.

---

## 3. Componentes Utilizados

### Hardware
* **ESP32 Dev Module**
* **2 Potenciómetros** de 1 kΩ (o 10 kΩ)
* **Teclado Matricial 4x4**
* Computador
* Cable de datos Micro-USB / USB-C
* Protoboard y cables de conexión (Jumpers)

### Software
* **Arduino IDE** (para compilación y carga del código C++ en la ESP32)
* **Python 3.12**
* **PyBullet** (motor de simulación física y visualización 3D)
* **PySerial** (librería para lectura del puerto COM)
* **Visual Studio Code**
* Archivo **`brazo.urdf`** (modelo cinemático y geométrico del robot)

---

## 4. Conexiones del Hardware

### Potenciómetros
* **Potenciómetro 1 (Articulación 1 - `joint_1`):**
  * Pin lateral → GND
  * Pin central → **GPIO 34** (ADC1_CH6)
  * Pin lateral → 3.3V
* **Potenciómetro 2 (Articulación 2 - `joint_2`):**
  * Pin lateral → GND
  * Pin central → **GPIO 35** (ADC1_CH7)
  * Pin lateral → 3.3V

### Teclado Matricial
Para el control del gripper se utilizaron las líneas correspondientes a la fila 1 y columnas 1 y 2:
* **Fila 1 (R1):** **GPIO 13**
* **Columna 1 (C1):** **GPIO 27**
* **Columna 2 (C2):** **GPIO 32**

**Asignación de teclas:**
* **Tecla 1:** Apertura del gripper.
* **Tecla 2:** Cierre del gripper.

---

## 5. Comunicación Serial UART

* **Puerto:** COM (Asignado dinámicamente por el sistema, e.g., `COM3`).
* **Velocidad de transmisión:** `115200 baudios`.
* **Estructura de la trama:**
  * Para posición continua de potenciómetros: `POT1,POT2` (valores enteros de ADC entre `0` y `4095`).  
    *Ejemplo:* `2048,1980`
  * Al presionar **Tecla 1**: La ESP32 envía el comando `OPEN`.
  * Al presionar **Tecla 2**: La ESP32 envía el comando `CLOSE`.

---

## 6. Arquitectura del Sistema

El flujo de información y control del sistema sigue el esquema:

`ESP32 (ADC/Teclado) → UART (USB/COM) → Python (pySerial) → PyBullet Engine → Modelo Brazo URDF`

1. La ESP32 realiza el muestreo analógico de los GPIO 34 y GPIO 35, y escanea las entradas del teclado.
2. Formatea los valores en una cadena de texto (trama UART) y los transmite a 115200 baudios.
3. El script de Python escucha el puerto serie, parsea la cadena y realiza la conversión matemática:
   * Convierte las lecturas ADC (0 - 4095) a ángulos en radianes según los límites de cada `joint`.
   * Interpreta los eventos `OPEN` / `CLOSE` para actualizar el desplazamiento lineal de las juntas prismáticas del gripper.
4. Python envía los comandos de control de posición (`p.POSITION_CONTROL`) a PyBullet para actualizar el modelo 3D.

---

## 7. Control de las Articulaciones y Mapeo URDF

El modelo `brazo.urdf` contiene 5 articulaciones en total:

| Índice | Nombre Joint | Tipo | Elemento de Control | Rango de Movimiento |
| :---: | :---: | :---: | :---: | :---: |
| **0** | `joint_1` | Revoluta (0) | Potenciómetro 1 (GPIO 34) | -2.5 rad a 2.5 rad |
| **1** | `joint_2` | Revoluta (0) | Potenciómetro 2 (GPIO 35) | -2.0 rad a 2.0 rad |
| **2** | `joint_gripper` | Prismática (1) | Tecla 1 / Tecla 2 | 0.00 m a 0.04 m |
| **3** | `joint_dedo_izq` | Prismática (1) | Tecla 1 / Tecla 2 | 0.00 m a 0.04 m |
| **4** | `joint_dedo_der` | Prismática (1) | Tecla 1 / Tecla 2 | 0.00 m a -0.04 m (Invertido) |

---

## 8. Programa en Python (`potenciometros_brazo.py`)

El script principal cumple las siguientes funciones:
* Inicializa la interfaz gráfica y entorno físico de PyBullet.
* Carga el archivo `brazo.urdf` y mapea los nombres e índices de las articulaciones.
* Desactiva los motores de velocidad por defecto (`p.VELOCITY_CONTROL`) para evitar interferencias de torque.
* Abre la conexión con la ESP32 a través de `pySerial` a 115200 baudios.
* Ejecuta un hilo (*thread*) o bucle continuo de lectura serial para recibir las tramas sin congelar el renderizado 3D.
* Transforma los datos recibidos y aplica la función `p.setJointMotorControl2()` con modo `POSITION_CONTROL` y fuerza adecuada para lograr movimientos suaves e instantáneos.

---

## 9. Instrucciones de Ejecución

1. Cargar el código en la placa ESP32 utilizando Arduino IDE.
2. Verificar en el Administrador de Dispositivos de Windows el puerto asignado (ejemplo: `COM3`).
3. **Cerrar el Monitor Serial** de Arduino IDE para liberar el puerto COM.
4. Abrir la terminal en la ruta del proyecto:
   ```bash
   cd "C:\Users\rozob\U_Militar\8) Brazo_URDF"
