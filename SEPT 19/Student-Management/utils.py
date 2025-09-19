# utils.py
import json
import csv
from collections import defaultdict
from typing import Dict, List
from student import Student
from teacher import Teacher

# ---------- JSON (students) ----------
def load_students(filename="students.json") -> Dict[int, Student]:
    students = {}
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            sid = int(entry.get("id"))
            name = entry.get("name")
            age = int(entry.get("age", 0))
            grade = entry.get("grade", "")
            marks = entry.get("marks", {})
            students[sid] = Student(sid, name, age, grade, marks)
    return students

def save_students(students: Dict[int, Student], filename="students.json"):
    data = [s.to_dict() for s in students.values()]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ---------- CSV (teachers) ----------
def load_teachers(filename="teachers.csv") -> Dict[int, Teacher]:
    teachers = {}
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tid = int(row["id"])
            name = row["name"]
            subject = row["subject"]
            salary = float(row["salary"])
            t = Teacher(tid, name, subject, salary)
            teachers[tid] = t
    return teachers

def save_teachers(teachers: Dict[int, Teacher], filename="teachers.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "subject", "salary"])
        for t in teachers.values():
            writer.writerow([t.id, t.name, t.subject, int(t.salary)])

# ---------- Reports & Analysis ----------
def print_all_students(students: Dict[int, Student]):
    print("\nStudents:")
    for s in students.values():
        avg = s.get_average()
        print(f" - ID {s.id}: {s.name}, Grade {s.grade}, Age {s.age}, Avg = {avg:.2f}, Marks = {s.marks}")

def print_all_teachers(teachers: Dict[int, Teacher]):
    print("\nTeachers:")
    for t in teachers.values():
        print(f" - {t.get_details()}")

def find_topper(students: Dict[int, Student]):
    if not students:
        return None
    return max(students.values(), key=lambda s: s.get_average())

def avg_salary(teachers: Dict[int, Teacher]) -> float:
    if not teachers:
        return 0.0
    return sum(t.salary for t in teachers.values()) / len(teachers)

def highest_paid_teacher(teachers: Dict[int, Teacher]):
    if not teachers:
        return None
    return max(teachers.values(), key=lambda t: t.salary)

def student_teacher_mapping(students: Dict[int, Student], teachers: Dict[int, Teacher]):
    """
    For each student, find a teacher whose subject matches the student's top subject.
    Returns dict: student_id -> teacher (or None)
    """
    subj_to_teacher = {}
    for t in teachers.values():
        # if multiple teachers teach same subject, this picks the last one encountered
        subj_to_teacher.setdefault(t.subject, t)

    mapping = {}
    for s in students.values():
        top_sub = s.top_subject()
        mapping[s.id] = subj_to_teacher.get(top_sub)  # possibly None
    return mapping

def students_per_grade(students: Dict[int, Student]):
    counts = defaultdict(int)
    for s in students.values():
        counts[s.grade] += 1
    return dict(counts)

def average_marks_per_subject(students: Dict[int, Student]):
    totals = defaultdict(float)
    counts = defaultdict(int)
    for s in students.values():
        for subj, mark in s.marks.items():
            totals[subj] += mark
            counts[subj] += 1
    avg = {}
    for subj in totals:
        avg[subj] = (totals[subj] / counts[subj]) if counts[subj] else 0.0
    return avg

def total_salary_spent(teachers: Dict[int, Teacher]):
    return sum(t.salary for t in teachers.values())
