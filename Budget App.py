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

    print(gastos)
    print(gastos_porcentajes)