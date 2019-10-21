#amstrong number check

n=input()
summ=0
if n.isdigit()==True:
    n=int(n)
    if n<=100000:
        temp=n
        while temp>0 :
            digit=temp%10
            summ+=digit**3
            temp//=10
        if n==summ:
            print("yes")
        else:
            print("no")
    else:
        print("invalid")
else:
    print("invalid")