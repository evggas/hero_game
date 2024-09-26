import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name}, нанося {damage} урона.")
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print(f"Игра началась! Герои {self.player.name} и {self.computer.name} вступают в бой.\n")

        while self.player.is_alive() and self.computer.is_alive():
            print(
                f"{self.player.name}: {self.player.health} здоровья, {self.computer.name}: {self.computer.health} здоровья.")
            player_action = input("Нажми Enter для атаки: ")

            if player_action == "":
                self.player.attack(self.computer)
            else:
                print("Неверная команда, попробуй снова.")
                continue

            if self.computer.is_alive():
                self.computer_turn()
            print("\n")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def computer_turn(self):
        print(f"{self.computer.name} атакует!")
        self.computer.attack(self.player)


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
