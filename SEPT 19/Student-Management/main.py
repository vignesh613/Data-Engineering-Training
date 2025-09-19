# main.py
from utils import (
    load_students, save_students, load_teachers, save_teachers,
    print_all_students, print_all_teachers, find_topper, avg_salary,
    highest_paid_teacher, student_teacher_mapping, students_per_grade,
    average_marks_per_subject, total_salary_spent
)
from student import Student
from teacher import Teacher

def add_new_student(students):
    new_id = max(students.keys(), default=0) + 1
    name = input("Student name: ").strip()
    age = int(input("Age: "))
    grade = input("Grade/Class: ").strip()
    marks = {}
    print("Enter marks (subject and score). Type 'done' as subject to finish.")
    while True:
        subj = input(" Subject (or 'done'): ").strip()
        if subj.lower() == "done":
            break
        score = float(input(f"  Score for {subj}: "))
        marks[subj] = score
    s = Student(new_id, name, age, grade, marks)
    students[new_id] = s
    save_students(students)
    print(f"Added student ID {new_id}")

def add_new_teacher(teachers):
    new_id = max(teachers.keys(), default=0) + 1
    name = input("Teacher name: ").strip()
    subject = input("Subject: ").strip()
    salary = float(input("Salary: "))
    t = Teacher(new_id, name, subject, salary)
    teachers[new_id] = t
    save_teachers(teachers)
    print(f"Added teacher ID {new_id}")

def generate_reports(students, teachers):
    print("\n==== Reports ====")
    print_all_students(students)
    print_all_teachers(teachers)

    topper = find_topper(students)
    if topper:
        print(f"\nTopper: {topper.name} (ID {topper.id}) with avg {topper.get_average():.2f}")

    print(f"\nAverage teacher salary: {avg_salary(teachers):.2f}")
    hp = highest_paid_teacher(teachers)
    if hp:
        print(f"Highest paid teacher: {hp.name} ({hp.subject}) salary {hp.salary:.2f}")

    mapping = student_teacher_mapping(students, teachers)
    print("\nStudent -> Class Teacher (based on student's top subject):")
    for sid, teacher in mapping.items():
        student = students[sid]
        if teacher:
            print(f" - {student.name} (Top subject: {student.top_subject()}) -> {teacher.name} ({teacher.subject})")
        else:
            print(f" - {student.name} (Top subject: {student.top_subject()}) -> No teacher for this subject")

    print("\nSummary:")
    print(" Students per grade:", students_per_grade(students))
    print(" Average marks per subject:", average_marks_per_subject(students))
    print(" Total salary spent on teachers:", total_salary_spent(teachers))

def menu_loop():
    students = load_students("students.json")
    teachers = load_teachers("teachers.csv")

    while True:
        print("\n===== School Management Menu =====")
        print("1. View all students")
        print("2. View all teachers")
        print("3. Add new student")
        print("4. Add new teacher")
        print("5. Generate reports")
        print("6. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            print_all_students(students)
        elif choice == "2":
            print_all_teachers(teachers)
        elif choice == "3":
            add_new_student(students)
        elif choice == "4":
            add_new_teacher(teachers)
        elif choice == "5":
            generate_reports(students, teachers)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu_loop()
