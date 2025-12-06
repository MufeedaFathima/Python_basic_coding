x = input("enter the number")
lst = ["zero","one","two","three","four","five","six","seven","eight","nine"]
for i in x:
    if i =="-":
        print("minus",end=" ")
    else:
        print(lst[int(i)],end=" ")