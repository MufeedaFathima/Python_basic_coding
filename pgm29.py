x=int(input("enter a number"))
sq=x**2
n = len(str(x))
if sq%(10**n)==x:
    print("automorphic")
else:
    print("not automorphic")