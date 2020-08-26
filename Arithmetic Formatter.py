import re

def valido(lista):
    if len(lista) > 5: 
        return "Error: Too many problems."

    for x in lista:
        num1 = x.split()[0]
        num2 = x.split()[2]
        signo = x.split()[1]

        if signo not in '+-':
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2)> 4:
            return"Error: Numbers cannot be more than four digits."
            

        if (re.search("^\d+", num1) is None) or (re.search("^\d+", num2) is None):
            return "Error: Numbers must only contain digits."

    return True

def arithmetic_arranger(lista, resultado=False):
    if valido(lista) is not True:
        return valido(lista)
    else:
        return 'OK'
    


print(arithmetic_arranger(["5 - 8", "9 - 3801", "9999 + 9999", "523 - 49"], True))