x = input("enter a string")
r = x[::-1]
print("reversed string",x[::-1])
if x.lower() == r.lower():
    print("Palindrome")
else:
    print("Not Palindrome")