"""
Escribir en un archivo
# 01 Cerrar archivo manualmente
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""
"""
# 02 Cerrar archivo automaticamente
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""

"""
Leer un archivo
# 01
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in sorted(lines):
    print("hello,", line.rstrip())

# 02
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names):
    print("hello,", name)

# 03
"""
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,", line.rstrip())