value= input("enter a value:")

if value.isnumeric():
    if int(value) >= 90:
        print ("excellent performance")
    elif int(value) < 40:
        print ("try harder next time")
    else:
        print("adequate performance")
else:
    print ("the input must be whole number")
