def sical():
	print("enter principle")
	p=float(input())
	print("rate of interest")
	r=float(input())
	print("enter time")
	t=float(input())
	si=(p*r*t)/100
	return si
res=sical()
print("simpleinterest=",res)