numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0

#even = [n for n in numbers if n %2 == 0]
even = filter(lambda n: n % 2 == 0, numbers)
print(*even)