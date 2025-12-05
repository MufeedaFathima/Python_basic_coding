x = int(input("enter the year"))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print(" is leap year")
        else:
             print(" is not leap year")
    else:
        print("is leap year")
else:
    print("is not leap year")