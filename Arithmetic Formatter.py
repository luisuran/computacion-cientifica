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
            

        if num1.isdigit() and num2.isdigit():
            pass
        else:
            return "Error: Numbers must only contain digits."

    return True

def formatoNumero(longitud, cadena, esResultado=False):
    espacios = longitud - len(cadena)
    if cadena.isnumeric() or esResultado:
        cadena = ' '*espacios + cadena
    else:
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
            num1 = x.split()[0]
            num2 = x.split()[2]
            signo = x.split()[1]
            longitud = max(len(num1), len(num2)) + 2
            resultado = str(eval(x))
            
            numerador += formatoNumero(longitud, num1) + "    "
            denominador += formatoNumero(longitud, signo + num2) + "    "
            barra += '-' * longitud + "    "
            resultados += formatoNumero(longitud, resultado, True) + "    "

        if mostrarResultado:
            return (numerador.rstrip() + '\n' + denominador.rstrip() + '\n' + barra.rstrip() + '\n' + resultados.rstrip())
        else:
            return (numerador.rstrip() + '\n' + denominador.rstrip() + '\n' + barra.rstrip())
    


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))

