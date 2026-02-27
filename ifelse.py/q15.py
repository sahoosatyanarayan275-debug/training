#wap take 3 no. from keybord display biggest number
print("entr a number")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first no is greatest")
	else:
		print("3dr no is greatest")
else:
	if no2>=no3:
		print("2nd no is greatest")
	else:
		print("3rd no is greatest")
