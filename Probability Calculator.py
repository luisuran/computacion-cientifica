import copy
import random

class Hat:
    def __init__(self, **kwargs):
        contents = []
        for k, v in kwargs.items():
            for n in range(v):
                contents.append(k)
        self.contents = contents

    def draw(self, num):
        bolas_sacadas = []

        for _ in range(num):
            try:
                num_bola = random.randint(0, len(self.contents) - 1)
                bolas_sacadas.append(self.contents.pop(num_bola))
            except:
                break

        return bolas_sacadas

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_copia = Hat()
    M = 0

    esperadas = []                      # Guardo las bolas que espero sacar en forma de arreglo unidimensional
    for k, v in expected_balls.items():
        for _ in range(v):
            esperadas.append(k)
    
    for _ in range(num_experiments):
        hat_copia.contents = copy.copy(hat.contents)
        sacadas = hat_copia.draw(num_balls_drawn)       # Arreglo con bolas sacadas en éste experimento
        
        for x in esperadas:
            if x in sacadas: sacadas.remove(x)

        if len(sacadas) == min(len(hat.contents), num_balls_drawn) - len(esperadas): M += 1

    return M / num_experiments


hat = Hat(blue=4, red=2, green=6)
probability = experiment(hat=hat, expected_balls={"blue": 2, "red": 1}, num_balls_drawn=4, num_experiments=3000)
print("Probabilidad:", probability)