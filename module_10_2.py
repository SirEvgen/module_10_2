import random
from threading import Thread
import time
from colorama import Fore


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        color = [Fore.BLUE, Fore.GREEN, Fore.RED, Fore.CYAN, Fore.YELLOW]
        self.color_res = random.choice(color)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.color_res + self.name}, на нас напали!")
        k = 0
        while self.enemies > 0:
            self.enemies -= self.power
            if self.enemies < self.power:
                self.power = self.enemies
            time.sleep(1)
            k += 1
            print(f"{self.color_res + self.name} сражается {k} день, осталось {self.enemies} воинов.")
        if self.enemies == 0:
            print(f"{self.name} одержал победу спустя {k} дней!")

    def start(self):
        Thread.start(self)


first_knight = Knight('Sir Lancelot', 9)
second_knight = Knight("Sir Galahad", 7)
first_knight.start()
second_knight.start()
