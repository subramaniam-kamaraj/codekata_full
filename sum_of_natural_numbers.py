N=input()
if N.isdigit()==True:
    N=int(N)
    if N>0:
        sum=0
        while(N>0):
            sum=sum+N
            N=N-1
        print(sum)
else:
    print("invalid")    
