#CSV import/export for the Student Management System

import os
import csv

THIS_DIR = os.path.dirname(__file__)
DEFAULT_CSV_PATH = os.path.abspath(os.path.join(THIS_DIR, '..', 'csv', 'students.csv'))

CSV_HEADERS = [
    'full_name',
    'section',
    'spanish_grade',
    'english_grade',
    'social_grade',
    'science_grade',
    'average',
]

def ensure_csv_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def section_is_valid(text):
    if not isinstance(text, str):
        return False
    text = text.strip().replace(' ', '').upper()
    if len(text) not in (2, 3):
        return False
    last = text[-1]
    if not (last.isalpha() and last.isupper()):
        return False
    number_part = text[:-1]
    if not (number_part.isdigit() and 1 <= len(number_part) <=2):
        return False
    return True


def normalize_section(text):
    return text.strip().replace(' ', '').upper()


def student_average_from_values(span, eng, soc, sci):
    return (span + eng + soc + sci) / 4.0


def export_csv(students, path=DEFAULT_CSV_PATH):
    ensure_csv_dir(path)
    try:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
            writer.writeheader()
            for student in students:
                span = float(student['spanish_grade'])
                eng = float(student['english_grade'])
                soc = float(student['social_grade'])
                sci = float(student['science_grade'])
                avg = student_average_from_values(span, eng, soc, sci)
                writer.writerow({
                    'full_name': student['full_name'],
                    'section': student['section'],
                    'spanish_grade': span,
                    'english_grade': eng,
                    'social_grade': soc,
                    'science_grade': sci,
                    'average': f"{avg:.2f}",
                })
        print(f"Data exported to: {os.path.abspath(path)}")
    except OSError as Error:
        print(f"Export failed: {Error}")


def import_csv(students, path=DEFAULT_CSV_PATH):
    metrics = {'imported': 0, 'skipped': 0, 'errors': 0}

    if not os.path.exists(path):
        print('No previously exported file found. Please export at least once before importing.')
        return metrics

    try:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            expected_headers = CSV_HEADERS
            found_headers = reader.fieldnames or []
            missing_headers = [header for header in expected_headers if header not in found_headers]
            if missing_headers:
                print(f'Invalid CSV format. Missing headers: {missing_headers}')
                return metrics
            
            line_number = 1
            for row in reader:
                line_number += 1
                try:
                    full_name = (row.get('full_name') or '').strip()
                    section = normalize_section(row.get('section') or '')

                    if len(full_name) < 3:
                        raise ValueError('full_name too short')
                    if not section_is_valid(section):
                        raise ValueError('Invalid section format')
                    
                    def parse_grade(key):
                        text = (row.get(key) or '').strip()
                        if text == '':
                            raise ValueError(f'{key} empty')
                        try:
                            value = float(text)
                        except ValueError:
                            raise ValueError(f'{key} not a number')
                        if not (0.0 <= value <= 100.0):
                            raise ValueError(f'{key} out of range')
                        return value

                    span = parse_grade('spanish_grade')
                    eng = parse_grade('english_grade')
                    soc = parse_grade('social_grade')
                    sci = parse_grade('science_grade')

                    students.append({
                        'full_name': full_name.title(),
                        'section': section,
                        'spanish_grade': span,
                        'english_grade': eng,
                        'social_grade': soc,
                        'science_grade': sci,
                    })
                    metrics['imported'] += 1

                except Exception as Error:
                    print(f'Line {line_number}: skipped due to error -> {Error}')
                    metrics['skipped'] += 1

    except OSError as Error:
        print(f'Import failed: {Error}')
        metrics['errors'] += 1

    print(
        f"Import summary -> imported: {metrics['imported']}, "
        f"skipped: {metrics['skipped']}, errors: {metrics['errors']}"
    )
    return metrics

