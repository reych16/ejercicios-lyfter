class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        print(f"\nCuenta creada con un balance de: {self.balance}")
    
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito exitoso. Nuevo balance de: {self.balance}")
        else:
            print("El monto debe ser mayor a 0.")


    def withdraw_money(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Retiro exitoso. Nuevo balance de: {self.balance}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor a 0.")

account = BankAccount(100)
account.deposit_money(50)
account.withdraw_money(80)
account.withdraw_money(220)

class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw_money(self, amount):
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                print(f"Retiro exitoso. Nuevo balance de: {self.balance}")
            else:
                print("Error: no se puede retirar, rompe el saldo mínimo.")
        else:
            print("El monto debe ser mayor a 0.")

saving = SavingsAccount(200, 100)
saving.withdraw_money(50)
saving.withdraw_money(150)
saving.deposit_money(80)
