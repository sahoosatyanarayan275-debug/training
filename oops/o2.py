class simple:
	def __init__(self,p,r,t):
		self.principal=p
		self.rate=r
		self.time=t
	def show(self):
		print("principal=",self.principal)
		print("rate=",self.rate)
		print("time=",self.time)
	def sical(self):
		return self.principal*self.rate*self.time/100
i1=simple(1000,10,2)
i1.show()
print("simple interest=",i1.sical())
