#CSV import/export for the Student Management System

import os
import csv
from models import Student

def ensure_csv_dir(path):
    directory = os.path.dirname(path)
    if os.path.exists(directory):
        if not os.path.isdir(directory):
            raise OSError(f'Path exists but is not a directory: {directory}')
    else:
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


def export_csv(students, *, path, headers):
    ensure_csv_dir(path)
    try:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for student in students:
                    writer.writerow(student.to_dict())
        print(f"Data exported to: {os.path.abspath(path)}")
    except OSError as Error:
        print(f"Export failed: {Error}")


def import_csv(students, *, path, headers):
    metrics = {'imported': 0, 'skipped': 0, 'errors': 0}

    if not os.path.exists(path):
        print('No previously exported file found. Please export at least once before importing.')
        return metrics

    try:
        with open(path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            found_headers = reader.fieldnames or []
            missing_headers = [header for header in headers if header not in found_headers]
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

                    student = Student(full_name.title(), section, span, eng, soc, sci)
                    students.append(student)
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

