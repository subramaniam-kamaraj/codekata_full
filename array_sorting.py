n=input()
a=[]
if n.isdigit()==True:
    n=int(n)
    if 1<=n and n<=100000:
        for i in range(1,n+1):
            a.append(int(input()))
        a.sort()
        print(a)                                    #minimum of array
    else:
          print("invalid")
