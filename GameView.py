import tkinter
import tkinter.ttk
from tkinter import *


class firstScreen:
    def __init__(self, window):
        self.window = window
        self.window.title("Pantalla Inicial")

        self.window.geometry('600x600+0+0')
        frame1 = Frame(self.window)
        frame1.pack()
        label = Label(frame1, text="Juego del Gato", font=('consolas', 40))
        label.pack(side=TOP)
        label2 = Label(frame1, text="Seleccione un modo de juego", font=('consolas', 30))
        label2.pack(pady=50)
        button1Jugador = Button(frame1, command=self.players_window, text="Jugador vs Jugador", font=("consolas", 20, 'bold'))
        button1Jugador.pack(padx=0, pady=15)
        button2Jugador = Button(frame1, text="Jugador vs IU", font=("consolas", 20, 'bold'))
        button2Jugador.pack()



    def players_window(self):
        new_window = playerScreen()
    def ui_window(self):
        new_window = secondScreen()


class playerScreen:
    def __init__(self):
        window = Toplevel()
        window.title("Registrar Jugadores")
        window.geometry('600x600+0+0')

        labelJugador0 = Label(window, text="Registro de jugadores", font=('consolas', 40))
        labelJugador0.pack(pady=50)

        labelJugador1 = Label(window, text="Nombre del primer jugador", font=('consolas', 20))
        labelJugador1.pack(pady=10)
        textoJugador1 = tkinter.ttk.Entry(window)
        textoJugador1.pack()

        labelJugador2 = Label(window, text="Nombre del primer jugador", font=('consolas', 20))
        labelJugador2.pack(pady=5)
        textoJugador2 = tkinter.ttk.Entry(window)
        textoJugador2.pack()

        button1Jugar = Button(window, text="Jugar", command=secondScreen.game_window)
        button1Jugar.pack()

    def game_windows(self):
        pass

