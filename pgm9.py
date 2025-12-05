x = int(input("enter a number"))
r=0
n=x
while x !=0:
    l = x%10
    r = r*10 + l
    x = x//10
print(r)
if n==r:
    print("Palindrome")
else:
    print("Not Palindrome")