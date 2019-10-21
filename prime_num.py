n=int(input())
flg=0
if (n<=1000):
    for i in range(2,n):
        if  n%i==0:
            flg=1
            break

    if flg==1:
        print("no")
    else:
        print("yes")
else:
    print("invalid")






