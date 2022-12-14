y=input("Enter the white or black color of the box: ")
y = y.lower()
if y=="black box":
    x = input("Enter the value of box from a1 to h8: ")
    x = x.lower()
    if (x[0]>='a' and x[0]<='h' and int(x[1])>=1 and int(x[1])<9 and len(x)<=2):
        if(ord(x[0])%2!=0) and (int(x[1])%2!=0):
            print("black box")
        elif(ord(x[0])%2!=0) and (int(x[1])%2==0):
            print("White box")
        elif(ord(x[0])%2==0) and (int(x[1])%2!=0):
            print("black box")
        elif(ord(x[0])%2==0) and (int(x[1])%2==0):
            print("White box")
    else:print("invalid entry")
elif y=="white box":
    x = input("Enter the value of box from a1 to h8: ")
    x = x.lower()
    if (x[0]>='a' and x[0]<='h' and int(x[1])>=1 and int(x[1])<9 and len(x)<=2):
        if (ord(x[0]) % 2 == 0) and (int(x[1]) % 2 == 0):
            print("black box")
        elif (ord(x[0]) % 2 == 0) and (int(x[1]) % 2 != 0):
            print("White box")
        elif (ord(x[0]) % 2 != 0) and (int(x[1]) % 2 == 0):
            print("black box")
        elif (ord(x[0]) % 2 != 0) and (int(x[1]) % 2 != 0):
            print("White box")
    else:print("invalid entry")
else:print("Invalid color because You need to enter either white box or black box only")