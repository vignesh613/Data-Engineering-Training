from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder \
    .appName("StudentsCoursesScenario") \
    .getOrCreate()


#Create DataFrames


# Student data
students_data = [
    (1, "Rahul Sharma", 20, "Bangalore"),
    (2, "Priya Singh", 21, "Delhi"),
    (3, "Aman Kumar", 19, "Hyderabad"),
    (4, "Sneha Reddy", 22, "Chennai"),
    (5, "Arjun Mehta", 23, "Mumbai"),
    (6, "Divya Nair", 20, None)  # Student without city
]
students_cols = ["student_id", "name", "age", "city"]
students_df = spark.createDataFrame(students_data, students_cols)

# Course data
courses_data = [
    (101, "Python", "Programming"),
    (102, "Data Science", "Analytics"),
    (103, "Databases", "Technology"),
    (104, "Business Studies", "Management")
]
courses_cols = ["course_id", "course_name", "category"]
courses_df = spark.createDataFrame(courses_data, courses_cols)

# Enrollment data
enrollment_data = [
    (1, 101, "A"),
    (2, 101, "B"),
    (3, 102, "A"),
    (4, 103, "C"),
    (5, 102, "B"),
    (7, 104, "A")  # Enrollment with non-existent student
]
enrollment_cols = ["student_id", "course_id", "grade"]
enrollment_df = spark.createDataFrame(enrollment_data, enrollment_cols)

# Show all DataFrames
print("===== Students Data =====")
students_df.show()
print("===== Courses Data =====")
courses_df.show()
print("===== Enrollment Data =====")
enrollment_df.show()


# Step 2: Transformation Tasks


print("1. Select all student names and their cities")
students_df.select("name", "city").show()

print("2. Find students who are older than 20")
students_df.filter(students_df.age > 20).show()

print("3. List all courses under the 'Analytics' category")
courses_df.filter(courses_df.category == "Analytics").show()


# Step 3: Aggregation Tasks


print("1. Count how many students are enrolled in each course")
enrollment_df.groupBy("course_id").count().show()

print("2. Find the average age of students per city")
students_df.groupBy("city").agg(F.avg("age").alias("avg_age")).show()

print("3. Get the maximum and minimum age of students")
students_df.agg(
    F.max("age").alias("max_age"),
    F.min("age").alias("min_age")
).show()


# Step 4: Join Tasks

print("1. Join students with enrollments to see which student took which course")
students_enroll_df = students_df.join(enrollment_df, "student_id", "inner")
students_enroll_df.show()

print("2. Left join enrollments with courses to get course details")
enroll_course_df = enrollment_df.join(courses_df, "course_id", "left")
enroll_course_df.show()

print("3. Find students who are not enrolled in any course")
students_without_courses = students_df.join(enrollment_df, "student_id", "left_anti")
students_without_courses.show()

print("4. Find courses with no students enrolled")
courses_without_students = courses_df.join(enrollment_df, "course_id", "left_anti")
courses_without_students.show()


# Step 5: SQL Tasks


# Register temp views
students_df.createOrReplaceTempView("students")
courses_df.createOrReplaceTempView("courses")
enrollment_df.createOrReplaceTempView("enrollment")

print("1. Get all students with their course names and grades")
spark.sql("""
    SELECT s.name, c.course_name, e.grade
    FROM students s
    JOIN enrollment e ON s.student_id = e.student_id
    JOIN courses c ON e.course_id = c.course_id
""").show()

print("2. Find the number of students who got grade 'A' in each course")
spark.sql("""
    SELECT c.course_name, COUNT(*) AS num_A_students
    FROM enrollment e
    JOIN courses c ON e.course_id = c.course_id
    WHERE e.grade = 'A'
    GROUP BY c.course_name
""").show()

print("3. Find the top city with the most students enrolled in courses")
spark.sql("""
    SELECT s.city, COUNT(*) AS student_count
    FROM students s
    JOIN enrollment e ON s.student_id = e.student_id
    GROUP BY s.city
    ORDER BY student_count DESC
    LIMIT 1
""").show()


spark.stop()
