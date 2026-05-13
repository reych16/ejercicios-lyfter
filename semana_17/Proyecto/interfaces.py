import FreeSimpleGUI as sg
import csv
from pathlib import Path
from logica import FinanceManager, get_current_date
from persistencia import load_data, save_data

def run_app():
    finance_manager = FinanceManager()
    load_data(finance_manager)

    displayed_transactions = finance_manager.transactions

    main_window = create_main_window(finance_manager.get_transactions_table())
    update_table(main_window, finance_manager, displayed_transactions)

    while True:
        event, values = main_window.read()

        if event in (None, "Salir"):
            break

        if event == "Agregar categoría":
            handle_category(finance_manager)
            update_table(main_window, finance_manager)
        
        elif event == "Agregar gasto":
            handle_transaction(finance_manager, "gasto")
            update_table(main_window, finance_manager)

        elif event == "Agregar ingreso":
            handle_transaction(finance_manager, "ingreso")
            update_table(main_window, finance_manager)
        
        elif event == "Editar seleccionado":
            selected_index = get_selected_transaction_index(values)

            if selected_index is not None:
                transaction = displayed_transactions[selected_index]
                real_index = finance_manager.transactions.index(transaction)

                handle_edit_transaction(finance_manager, real_index, transaction)

                displayed_transactions = finance_manager.transactions
                update_table(main_window, finance_manager, displayed_transactions)
        
        elif event == "Eliminar seleccionado":
            selected_index = get_selected_transaction_index(values)

            if selected_index is not None:
                transaction = displayed_transactions[selected_index]
                real_index = finance_manager.transactions.index(transaction)

                confirmation = sg.popup_yes_no("¿Seguro que deseas eliminar este movimiento?")

                if confirmation == "Yes":
                    finance_manager.delete_transaction(real_index)
                    save_data(finance_manager)

                    displayed_transactions = finance_manager.transactions
                    update_table(main_window, finance_manager, displayed_transactions)
        
        elif event == "Filtrar":
            try:
                displayed_transactions = finance_manager.filter_transactions_by_date(
                    values["-START-DATE-"],
                    values["-END-DATE-"]
                )
                update_table(main_window, finance_manager, displayed_transactions)
            except ValueError as error:
                show_error(str(error))
        
        elif event == "Limpiar filtro":
            main_window["-START-DATE-"].update("")
            main_window["-END-DATE-"].update("")
            displayed_transactions = finance_manager.transactions
            update_table(main_window, finance_manager, displayed_transactions)

        elif event == "Exportar a CSV":
            export_to_csv(finance_manager)

    save_data(finance_manager)
    main_window.close()


def create_main_window(transactions):
    layout = [
        [sg.Text("Gestor de Finanzas Personales", font=("Arial", 18))],

        [
            sg.Text("Fecha inicio"),
            sg.Input(key="-START-DATE-", size=(12, 1)),
            sg.Text("Fecha fin"),
            sg.Input(key="-END-DATE-", size=(12, 1)),
            sg.Button("Filtrar"),
            sg.Button("Limpiar filtro")
        ],

        [
            sg.Table(
                values=transactions,
                headings=["Fecha", "Título", "Monto", "Categoría", "Tipo"],
                key="-TABLE-",
                auto_size_columns=True,
                justification="center",
                num_rows=12,
                row_colors=[],
                enable_events=True
            )
        ],

        [
            sg.Text("Ingresos:"),
            sg.Text("0", key="-TOTAL-INCOME-", size=(10, 1)),
            sg.Text("Gastos:"),
            sg.Text("0", key="-TOTAL-EXPENSE-", size=(10, 1)),
            sg.Text("Balance:"),
            sg.Text("0", key="-BALANCE-", size=(10, 1))
        ],

        [
            sg.Button("Agregar categoría"),
            sg.Button("Agregar gasto"),
            sg.Button("Agregar ingreso"),
            sg.Button("Editar seleccionado"),
            sg.Button("Eliminar seleccionado"),
            sg.Button("Exportar a CSV"),
            sg.Button("Salir")
        ]
    ]
    return sg.Window("Finanzas Personales", layout, finalize=True)


def get_selected_transaction_index(values):
    selected_rows = values["-TABLE-"]

    if not selected_rows:
        show_error("Debe seleccionar un movimiento en la tabla.")
        return None
    return selected_rows[0]


def handle_category(finance_manager):
    category_window = create_category_window()

    while True:
        event, values = category_window.read()

        if event in (None, "Cancelar"):
            break

        if event == "Guardar":
            try:
                category_name = values["-CATEGORY-NAME-"]
                category_color = values["-CATEGORY-COLOR-"] or "#FFFFFF"

                finance_manager.add_category(category_name, category_color)
                save_data(finance_manager)
                show_message("Categoría agregada correctamente")
                break

            except ValueError as error:
                show_error(str(error))

    category_window.close()


def create_category_window():
    layout = [
        [sg.Text("Nombre de la categoría")],
        [sg.Input(key="-CATEGORY-NAME-")],

        [sg.Text("Color de la categoría")],
        [
            sg.Input("#FFFFFF", key="-CATEGORY-COLOR-", size=(12, 1)),
            sg.ColorChooserButton("Seleccionar color", target="-CATEGORY-COLOR-")
        ],

        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]

    return sg.Window("Agregar categoría", layout, modal=True)


def handle_transaction(finance_manager, transaction_type):
    if not finance_manager.categories:
        show_error("No puede agregar movimientos sin categorías disponibles")
        return

    category_names = finance_manager.get_category_names()

    transaction_window = create_transaction_window(
        transaction_type,
        category_names,
        get_current_date()
    )

    while True:
        event, values = transaction_window.read()

        if event in (None, "Cancelar"):
            break

        if event == "Guardar":
            try:
                title = values["-TITLE-"]
                amount = values["-AMOUNT-"]
                category = values["-CATEGORY-"]
                transaction_date = values["-DATE-"]

                finance_manager.add_transaction(
                    title,
                    amount,
                    category,
                    transaction_type,
                    transaction_date
                )

                save_data(finance_manager)
                show_message(f"{transaction_type.capitalize()} agregado correctamente")
                break

            except ValueError as error:
                show_error(str(error))

    transaction_window.close()


def handle_edit_transaction(finance_manager, transaction_index, transaction):
    category_names = finance_manager.get_category_names()

    transaction_window = create_transaction_window(
        transaction.transaction_type,
        category_names,
        transaction.transaction_date,
        transaction
    )

    while True:
        event, values = transaction_window.read()

        if event in (None, "Cancelar"):
            break

        if event == "Guardar":
            try:
                finance_manager.edit_transaction(
                    transaction_index,
                    values["-TITLE-"],
                    values["-AMOUNT-"],
                    values["-CATEGORY-"],
                    transaction.transaction_type,
                    values["-DATE-"]
                )

                save_data(finance_manager)
                show_message("Movimiento editado correctamente.")
                break

            except ValueError as error:
                show_error(str(error))

    transaction_window.close()


def create_transaction_window(transaction_type, category_names, current_date, transaction=None):
    title_value = transaction.title if transaction else ""
    amount_value = transaction.amount if transaction else ""
    category_value = transaction.category if transaction else ""
    date_value = transaction.transaction_date if transaction else ""

    layout = [
        [sg.Text(f"Agregar/Editar {transaction_type}")],

        [sg.Text("Título")],
        [sg.Input(title_value, key="-TITLE-")],

        [sg.Text("Monto")],
        [sg.Input(amount_value, key="-AMOUNT-")],

        [sg.Text("Categoría")],
        [sg.Combo(category_names, default_value=category_value, key="-CATEGORY-", readonly=True)],

        [sg.Text("Fecha (dd/mm/yyyy)")],
        [sg.Input(date_value, key="-DATE-")],

        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]

    return sg.Window(f"Agregar/Editar {transaction_type}", layout, modal=True)


def update_table(main_window, finance_manager, transactions=None):
    transactions_to_show = (
        transactions if transactions is not None else finance_manager.transactions
    )

    table_data = finance_manager.get_transactions_table(transactions_to_show)
    row_colors = get_row_colors(finance_manager, transactions_to_show)

    main_window["-TABLE-"].update(values=table_data, row_colors=row_colors)

    total_income, total_expenses, balance = finance_manager.calculate_totals(
        transactions_to_show
    )

    main_window["-TOTAL-INCOME-"].update(f"{total_income:.2f}")
    main_window["-TOTAL-EXPENSE-"].update(f"{total_expenses:.2f}")
    main_window["-BALANCE-"].update(f"{balance:.2f}")


def get_row_colors(finance_manager, transactions):
    row_colors = []

    for index, transaction in enumerate(transactions):
        category_color = finance_manager.get_category_color(transaction.category)
        row_colors.append((index, "black", category_color))

    return row_colors


def export_to_csv(finance_manager):
    export_file = Path(__file__).parent / "finance_report.csv"
    total_income, total_expenses, balance = finance_manager.calculate_totals()

    with open(export_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])

        for transaction in finance_manager.transactions:
            writer.writerow([
                transaction.transaction_date,
                transaction.title,
                transaction.amount,
                transaction.category,
                transaction.transaction_type
            ])

        writer.writerow([])
        writer.writerow(["Total ingresos", total_income])
        writer.writerow(["Total gastos", total_expenses])
        writer.writerow(["Balance neto", balance])

    show_message(f"Archivo CSV generado correctamente:\n{export_file}")


def show_error(message):
    sg.popup_error(message)


def show_message(message):
    sg.popup(message)