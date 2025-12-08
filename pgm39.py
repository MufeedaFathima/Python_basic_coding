st = input("enter the string")
for i in set(st):
    print(sorted(f"{i}"*st.count(i),end =" "))
    


