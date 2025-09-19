# teacher.py
from person import Person

class Teacher(Person):
    def __init__(self, teacher_id: int, name: str, subject: str, salary: float):
        super().__init__(name, age=0)  # teachers.csv doesn't include age — set 0 or modify if you have age
        self.id = int(teacher_id)
        self.subject = str(subject)
        self.salary = float(salary)

    def get_details(self) -> str:
        return f"Teacher(id={self.id}, name={self.name}, subject={self.subject}, salary={self.salary:.2f})"

    def to_csv_row(self):
        return [self.id, self.name, self.subject, int(self.salary)]

    def __repr__(self):
        return self.get_details()
