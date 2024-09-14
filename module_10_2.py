import threading
from time import sleep


class Knight(threading.Thread):
    enemies = 100
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            with self.lock:
                if self.enemies <= 0:
                    break
                self.enemies -= self.power
            sleep(1)
            self.days += 1
            with self.lock:
                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
