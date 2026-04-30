#stack program in python(without oop)
MAX=5
queue=[0] * MAX
front,rear=-1,-1
def enqueue():
	global rear, front
	if rear== MAX -1:
		print("")
