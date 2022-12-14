print("Giving number in words")
def conv(n):
    if n>999:
        print("please enter the number in range 0-999")
    else:
        d = [0,0,0]
        i = 0
        if(n==0):
            print("zero")
        while n>0:
            d[i] = n%10
            i+=1
            n=n//10
        num = " "
        if d[2]!=0:
            num += number[d[2]] + " Hundred "
        if d[1] != 0:
            if(d[1]==1):
                num += tens[d[0]]
            else:
                num += nty[d[1]]+ " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
        print(num)
number = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
tens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n = int(input("Enter a number: "))

conv(n)