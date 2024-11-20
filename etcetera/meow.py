class Cat:
    MEOWS = 4

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
        

cat = Cat()
cat.meow()