import random

class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.numbers = self.generate_numbers()  # Генерация случайных чисел для игрока

    def generate_numbers(self):
        return random.sample(range(1, 91), 5)  # Сгенерировать 5 случайных чисел от 1 до 90

    def check_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)  # Удалить число, если оно есть
            return True
        return False

    def has_won(self):
        return len(self.numbers) == 0  # Победа, если все числа выбраны

    def __str__(self):
        return f"Игрок {self.name}, компьютер: {self.is_computer}, оставшиеся числа: {self.numbers}"

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name
        return False


class Ball:
    def __init__(self):
        self.available_numbers = list(range(1, 91))  # Все возможные номера бочонков

    def draw_ball(self):
        if not self.available_numbers:
            return None
        return self.available_numbers.pop(random.randint(0, len(self.available_numbers) - 1))

    def __str__(self):
        return f"Осталось {len(self.available_numbers)} бочонков"

    def __eq__(self, other):
        if isinstance(other, Ball):
            return self.available_numbers == other.available_numbers
        return False


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.ball = Ball()
        self.turn = 1

    def play_turn(self):
        current_player = self.player1 if self.turn % 2 == 1 else self.player2
        ball_number = self.ball.draw_ball()

        if ball_number is None:
            print("Бочонки закончились!")
            return False  # Игра окончена, если бочонки закончились

        print(f"Вытащен бочонок: {ball_number}")
        if current_player.check_number(ball_number):
            print(f"{current_player.name} зачеркнул число {ball_number}.")
        else:
            print(f"{current_player.name} не имеет числа {ball_number}.")

        self.turn += 1
        return True

    def check_winner(self):
        if self.player1.has_won():
            print(f"{self.player1.name} выиграл!")
            return True
        elif self.player2.has_won():
            print(f"{self.player2.name} выиграл!")
            return True
        return False

    def start_game(self):
        print("Игра началась!")
        while True:
            if not self.play_turn():
                break
            if self.check_winner():
                break

    def __str__(self):
        return f"Игра между {self.player1.name} и {self.player2.name}, очередь игрока: {self.turn}"

    def __eq__(self, other):
        if isinstance(other, Game):
            return self.player1 == other.player1 and self.player2 == other.player2 and self.turn == other.turn
        return False
