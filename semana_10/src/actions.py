# Logic for the actions of the Student Management System
def normalize_spaces(text):
    return " ".join(text.strip().split())


def is_valid_full_name(text):
    if not isinstance(text, str):
        return False
    cleaned = normalize_spaces(text)
    if len(cleaned) < 3:
        return False

    has_letter = False
    for char in cleaned:
        if char.isalpha():
            has_letter = True
            continue
        if char in (" ", "-","'"):
            continue
        return False
    return has_letter


def add_student(students):
    print('\n-- Add Student --')

    #Full name (min 3 chars)
    while True: 
        raw = input('Full name: ')
        if is_valid_full_name(raw):
            name = normalize_spaces(raw).title()
            break
        print("Invalid name. Use letters/spaces only (optional - or '). Min length: 3.")
    
    #Section: 1-2 digits + 1 uppercase letter
    while True:
        section = input('Section (e.g., 11B): ').strip()
        section = section.replace(' ', '').upper()

        if len(section) in (2, 3) and section[-1].isalpha() and section[-1].isupper():
            number_part = section[:-1]
            if number_part.isdigit() and 1 <= len(number_part) <= 2:
                break 
        print("Invalid section format. Expected like '11B'.")
    
    #Grades
    spanish_grade = ask_grade('Spanish grade (0-100): ')
    english_grade = ask_grade('English grade (0-100): ')
    social_grade = ask_grade('Social Studies grade (0-100): ')
    science_grade = ask_grade('Science grade (0-100): ')

    student = {
        'full_name': name,
        'section': section,
        'spanish_grade': spanish_grade,
        'english_grade': english_grade,
        'social_grade': social_grade,
        'science_grade': science_grade,
    }
    students.append(student)
    print(f'Student added: {name} [{section}]')


def ask_grade(prompt):
    while True:
        grade_str = input(prompt).strip()
        if grade_str == "":
            print('Grade cannot be empty.')
            continue
        try:
            grade = float(grade_str)
        except ValueError as error:
            print(f'Grade must be a number between 0 and 100. Error: {error}')
            continue
        if 0.0 <= grade <= 100.0:
            return grade
        print('Grade out of range. Enter a number between 0 and 100.')


def list_students(students):
    print('\n-- All Students --')
    if len(students) == 0:
        print('No students yet.')
        return

    index = 1
    for student in students:
        average = get_student_average(student)

        print('{}. {} [{}] - Spa:{} Eng:{} Soc:{} Sci:{} | Avg:{:.2f}'.format(
            index,
            student['full_name'],
            student['section'],
            student['spanish_grade'],
            student['english_grade'],
            student['social_grade'],
            student['science_grade'],
            average
        ))
        index = index + 1


def get_student_average(student):
    return (
        student['spanish_grade']
        + student['english_grade']
        + student['social_grade']
        + student['science_grade']
    ) / 4.0


def show_top_three(students):
    print('\n-- Top 3 by Average --')
    if len(students) == 0:
        print('No students to evaluate.')
        return
    
    used_indices = [False] * len(students)
    top_students = []

    limit = min(3, len(students))
    selections_made = 0
    while selections_made < limit:
        best_index = -1

        index = 0
        for candidate in students:
            if used_indices[index]:
                index = index + 1
                continue

            if best_index == -1:
                best_index = index
            else:
                cand_avg = get_student_average(candidate)
                best_avg = get_student_average(students[best_index])

                if cand_avg > best_avg:
                    best_index = index
                elif cand_avg == best_avg:
                    if candidate['full_name'].lower() < students[best_index]['full_name'].lower():
                        best_index = index
            
            index = index + 1
        
        if best_index == -1:
            break

        top_students.append(students[best_index])
        used_indices[best_index] = True
        selections_made = selections_made + 1

    rank = 1
    for student in top_students:
        avg = get_student_average(student)
        print(f"#{rank} {student['full_name']} [{student['section']}] - Avg: {avg:.2f}")
        rank = rank + 1


def show_global_average(students):
    print('\n-- Global Average --')
    if len(students) == 0:
        print('No students to compute the global average.')
        return
    
    total = 0.0
    count = 0
    for student in students:
        total = total + get_student_average(student)
        count = count + 1

    global_avg = total / count
    print(f'Global average across all students: {global_avg:.2f}')






