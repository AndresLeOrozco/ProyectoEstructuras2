import unittest
import GameView

class Unit_testing(unittest.TestCase):

    def test_validateWinner(self):
        juego = GameView.gameScreen
        bot = juego.getBotones()
