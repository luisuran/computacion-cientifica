import random

class Hat:
    contents = []

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num):
        bolas_sacadas = []

        for _ in range(num):
            num_bola = random.randint(0, len(self.contents) - 1)
            bolas_sacadas.append(self.contents.pop(num_bola))

        return bolas_sacadas

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass