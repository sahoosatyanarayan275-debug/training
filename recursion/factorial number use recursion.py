def fact(no):
	if no==0:
		return 1
	else:
		return no*fact(no-1)
res=fact(5)
print("factorial=",res)