def kaprekarNumbers(p, q):
    k=0
    if p<9:
        p=9
        print(1,end=" ")
    for i in range(p,q+1):
        n=i**2
        n=str(n)
        d=len(n)//2
        num1=n[:d]
        num2=n[d:]
        if i==(int(num1)+int(num2)):
            print(i,end=" ")
            k=-1
    if k==0:
        print("INVALID RANGE")
in this question str is used to split each digit as an string it is an inbuilt function 
