people = ["Juan", "Felipe", "Maria"]

# peruvians = [{"name": person, "country": "Peru"} for person in people]
peruvians = {person: "Peru" for person in people}

print(peruvians)