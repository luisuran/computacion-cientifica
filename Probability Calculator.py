import copy
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
    hat_copia = copy.deepcopy(hat)
    M = 0
    expected = []
    
    for k, v in expected_balls.items():
        for _ in range(v):
            expected.append(k)

    for _ in range(num_experiments):
        hat_copia.contents = copy.deepcopy(hat.contents)
        
        sorteadas = hat_copia.draw(num_balls_drawn)

        # Si encuentro una bola esperada en la lista de bolas sorteadas, la elimino de la lista de sorteadas
        for x in expected:
            if x in sorteadas:
                sorteadas.remove(x)

        # Si la cantidad de bolas en la lista sorteada coincide con la cantidad sacada menos la esperada, quiere 
        # decir que obtuve todas las bolas
        if len(sorteadas) == num_balls_drawn - len(expected): M += 1
    
    return M / num_experiments