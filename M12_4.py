import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        try:
            self.distance += self.speed * 2
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для Runner')

    def walk(self):
        try:
            self.distance += self.speed
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", encoding="utf-8", filename="runner_tests.log",
                        format='%(asctime)s | %(levelname)s | %(message)s')

first = Runner('Вася', -5)
second = Runner('10', 5)
third = Runner('Арсен', 10)

a = first.run()
b = second.walk()
