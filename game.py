import random

class Game:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.attempts = 0

    def guess(self, guess_number):
        self.attempts += 1
        if guess_number < self.number:
            return "Слишком маленькое число!"
        elif guess_number > self.number:
            return "Слишком большое число!"
        else:
            return f"Поздравляем! Вы угадали число {self.number} за {self.attempts} попыток."

def aza():
    game = Game()
    print("Добро пожаловать в игру угадывания числа!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    while True:
        try:
            guess_number = int(input("Введите ваше предположение: "))
            result = game.guess(guess_number)
            print(result)
            if guess_number == game.number:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

aza()
