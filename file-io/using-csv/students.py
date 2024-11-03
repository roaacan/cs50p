import csv


students = []

with open("./students.csv") as file:     
    reader = csv.DictReader(file) # Return dictionaries
    for  row in reader:
        students.append({"name": row["name"], "course": row["course"], "score": row["score"]})



for student in sorted(students, key=lambda student: student["score"], reverse=True):
    print(f"The student {student['name']} received a score of {student['score']} in the {student['course']} course.")



"""
 reader = csv.reader(file) # Read a csv file for your, deal with it for you.
 for name, course, score in reader:
        students.append({"name": name, "course": course, "score": score})
"""