from menu import show_menu, get_choice_from_menu
import actions
import data

def pause():
    try:
        input('\nPress Enter to continue...')
    except (EOFError, KeyboardInterrupt): 
        pass


def main():
    students = []

    print('Welcome to the Student Management System!')
    while True:
        try:
            show_menu()
            choice = get_choice_from_menu()

            if choice == 1:
                actions.add_student(students)
                pause()
            elif choice == 2:
                actions.list_students(students)
                pause()
            elif choice == 3:
                actions.show_top_three(students)
                pause()
            elif choice == 4:
                actions.show_global_average(students)
                pause()
            elif choice == 5:
                data.export_csv(students)
                pause()
            elif choice == 6:
                data.import_csv(students)
                pause()
            elif choice == 7:
                print('Goodbye!')
                break
        except (KeyboardInterrupt, EOFError):
            print('\nExiting...')
            break


if __name__ == '__main__':
    main()