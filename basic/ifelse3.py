#""wap take emp salary from keybord  if sal>=5000
print("enter basic salary")
sal=float(input())
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
else:
    da=sal*0.2
    hra=sal*0.1
totalsal=sal+da+hra
print("basic sale=",sal)
print("da=",da)
print("hra=",hra)
print("totalsalary=",totalsal)