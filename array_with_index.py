n=input()
a=[]
if n.isdigit()==True:
    n=int(n)
    if 1<=n and n<=100000:
        for i in range(1,n+1):
            a.append(int(input()))

         for a in range(1,a+1):
             print(a.index('a'))


    else:
          print("invalid")
