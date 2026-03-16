class student:
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		self._name = value

s = student("virat")
print(s.name)

s.name = "satya"
print(s.name)