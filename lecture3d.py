n=int(input("Enter a desired number: "))
s = 0
while(n>0):
    r=n%10
    s=s+r
    n=n//10

print("the sum of the digits is",s)
