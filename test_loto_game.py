import unittest
from loto_game import Player, Ball, Game

class TestLotoGame(unittest.TestCase):

    def test_player_str(self):
        player = Player("Игрок 1")
        self.assertEqual(str(player), f"Игрок Игрок 1, компьютер: False, оставшиеся числа: {player.numbers}")

    def test_ball_str(self):
        ball = Ball()
        self.assertEqual(str(ball), "Осталось 90 бочонков")

    def test_game_str(self):
        player1 = Player("Игрок 1")
        player2 = Player("Игрок 2")
        game = Game(player1, player2)
        self.assertTrue(str(game).startswith("Игра между Игрок 1 и Игрок 2"))

    def test_player_equality(self):
        player1 = Player("Игрок 1")
        player2 = Player("Игрок 1")
        self.assertTrue(player1 == player2)
        self.assertFalse(player1 != player2)

    def test_ball_equality(self):
        ball1 = Ball()
        ball2 = Ball()
        self.assertTrue(ball1 == ball2)
        ball1.draw_ball()
        self.assertFalse(ball1 == ball2)

    def test_game_equality(self):
        player1 = Player("Игрок 1")
        player2 = Player("Игрок 2")
        game1 = Game(player1, player2)
        game2 = Game(player1, player2)
        self.assertTrue(game1 == game2)
        game1.play_turn()
        self.assertFalse(game1 == game2)

if __name__ == "__main__":
    unittest.main()
