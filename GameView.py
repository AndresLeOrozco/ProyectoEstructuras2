import tkinter
import tkinter.ttk
import unittest
from tkinter import *
import random
import time


class firstScreen:
    def __init__(self, window):
        self.window = window #Se crea la primera pantalla donde recibe la ventana main
        self.window.title("Pantalla Inicial")

        self.window.geometry('600x600+0+0')
        frame1 = Frame(self.window) #se le agrega el frame que va a contener los componentes de la pantalla inicial
        frame1.pack()
        label = Label(frame1, text="Juego del Gato", font=('consolas', 40)) #label titulo
        label.pack(side=TOP)
        label2 = Label(frame1, text="Seleccione un modo de juego", font=('consolas', 30))
        label2.pack(pady=50)
        button1Jugador = Button(frame1, command=self.players_window, text="Jugador vs Jugador",#boton para acceder al modo de juego jug vs jug
                                font=("consolas", 20, 'bold'))
        button1Jugador.pack(pady=5)
        button2Jugador = Button(frame1, command=self.ui_window, text="Jugador vs IU", font=("consolas", 20, 'bold'))#boton para acceder al modo de juego jug vs UI
        button2Jugador.pack(pady=50)
        buttonSalir = Button(frame1, text="Salir", font=("consolas", 20, 'bold'), command=lambda: self.window.destroy())
        buttonSalir.pack()

    def players_window(self):
        nextScreen = playerScreen()

    def ui_window(self):
        otherScreen = uiScreen()


class uiScreen():
    def __init__(self):
        window = Toplevel() #toma la window principal para cambiarle el frame y ponerle el frame del modo de juego UI
        window.title("Registrar Jugador")
        window.geometry('600x600+0+0')

        labelJugador0 = Label(window, text="Registro del jugador", font=('consolas', 40))
        labelJugador0.pack(pady=50)

        labelJugador1 = Label(window, text="Nombre del jugador", font=('consolas', 20))
        labelJugador1.pack(pady=10)
        textoJugador1 = tkinter.ttk.Entry(window)
        textoJugador1.pack()

        labeltext = Label(window, text="Seleccione la dificultad que desea Jugar", font=('consolas', 20))
        labeltext.pack(pady=10)
        #Botones de dificultad contra la maquina
        button1Jugar = Button(window, text="Facil", font=('consolas', 20),
                              command=lambda: self.game_windows(textoJugador1.get(), "CPU", "easy"))
        button1Jugar.pack(pady=20)
        button2Jugar = Button(window, text="Media", font=('consolas', 20),
                              command=lambda: self.game_windows(textoJugador1.get(), "CPU", "medium"))
        button2Jugar.pack(pady=20)
        button3Jugar = Button(window, text="Dificil", font=('consolas', 20),
                              command=lambda: self.game_windows(textoJugador1.get(), "CPU", "hard"))
        button3Jugar.pack(pady=20)

    def game_windows(self, jugador1, jugador2, gamemode):
        games = gameScreen(jugador1, jugador2, gamemode)


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

        labelJugador2 = Label(window, text="Nombre del segundo jugador", font=('consolas', 20))
        labelJugador2.pack(pady=10)
        textoJugador2 = tkinter.ttk.Entry(window)
        textoJugador2.pack()

        button1Jugar = Button(window, text="Jugar", font=('consolas', 20),
                              command=lambda: self.game_windows(textoJugador1.get(), textoJugador2.get()))
        button1Jugar.pack(pady=50)

    def game_windows(self, jugador1, jugador2):
        games = gameScreen(jugador1, jugador2, 'none')


class gameScreen:
    def __init__(self, jugador1, jugador2, bandera):
        self.finish = False
        self.modoJuego = bandera
        window = Toplevel()
        window.title("Juego GATO")

        self.jugadores = [jugador1, jugador2]
        self.movimientos = ["X", "O"]

        self.jugador = random.choice(self.jugadores)

        self.buttons = [[0, 0, 0]
            , [0, 0, 0]
            , [0, 0, 0]]

        self.label = Label(window, text="Turno de: " + self.jugador, font=('consolas', 40))
        self.label.pack(side="top")

        reset_button = Button(window, text="Reiniciar", font=('consolas', 20), command=lambda: self.restartButtoms())
        reset_button.pack(side="top")

        frame = Frame(window)
        frame.pack()

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                                   command=lambda row=row, column=column: self.nextTurn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

        if self.jugador == "CPU" and self.modoJuego == "easy":
            self.easyGame()
        if self.jugador == "CPU" and self.modoJuego == "hard":
            self.HardGame()

    def easyGame(self):
        if self.jugador == "CPU":
            for row in range(3):
                for column in range(3):
                    if self.buttons[row][column]['text'] == "":
                        self.nextTurn(row, column)
                        return
        return

    def mediumGame(self):
        while self.jugador == "CPU":
            row = random.choice([0, 1, 2])
            column = random.choice([0, 1, 2])
            self.nextTurn(row, column)

    def HardGame(self):
        if self.jugador == "CPU":
            if self.is_empty_board() is True:
                row = 1
                column = 1
                self.nextTurn(row,column)
            elif self.cantidad_jugadas() == 1:
                row = random.choice([0, 1, 2])
                column = random.choice([0, 1, 2])
                self.nextTurn(row, column)
            else:
                MejorPuntuacion = float('-inf')
                MejorMovimiento = None
                for row in range(3):
                    for column in range(3):
                        if self.buttons[row][column]['text'] == "":
                            self.buttons[row][column]['text'] = self.movimientos[1]
                            Puntuacion = self.arbol_decision(self.buttons,0,False)
                            self.buttons[row][column]['text'] = ""
                            if Puntuacion > MejorPuntuacion:
                                MejorPuntuacion = Puntuacion
                                MejorMovimiento = [row,column]

                rows = MejorMovimiento[0]
                columns = MejorMovimiento[1]
                self.nextTurn(rows,columns)


    def arbol_decision(self, botones,cantJugadas,bandera):
        resultado = self.quien_gana(botones)
        if resultado != None:
            if resultado == self.movimientos[0]:
                return -1
            if resultado == self.movimientos[1]:
                return 1
            if resultado == "Empate":
                return 0

        if bandera is True:
            MejorPuntuacion = float('-inf')
            for row in range(3):
                for column in range(3):
                    if botones[row][column]['text'] == "":
                        botones[row][column]['text'] = self.movimientos[1]
                        Puntuacion = self.arbol_decision(botones,cantJugadas+1, False)
                        botones[row][column]['text'] = ""
                        MejorPuntuacion = max(Puntuacion,MejorPuntuacion)
            return MejorPuntuacion
        else:
            MejorPuntuacion = float('inf')
            for row in range(3):
                for column in range(3):
                    if botones[row][column]['text'] == "":
                        botones[row][column]['text'] = self.movimientos[0]
                        Puntuacion = self.arbol_decision(botones, cantJugadas+1, True)
                        botones[row][column]['text'] = ""
                        MejorPuntuacion = min(Puntuacion, MejorPuntuacion)
            return MejorPuntuacion

    def quien_gana(self,botones):

        for row in range(3):
            if botones[row][0]['text'] == botones[row][1]['text'] == botones[row][2]['text'] != "":
                return botones[row][0]['text']

        for column in range(3):
            if botones[0][column]['text'] == botones[1][column]['text'] \
                    == botones[2][column]['text'] != "":
                return botones[0][column]['text']

        if botones[0][0]['text'] == botones[1][1]['text'] == botones[2][2]['text'] != "":
            return botones[0][0]['text']
        elif botones[0][2]['text'] == botones[1][1]['text'] == botones[2][0]['text'] != "":
            return botones[0][2]['text']
        elif self.EspVacios(botones) is False:
            return "Empate"
        else:
            return None

    def EspVacios(self,Botones):
        for row in range(3):
            for col in range(3):
                if Botones[row][col]['text'] == "":
                    return True

        return False

    def is_empty_board(self):
        for row in range(3):
            for column in range (3):
                if self.buttons[row][column]['text'] != "":
                    return False
        return True

    def gameType(self):
        if self.modoJuego == "easy":
            self.easyGame()
        elif self.modoJuego == "medium":
            self.mediumGame()
        elif self.modoJuego == "hard":
            self.HardGame()
        else:
            return

    def nextTurn(self, row, column):

        if self.buttons[row][column]['text'] == "" and self.validate_winner() is False:

            if self.jugador == self.jugadores[0]:
                self.buttons[row][column]['text'] = self.movimientos[0]

                if self.validate_winner() is False:
                    self.jugador = self.jugadores[1]
                    self.label.config(text=("Turno de: " + self.jugador))
                    self.gameType()

                elif self.validate_winner() is True:
                    self.label.config(text=(self.jugador + " es le ganadore"))
                    self.jugador = self.jugadores[1]

                elif self.validate_winner() == "Empate":
                    self.label.config(text=("EMPATADO"))

            else:
                self.buttons[row][column]['text'] = self.movimientos[1]

                if self.validate_winner() is False:
                    self.jugador = self.jugadores[0]
                    self.label.config(text=("Turno de: " + self.jugador))
                    self.gameType()


                elif self.validate_winner() is True:
                    self.label.config(text=(self.jugador + " es le ganadore"))
                    self.jugador = self.jugadores[0]

                elif self.validate_winner() == "Empate":
                    self.label.config(text=("EMPATADO"))


    def validate_winner(self):

        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return True

        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] \
                    == self.buttons[2][column]['text'] != "":
                return True

        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        elif self.espacios_vacios() is False:
            return "Empate"
        else:
            return False

    def espacios_vacios(self):

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == "":
                    return True

        return False

    def restartButtoms(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ""
                if self.jugador == self.jugadores[0] == "CPU":
                    self.jugador = self.jugadores[1]
                self.label.config(text="Turno de: " + self.jugador)

    def cantidad_jugadas(self):
        cont = 0
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == self.movimientos[0]:
                    cont = cont+1

        return cont

