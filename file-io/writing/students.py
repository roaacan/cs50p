import csv


name = input("What's your name? ")
course = input("Course: ")
score = input("Score: " )


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "course", "score"])
    writer.writeheader()
    writer.writerow({"name": name, "course": course, "score": score})


"""
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, course, score])
"""