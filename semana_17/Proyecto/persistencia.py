import json
from pathlib import Path
from logica import Category, Transaction

BASE_DIR = Path(__file__).parent
CAT_FILE = BASE_DIR / "categories.json"
TRANSACTIONS_FILE = BASE_DIR / "transactions.json"

def save_data(finance_manager):
    categories_data = [
        {
        "name": category.name, 
        "color": category.color
        } 
        for category in finance_manager.categories
    ]

    transactions_data = [
        {
            "title": transaction.title,
            "amount": transaction.amount,
            "category": transaction.category,
            "transaction_type": transaction.transaction_type,
            "transaction_date": transaction.transaction_date
        }
        for transaction in finance_manager.transactions
    ]

    with open(CAT_FILE, "w", encoding="utf-8") as categories_file:
        json.dump(categories_data, categories_file, indent=4, ensure_ascii=False)
    
    with open(TRANSACTIONS_FILE, "w", encoding="utf-8") as transactions_file:
        json.dump(transactions_data, transactions_file, indent=4, ensure_ascii=False)


def load_data(finance_manager):
    if CAT_FILE.exists():
        with open(CAT_FILE, "r", encoding="utf-8") as categories_file:
            categories_data = json.load(categories_file)

            finance_manager.categories = [
                Category(
                    category_data["name"],
                    category_data.get("color", "FFFFFF")
                )
                for category_data in categories_data
            ]
    
    if TRANSACTIONS_FILE.exists():
        with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as transactions_file:
            transactions_data = json.load(transactions_file)

            finance_manager.transactions = [
                Transaction(
                    transaction_data["title"],
                    transaction_data["amount"],
                    transaction_data["category"],
                    transaction_data["transaction_type"],
                    transaction_data["transaction_date"]
                )
                for transaction_data in transactions_data
            ]