class Category:
    nombre = ''
    ledger = []

    def __init__ (self, nom):
        self.nombre = nom

    def deposit(self, monto, descripcion=''):
        self.ledger.append({"amount": monto, "description": descripcion})

    def withdraw(self, monto, descripcion=''):
        if self.check_funds(monto):
            self.ledger.append({"amount": monto * -1, "description": descripcion})
        return self.check_funds()

    def get_balance(self):
        balance = 0

        for transaccion in self.ledger:
            balance += transaccion['amount']

        return balance

    def transfer(self, monto, categoria):
        pass

    def check_funds(self, monto):
        return monto > self.get_balance()