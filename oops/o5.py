class rectangle:
	def __init__(self):
	    self.length=5
	    self.breadth=7
	def show(self):
		print("rectangle length=",self.length)
		print("rectangle breadth=",self.breadth)
	def area (self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return
		2*(self.length+self.breadth)
r=rectangle()
r.show()
r.area()
print("parimeter of rectangle=",r.perimeter())
r1=rectangle()
r1.show()
r1.area()
print("parimeter of rectangle=",r1.perimeter())