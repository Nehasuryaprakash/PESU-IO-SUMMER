s=input("enter the string")
l=[]
j=[]
for i in s:
	l.append(i)
	if(i.isdigit()==True):
		j.append(i)
if(l==j):
	print("the string is numeric")
else:
	print("the string is not numeric")
