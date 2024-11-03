"""
    01: Read csv files
    with open("students.csv") as file:
    for line in file:
       name, subject, age = line.rstrip().split(",")
       print(f"{name} is taking the subject '{subject}' at the age of {age}.")
"""
students = []

with open("students.csv") as file:
    for line in file:
        name, subject, age = line.rstrip().split(",")
        student = {"name": name, "subject": subject, "age": age}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is taking the subject '{student['subject']}' at the age of {student['age']}.")
