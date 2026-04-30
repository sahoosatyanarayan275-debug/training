# Stack Program in Python (Without OOP)
# Using top 1 and max size variable
MAX = 5
stack = [0] * MAX
top = -1
def push():
	global top 
	if top == MAX 1:
	else:
		print("Stack Overflow")
		item = int(input("Enter element to push: "))
		top top 1
		stack[top] = item
		print(item, "pushed into stack")
def pop_element():
	global top
	if top == -1:
		print("Stack Underflow")
	else:
		item=stack[top]
		top=top-1
		print(item, "popped from stack")