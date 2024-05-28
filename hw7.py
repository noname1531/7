import random
import sqlite3
from Game import Game 

connect = sqlite3.connect("register.db")
cursor = connect.cursor()

    
cursor.execute("""
        CREATE TABLE IF NOT EXISTS register (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            phone_number INTEGER NOT NULL,
            password INTEGER NOT NULL
        )
    """)
connect.commit()

   
full_name = input("Введите Имя: ")
phone_number = int(input("Введите Номер телефона: "))
password = int(input("Введите код: "))

  
cursor.execute("INSERT INTO register (full_name, phone_number, password) VALUES (?, ?, ?)",
                   (full_name, phone_number, password))


connect.commit()

connect.close()



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

    
    db = Game()

    while True:
        try:
            guess_number = int(input("Введите ваше предположение: "))
            result = game.guess(guess_number)
            print(result)
            if guess_number == game.number:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")


    db.close()

    
    

aza()