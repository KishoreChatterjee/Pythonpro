print("To determine the possibilities of knight moves")
d = [0,'a','b','c','d','e','f','g','h']
a = input("Enter the alphabet between a-h and enter the value between 1-8 only: ")
b,c = a[0], int(a[1:])
if(b>='a'and b<='i' and c>0 and c<9):
    if((d.index(b)==1 and c==1) or (d.index(b)==1 and c==8) or
        (d.index(b)==8 and c==8) or (d.index(b)==8 and c==1)):
        print("The possible moves of knight from current position are 2")
    elif((d.index(b)==1 and c==2) or (d.index(b)==1 and c==7) or
        (d.index(b)==2 and c==1) or (d.index(b)==7 and c==1) or
        (d.index(b)==1 and c==7) or (d.index(b)==8 and c==7) or
        (d.index(b)==8 and c==2) or (d.index(b)==7 and c==8)):
        print("The possible moves of knight from current position are 3")
    elif((d.index(b)==1 and ((c>=3) or (c<=6) )) or (((d.index(b)>=3) or ((d.index(b)<=6))) and (c==1))or
         (((d.index(b)>=3) or (d.index(b)<=6)) and (c==8)) or (d.index(b)==8 and ((c>=3) or (c<=6) ))):
        print("The possible moves of knight from current positon are 4")

    elif ((d.index(b) == 2 and ((c >= 3) or (c <= 6))) or (((d.index(b) >= 3) or ((d.index(b) <= 6))) and (c == 2)) or
          (((d.index(b) >= 3) or (d.index(b) <= 6)) and (c == 7)) or (d.index(b) == 7 and ((c >= 3) or (c <= 6)))):
        print("The possible moves of knight from current position are 6")
    else:
        print("The possible moves of knight from current position are 8")
else:
    print("Entered value is invalid please enter the value between a-h and 1-9")
