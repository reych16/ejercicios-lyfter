from datetime import datetime, date

DATE_FORMAT = "%d/%m/%Y"

class Category:
    def __init__(self, name, color="#FFFFFF"):
        self.name = name.strip()
        self.color = color


class Transaction:
    def __init__(self, title, amount, category, transaction_type, transaction_date):
        self.title = title.strip()
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date


class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []
    
    def add_category(self, name, color="#FFFFFF"):
        if not name.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío.")
        
        if self.category_exists(name):
            raise ValueError("La categoría ya existe.")
        
        self.categories.append(Category(name, color))
    
    def category_exists(self, name):
        return name.strip() in [category.name for category in self.categories]
    
    def get_category_names(self):
        return [category.name for category in self.categories]
    
    def get_category_color(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                return category.color
        
        return "#FFFFFF"
    
    def add_transaction(self, title, amount, category, transaction_type, transaction_date):
        if not self.categories:
            raise ValueError("No hay categorías.")
        
        if not title.strip():
            raise ValueError("El título no puede estar vacío.")
        
        validated_amount = validate_amount(amount)

        if category not in self.get_category_names():
            raise ValueError("La categoría no existe.")
        
        if transaction_type not in ["gasto", "ingreso"]:
            raise ValueError("El tipo debe ser gasto o ingreso.")
        
        validate_date(transaction_date)

        self.transactions.append(
            Transaction(title, validated_amount, category, transaction_type, transaction_date)
        )
    
    def get_transactions_table(self, transactions=None):
        transactions_to_show = transactions if transactions is not None else self.transactions

        return [
            [
                transaction.transaction_date,
                transaction.title,
                transaction.amount,
                transaction.category,
                transaction.transaction_type
            ]
            for transaction in transactions_to_show
        ]
    
    def filter_transactions_by_date(self, start_date, end_date):
        start = convert_date(start_date)
        end = convert_date(end_date)

        if start > end:
            raise ValueError("La fecha de inicio no puede ser mayor que la fecha fin.")
        
        filtered_transactions = []

        for transaction in self.transactions:
            current_transaction_date = convert_date(transaction.transaction_date)

            if start <= current_transaction_date <= end:
                filtered_transactions.append(transaction)
        
        return filtered_transactions

    
    def calculate_totals(self, transactions=None):
        transactions_to_calculate = transactions if transactions is not None else self.transactions

        total_income = 0
        total_expenses = 0

        for transaction in transactions_to_calculate:
            if transaction.transaction_type == "ingreso":
                total_income += transaction.amount
            elif transaction.transaction_type == "gasto":
                total_expenses += transaction.amount
        
        balance = total_income - total_expenses
        return total_income, total_expenses, balance
    
    def edit_transaction(self, transaction_index, title, amount, category, transaction_type, transaction_date):
        if transaction_index < 0 or transaction_index >= len(self.transactions):
            raise ValueError("Movimiento no encontrado.")
        
        if not title.strip():
            raise ValueError("El título no puede estar vacío.")
        
        validated_amount = validate_amount(amount)

        if category not in self.get_category_names():
            raise ValueError("La categoría no existe.")
        
        if transaction_type not in ["gasto", "ingreso"]:
            raise ValueError("El tipo debe ser gasto o ingreso.")
        
        validate_date(transaction_date)

        transaction = self.transactions[transaction_index]

        transaction.title = title.strip()
        transaction.amount = validated_amount
        transaction.category = category
        transaction.transaction_type = transaction_type
        transaction.transaction_date = transaction_date

    def delete_transaction(self, transaction_index):
        if transaction_index < 0 or transaction_index >= len(self.transactions):
            raise ValueError("Movimiento no encontrado.")
        
        self.transactions.pop(transaction_index)


def validate_amount(amount):
    try:
        converted_amount = float(amount)
    except ValueError:
        raise ValueError("El monto debe ser numérico.")

    if converted_amount <= 0:
        raise ValueError("Monto inválido. Debe ser mayor a 0.")
    return converted_amount


def convert_date(date_text):
    try:
        return datetime.strptime(date_text, DATE_FORMAT).date()
    except ValueError:
        raise ValueError("La fecha debe tener el formato dd/mm/yyyy")


def validate_date(date_text):
    transaction_date = convert_date(date_text)

    if transaction_date > date.today():
        raise ValueError("La fecha no puede estar en el futuro.")
    
    return True


def get_current_date():
    return date.today().strftime(DATE_FORMAT)