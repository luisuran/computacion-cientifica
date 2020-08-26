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

def formatoNumero(longitud, cadena):
    espacios = longitud - len(cadena)
    if cadena.isnumeric():
        cadena = ' '*espacios + cadena
    else:
        espacios = longitud - len(cadena)
        cadena = cadena[0] + ' '*espacios + cadena[1:]
    return cadena

def arithmetic_arranger(lista, mostrarResultado=False):
    if valido(lista) is not True:
        return valido(lista)
    else:
        numerador = ""
        denominador = ""
        barra = ""
        resultados = ""

        for x in lista:
            longitud = max(len(x.split()[0]), len(x.split()[2])) + 2
            resultado = str(eval(x))
            
            numerador = formatoNumero(longitud, x.split()[0])
            denominador = formatoNumero(longitud, x.split()[1] + x.split()[2])
            barra = '-' * longitud
            resultados = formatoNumero(longitud, resultado)

            print(numerador + '\n' + denominador + '\n' + barra + '\n' + resultados)

            break
        
    


arithmetic_arranger(["35 - 8", "9 - 3801", "9999 + 9999", "523 - 49"], True)