class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0 or (n + self.size) > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n < 0 or (self.size - n) < 0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(5)
    jar.deposit(0)
    jar.withdraw(0)
    print(jar)


main()
