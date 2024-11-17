class Name:
	def __init__(self, name):
		self.name = name

	
	def __add__(self, other):
		return f"{self.name} is friend with {other.name}"


marco = Name("Marco")
juan = Name("Juan")
print(marco + juan)