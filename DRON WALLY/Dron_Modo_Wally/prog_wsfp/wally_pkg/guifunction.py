# Import of the needed libraries and modules

from tkinter import messagebox
from stmch import *
from tkinter import *
from tkinter import ttk

# Creation of the window

window = Tk()
window.title("Wally the Recycler Robot")

# Creation of the first frame

frame_a = ttk.Frame(window)
frame_a.grid(column=0, row=0)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Creation of the test buttons for each use scenario, all of them are part of the first frame

ttk.Button(frame_a, text="Se suelta un objeto de la garra del robot", command=case1).grid(column=0, row=0)
ttk.Button(frame_a, text="Se mueve un objeto y este resulta tumbado al tratar de agarrarlo", command=case2).grid(column=1, row=0)
ttk.Button(frame_a, text="El robot no consigue llegar a la posición del objeto", command=case3).grid(column=2, row=0)
ttk.Button(frame_a, text="Se oprime el botón de parada de emergencia", command=case4).grid(column=0, row=1)
ttk.Button(frame_a, text="Se oprime el botón de continuar", command=case5).grid(column=1, row=1)
ttk.Button(frame_a, text="Se oprime el botón de start", command=case6).grid(column=2, row=1)
ttk.Button(frame_a, text="El robot llega al contenedor", command=case7).grid(column=0, row=2)
ttk.Button(frame_a, text="Se cambia la categoría del objeto a recoger", command=case8).grid(column=1, row=2)
ttk.Button(frame_a, text="La garra del robot no alcanza el objeto", command=case9).grid(column=2, row=2)
ttk.Button(frame_a, text="Ya no hay más objetos a recoger", command=case10).grid(column=0, row=3)
ttk.Button(frame_a, text="La cámara se desconectó y no hay imágenes", command=case11).grid(column=1, row=3)
ttk.Button(frame_a, text="El robot no logra recoger un objeto luego de varios minutos", command=case12).grid(column=2, row=3)
ttk.Button(frame_a, text="La AI cambia la categoria del objeto", command=case13).grid(column=1, row=4)

# Creation of the second frame

frame_b = ttk.Frame()
frame_b.grid(column=0, row=5)

# Creation of the message box and button to show the state of the robot, this one being part of the second frame

def state():
    robotstate = robot.state
    messagebox.showinfo(title="Robot's State", message = robotstate)

ttk.Button(frame_b, text="Click here to view the current state of the robot", command=state).grid(column=1, row=5)

window.mainloop()
