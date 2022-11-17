from tkinter import *


class GameView:



    def __int__(self):
        self.window = Tk()
        self.window.title("Gato")
        label = Label(text="Juego del Gato", font=('consolas', 40))
        label.pack(side="top")
        label2 = Label(text="Seleccione un modo de juego", font=('consolas', 30))
        label2.pack()

        button1Jugador = Button(text="Jugador vs Jugador",font= ('consolas', 10), command=self.ShowPantallaJugvsUI())
        button1Jugador.pack()
        button2Jugador = Button(text="Jugador vs IU")
        button2Jugador.pack()
        self.window.mainloop()

    def ShowPantallaJugvsUI(self):
        print("hola")