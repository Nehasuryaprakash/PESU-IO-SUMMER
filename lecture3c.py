def binary(array, value):
	low = 0
	high = len(array)-1
	while low <= high:
		midvalue = (low + high) // 2
		if array[midvalue] < value:
			low = midvalue + 1
		elif value < array[midvalue]:
			high = midvalue - 1
		else:
			return midvalue
	return None
  
l=[]
n=int(input("Enter the number of elements in the desired array:"))
for i in range(0,n):
	k=int(input())
	l.append(k)
	
m=int(input("Enter the value you want to search for"))
print(binary(l,m))
