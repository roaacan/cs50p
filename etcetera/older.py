students = [
    {"name": "Juan", "age": 20},
    {"name": "Pedro", "age": 16},
    {"name": "Maria", "age": 17},
    {"name": "Martina", "age": 30},
    {"name": "Federico", "age": 18}
]

def is_old(s):
    return s["age"] >= 18


olders = filter(is_old, students)


for older in sorted(olders, key=lambda s: s["name"]):
    print(older["name"])