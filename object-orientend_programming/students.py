class Student:

    def __init__(self, name, house):
        self.name = name 
        self.house = house


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


    # Getter
    @property
    def house(self):
        return self._house


    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        
        # Return an oject from this current class 
        return cls(name, house)


    def __str__(self):
        return f"{self.name} from {self.house}"
    



def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()