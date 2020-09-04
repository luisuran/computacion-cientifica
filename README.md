## Proyectos de computación científica con python


### 1 - Arithmetic Formatter
Crear una función que reciba una lista de problemas aritméticos y devuelva los problemas ordenados verticalmente y uno al lado del otro. La función debería tener opcionalmente un segundo argumento. Cuando el segundo argumento se establece en Verdadero, se deben mostrar las respuestas.

### 2 - Time Calculator
Se pide escribir una función llamada add_time que tome dos parámetros obligatorios y un parámetro opcional:
<ul>
  <li>Una hora de inicio en formato de reloj de 12 horas (que termina en AM o PM)</li>
  <li>Un tiempo de duración indicado en horas y minutos</li>
  <li>Un día de inicio de la semana (opcional). No distingue entre mayúsculas y minúsculas
</ul>
La función debe agregar el tiempo de duración a la hora de inicio y devolver el resultado.<br>
Si el resultado será el día siguiente, debería mostrarse (día siguiente) después de la hora. Si el resultado será más de un día después, debería mostrarse (n días después) después de la hora, donde "n" es el número de días después.<br>
Si a la función se le da el parámetro opcional de día de inicio de la semana, la salida debe mostrar el día de la semana del resultado. El día de la semana en la salida debe aparecer después de la hora y antes del número de días después.<br>
No importe ninguna librería de Python. Suponga que las horas de inicio son horas válidas. Los minutos del tiempo de duración serán un número entero menor que 60, pero la hora puede ser cualquier número entero.

### 3 - Budget App
Implementar la clase Category. Debería poder crear instancias de objetos en función de diferentes categorías de presupuesto, como comida, ropa y entretenimiento. Cuando se crean objetos, se pasan con el nombre de la categoría. La clase debe tener una variable de instancia llamada ledger que sea una lista. La clase también debe contener los siguientes métodos:
<ul>
  <li>Un método deposit que acepta una cantidad y una descripción. Si no se proporciona una descripción, debería ser una cadena vacía por defecto. El método debe agregar un objeto a la lista ledger en forma de {"amount": monto, "description": descripción}.</li>
  <li>Un método withdraw que es similar al método deposit, pero la cantidad transferida debe almacenarse en ledger como un número negativo. Si no hay fondos suficientes, no se debe agregar nada a ledger. Este método debe devolver True si se realizó el retiro y False en caso contrario.</li>
  <li>Un método get_balance que devuelve el saldo actual de la categoría de presupuesto en función de los depósitos y retiros que se han producido.</li>
  <li>Un método transferencia que acepta una cantidad y otra categoría presupuestaria como argumentos. El método debe agregar un retiro con el monto y la descripción "Transfer to [Categoría de presupuesto de destino]". Luego, el método debe agregar un depósito a la otra categoría de presupuesto con el monto y la descripción "Transfer from [Categoría de presupuesto de origen]". Si no hay fondos suficientes, no se debe agregar nada a ninguno de los ledgers. Este método debería devolver True si se realizó la transferencia y False en caso contrario.</li>
  <li>Un método check_funds que acepta una cantidad como argumento. Devuelve False si la cantidad es menor que el saldo de la categoría de presupuesto y devuelve True en caso contrario. Este método debe utilizarse tanto por el método withdraw como por el método transfer.</ul>
</ul>
Cuando el objeto budget se imprime debe mostar:
<ul>
  <li>Una línea de título de 30 caracteres donde el nombre de la categoría se centra en una línea de *.</li>
  <li>Una lista de los elementos del ledger. Cada línea debe mostrar la descripción y el monto. Deben mostrarse los primeros 23 caracteres de la descripción, luego la cantidad. La cantidad debe estar alineada a la derecha, contener dos lugares decimales y mostrar un máximo de 7 caracteres.</li>
  <li>Una línea que muestra el total de la categoría.</li>
</ul>
Además de la clase Category, crear una función (fuera de la clase) llamada create_spend_chart que tome una lista de categorías como argumento. Debería devolver una cadena que sea un gráfico de barras.<br>
El gráfico debe mostrar el porcentaje gastado en cada categoría pasada como parámetro a la función. El porcentaje gastado debe calcularse solo con retiros y no con depósitos. Abajo, en el lado izquierdo del gráfico, deben aparecer las etiquetas 0 - 100. Las "barras" en el gráfico de barras deben estar formadas por el carácter "o". La altura de cada barra debe redondearse hacia abajo al 10 más cercano. La línea horizontal debajo de las barras debe ir dos espacios más allá de la barra final. Cada nombre de categoría debe estar literalmente debajo de la barra. Debe haber un título en la parte superior que diga "Porcentaje gastado por categoría".

### 4 - Polygon Area Calculator
Crear una clase Rectangle y una clase Square. La clase Square debe ser una subclase de Rectangle y heredar métodos y atributos.
#### Clase Rectangle
Cuando se crea un objeto Rectangle, debe inicializarse con los atributos width (ancho) y (height) alto. La clase también debe contener los siguientes métodos:
<ul>
  <li>set_width</li>
  <li>set_height</li>
  <li>get_area: Devuelve el área del rectángulo</li>
  <li>get_perimeter: Devuelve el perímetro del rectángulo</li>
  <li>get_diagonal: Devuelve el largo de la diagonal</li>
  <li>get_picture: Devuelve una cadena que representa la forma usando líneas de "*". El número de líneas debe ser igual a la altura y el número de "*" en cada línea debe ser igual al ancho. Debe haber una nueva línea (\ n) al final de cada línea. Si el ancho o alto es mayor que 50, esto debería devolver la cadena: "Too big for picture".</li>
  <li>get_amount_inside: Toma otra forma (cuadrado o rectángulo) como argumento. Devuelve el número de veces que la forma pasada podría caber dentro de la forma (sin rotaciones).</li>
</ul>
Además, si una instancia de un rectángulo se representa como una cadena, debería verse así: Rectangle (width = 5, height = 10)
#### Square Rectangle
La clase Square debería ser una subclase de Rectangle. Cuando se crea un objeto Square, se pasa la longitud de un lado. El método __init__ debe almacenar la longitud del lado en los atributos de ancho y alto de la clase Rectangle.
La clase Square debería poder acceder a los métodos de la clase Rectangle pero también debería contener un método set_side. Si una instancia de un cuadrado se representa como una cadena, debería verse así: Square(side=9).
Además, los métodos set_width y set_height en la clase Square deben establecer tanto el ancho como el alto.

### 5 - Probability Calculator
Escribir un programa para determinar la probabilidad aproximada de sacar ciertas bolas al azar de un sombrero.
Primero, cree una clase Hat. La clase debe tomar un número variable de argumentos que especifiquen el número de bolas de cada color que hay en el sombrero.
Siempre se creará un sombrero con al menos una bola. Los argumentos que se pasan al objeto hat al crearse deben convertirse en una variable de instancia contents. Contents debe ser una lista de cadenas que contengan un elemento por cada bola del sombrero. Cada elemento de la lista debe tener un nombre de color que represente una sola bola de ese color. Por ejemplo, si su sombrero es {"rojo": 2, "azul": 1}, el contenido debe ser ["rojo", "rojo", "azul"].

La clase Sombrero debe tener un método draw que acepte un argumento que indique el número de bolas que se sacarán del sombrero. Este método debería eliminar bolas al azar del contenido y devolver esas bolas como una lista de cadenas. Las bolas no deben volver al sombrero durante el sorteo, similar a un experimento de urna sin reposición. Si el número de bolas a sacar supera la cantidad disponible, devuelva todas las bolas.

A continuación, cree la función experiment (fuera de la clase Hat). Esta función debe aceptar los siguientes argumentos:
<ul>
  <li>hat: Un objeto hat que contiene bolas que se deben copiar dentro de la función.</li>
  <li>expected_balls: Un objeto que indica el grupo exacto de bolas que se intentará sacar del sombrero para el experimento.</li>
  <li>num_balls_drawn: La cantidad de bolas que se sacarán del sombrero en cada experimento.</li>
  <li>num_experiments: El número de experimentos a realizar. (Cuantos más experimentos se realicen, más precisa será la probabilidad aproximada).</li>
</ul>
La función del experimento debería devolver una probabilidad.

Por ejemplo, digamos que desea determinar la probabilidad de obtener al menos 2 bolas rojas y 1 bola verde cuando saca 5 bolas de un sombrero que contiene 6 negras, 4 rojas y 3 verdes. Para hacer esto, realizamos N experimentos, contamos cuántas veces M obtenemos al menos 2 bolas rojas y 1 bola verde, y estimamos la probabilidad como M / N. Cada experimento consiste en comenzar con un sombrero que contiene las bolas especificadas, sacar varias bolas y verificar si obtuvimos las bolas que estábamos intentando sacar.

Dado que esto se basa en sorteos aleatorios, la probabilidad será ligeramente diferente cada vez que se ejecute el código.
