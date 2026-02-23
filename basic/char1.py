import sys
print("enter a char")
ch=input()
if len(ch)>1:
	print("one char allow")
	sys.exit()
if ch>='A'and ch<'Z':
   ch=chr(ord(ch)+32)    #if 65<ch<90   	
   print(ch)
ch=ord(ch)