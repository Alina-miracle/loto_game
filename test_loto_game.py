import unittest
from loto_game import Player, Ball, Game  # Импортируем из loto_game

class TestGame(unittest.TestCase):
    def test_player_generate_numbers(self):
        player = Player("Игрок 1")
        self.assertEqual(len(player.numbers), 5)  # Проверяем, что у игрока 5 чисел

    def test_player_check_number(self):
        player = Player("Игрок 1")
        number = player.numbers[0]
        self.assertTrue(player.check_number(number))  # Число должно быть найдено
        self.assertFalse(player.check_number(99))  # Номер 99 не должен быть у игрока

    def test_ball_draw(self):
        ball = Ball()
        number = ball.draw_ball()
        self.assertIsNotNone(number)
        self.assertTrue(1 <= number <= 90)  # Число должно быть в пределах от 1 до 90

    def test_game_winner(self):
        player1 = Player("Игрок 1")
        player2 = Player("Игрок 2")
        game = Game(player1, player2)
        for _ in range(5):
            game.play_turn()
        self.assertFalse(game.check_winner())  # Проверяем, что пока нет победителя

if __name__ == "__main__":
    unittest.main()
