class Category:
    def __init__ (self, nom):
        self.nombre = nom
        self.ledger = []

    def deposit(self, monto, descripcion=''):
        self.ledger.append({"amount": monto, "description": descripcion})

    def withdraw(self, monto, descripcion=''):
        if self.check_funds(monto):
            self.ledger.append({"amount": monto * -1, "description": descripcion})
        return self.check_funds(monto)

    def get_balance(self):
        balance = 0

        for transaccion in self.ledger:
            balance += transaccion['amount']

        return balance

    def transfer(self, monto, categoria):
        if self.check_funds(monto):
            self.withdraw(monto, descripcion="Transfer to {}".format(categoria.nombre))
            categoria.deposit(monto, descripcion="Transfer from {}".format(self.nombre))
        return self.check_funds(monto)

    def check_funds(self, monto):
        return self.get_balance() >= monto

    def __str__(self):
        resp = self.nombre.center(30, '*') + '\n'

        for transaccion in self.ledger:
            resp += transaccion['description'][:23]
            canti = "{:.2f}".format(transaccion['amount'])  # Formateo el monto para que tenga 2 decimales
            longi = len(transaccion['description'][:23])    # Calculo el espacio que ocupa el monto
            resp += canti.rjust(30-longi, ' ') + '\n'       
        
        resp += "Total: {}".format(self.get_balance())

        return resp

def create_spend_chart(categorias):
    gastos = []
    gastos_porcentajes = []
    categorias_nombres = [c.nombre for c in categorias]
    longi = len(max(categorias_nombres, key=len))       # Longitud del nombre de la categoría más largo

    for categoria in categorias:
        gasto_por_categoria = 0
        for transaccion in categoria.ledger:
            if transaccion['amount'] < 0:
                gasto_por_categoria -= transaccion['amount']
        gastos.append(gasto_por_categoria)

    for gasto in gastos:
        porc = int(gasto / sum(gastos) * 100)   # Calculo el porcentaje de gastos por categoría
        while porc % 10 != 0: porc -= 1         # Redondeo a la decena más baja
        gastos_porcentajes.append(porc)


    resp = "Percentage spent by category\n"

    for x in range(100, -10, -10):
        col = "{}|".format(x)
        resp += col.rjust(4) + " "
        
        for p in gastos_porcentajes:
            if p >= x:
                resp += "o  "
            else:
                resp += "   "
        
        resp += "\n"

    resp += "    " + "-" * (1 + (3 * len(gastos))) + "\n"  # Eje horizontal

    # Muestro los nombres
    for x in range(longi):
        linea = "     "
        for y in range(len(categorias)):
            try:
                linea += categorias_nombres[y][x] + "  "
            except:
                linea += "   "

        resp += linea + "\n"

    return resp[:-1]    # Quito el último '\n'


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))