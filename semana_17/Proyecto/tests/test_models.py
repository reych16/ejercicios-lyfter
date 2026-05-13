import pytest

from Proyecto.logica import (
    FinanceManager,
    validate_amount,
    validate_date
)

def test_add_category_successfully():
    finance_manager = FinanceManager()

    finance_manager.add_category("Comida", "#FF0000")

    assert len(finance_manager.categories) == 1
    assert finance_manager.categories[0].name == "Comida"
    assert finance_manager.categories[0].color == "#FF0000"


def test_add_empty_category_raises_error():
    finance_manager = FinanceManager()

    with pytest.raises(ValueError):
        finance_manager.add_category("")


def test_add_duplicate_category_raises_error():
    finance_manager = FinanceManager()
    finance_manager.add_category("Comida")

    with pytest.raises(ValueError):
        finance_manager.add_category("Comida")


def test_add_expense_succesfully():
    finance_manager = FinanceManager()
    finance_manager.add_category("Comida")

    finance_manager.add_transaction("Pizza", 5000, "Comida", "gasto", "01/01/2026")

    assert len(finance_manager.transactions) == 1
    assert finance_manager.transactions[0].transaction_type == "gasto"


def test_add_income_succesfully():
    finance_manager = FinanceManager()
    finance_manager.add_category("Salario")

    finance_manager.add_transaction("Pago", 300000, "Salario", "ingreso", "01/01/2026")

    assert len(finance_manager.transactions) == 1
    assert finance_manager.transactions[0].transaction_type == "ingreso"


def test_add_transaction_without_categories_raises_error():
    finance_manager = FinanceManager()

    with pytest.raises(ValueError):
        finance_manager.add_transaction("Pizza", 5000, "Comida", "gasto", "01/01/2026")


def test_add_transaction_with_negative_amount_raises_error():
    finance_manager = FinanceManager()
    finance_manager.add_category("Comida")

    with pytest.raises(ValueError):
        finance_manager.add_transaction("Pizza", -5000, "Comida", "gasto", "01/01/2026")


def test_invalid_date_format_raises_error():
    with pytest.raises(ValueError):
        validate_date("2025/01/01")


def test_filter_transactions_by_date():
    finance_manager = FinanceManager()
    finance_manager.add_category("Comida")

    finance_manager.add_transaction("Pizza", 5000, "Comida", "gasto", "01/01/2026")
    finance_manager.add_transaction("Hamburguesa", 3000, "Comida", "gasto", "10/01/2026")

    result = finance_manager.filter_transactions_by_date("01/01/2026", "05/01/2026")
    
    assert len(result) == 1
    assert result[0].title == "Pizza"


def test_calculate_totals():
    finance_manager = FinanceManager()
    finance_manager.add_category("General")

    finance_manager.add_transaction("Salario", 100000, "General", "ingreso", "01/01/2026")
    finance_manager.add_transaction("Comida", 25000, "General", "gasto", "01/01/2026")

    total_income, total_expenses, balance = finance_manager.calculate_totals()

    assert total_income == 100000
    assert total_expenses == 25000
    assert balance == 75000


