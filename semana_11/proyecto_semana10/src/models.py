class Student:
    def __init__(self, full_name, section, spanish_grade, english_grade, social_grade, science_grade):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = float(spanish_grade)
        self.english_grade = float(english_grade)
        self.social_grade = float(social_grade)
        self.science_grade = float(science_grade)
    

    def average(self):
        return (
            self.spanish_grade
            + self.english_grade
            + self.social_grade
            + self.science_grade
        ) / 4.0
    

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_grade": self.social_grade,
            "science_grade": self.science_grade,
            "average": f"{self.average():.2f}",
        }
    

    @staticmethod
    def from_dict(d):
        return Student(
            d["full_name"],
            d["section"],
            d["spanish_grade"],
            d["english_grade"],
            d["social_grade"],
            d["social_grade"],
            d["science_grade"],
        )