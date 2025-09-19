# student.py
from person import Person
from typing import Dict

class Student(Person):
    def __init__(self, student_id: int, name: str, age: int, grade: str, marks: Dict[str, float]):
        super().__init__(name, age)
        self.id = int(student_id)
        self.grade = str(grade)
        # ensure marks values are floats
        self.marks = {subject: float(score) for subject, score in marks.items()}

    def get_average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_subject(self):
        """Return subject with highest mark (or None if no marks)"""
        if not self.marks:
            return None
        return max(self.marks.items(), key=lambda kv: kv[1])[0]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "marks": {k: v for k, v in self.marks.items()}
        }

    def __repr__(self):
        avg = self.get_average()
        return f"Student(id={self.id}, name={self.name}, grade={self.grade}, avg={avg:.2f})"
