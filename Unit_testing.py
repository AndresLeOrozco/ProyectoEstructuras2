import unittest
import tkinter.ttk
from tkinter import *

import GameView

class Unit_testing(unittest.TestCase):

    def test_validateWinner(self):
        jogo = GameView.gameScreen("Craque", "Vini", "None")
        self.buttons = [[0, 0, 0]
            , [0, 0, 0]
            , [0, 0, 0]]

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button( text="", font=('consolas', 40), width=5, height=2)
                self.buttons[row][column].grid(row=row, column=column)

        result = jogo.quien_gana(self.buttons)
        self.assertEqual(result, None)

    def test_isEmptyBoard(self):
        jogo = GameView.gameScreen("Craque", "Vini", "None")
        self.buttons = [[0, 0, 0]
            , [0, 0, 0]
            , [0, 0, 0]]

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(text="", font=('consolas', 40), width=5, height=2)
                self.buttons[row][column].grid(row=row, column=column)

        result = jogo.is_empty_board()
        self.assertEqual(result, True)