"""
Menu module for the Student Management System

Goals:
- Print the main menu to the console.
- Read and validate the user's choice.
- Return a valid option 
"""
def show_menu():
    print('\n=== Student Management System (CLI) ===')
    print('1) Add a student')
    print('2) View all students')
    print('3) View Top 3 by average')
    print('4) View global average (across all students)')
    print('5) Export data to CSV')
    print('6) Import data from CSV (previously exported)')
    print('7) Exit')


def get_choice_from_menu():
    valid_choices = {'1', '2', '3', '4', '5', '6', '7'}
    while True:
        try:
            option = input('Select an option: ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nExiting...')
            return 7
        if option in valid_choices:
            return int(option)
        print("Invalid option. Please choose an option between [1-7]")


if __name__ == "__main__":
    show_menu()
    choice = get_choice_from_menu()
    print("You selected:", choice)