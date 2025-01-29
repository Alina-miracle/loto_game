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

class Ball:
    def __init__(self):
        self.available_numbers = list(range(1, 91))  # Все возможные номера бочонков

    def draw_ball(self):
        if not self.available_numbers:
            return None
        return self.available_numbers.pop(random.randint(0, len(self.available_numbers) - 1))

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

def choose_player_type(name):
    choice = input(f"Вы хотите, чтобы {name} был человеком (y/n)? ").strip().lower()
    return True if choice == "y" else False

def start_loto_game():
    player1_name = input("Введите имя первого игрока: ")
    player1_type = choose_player_type(player1_name)
    player1 = Player(player1_name, player1_type)

    player2_name = input("Введите имя второго игрока: ")
    player2_type = choose_player_type(player2_name)
    player2 = Player(player2_name, player2_type)

    game = Game(player1, player2)
    game.start_game()

if __name__ == "__main__":
    start_loto_game()
