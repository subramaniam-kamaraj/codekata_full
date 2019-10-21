n=input()
#count=0
if n.isdigit()==True:
    n=int(n)
    for i in range(1,6):
        m=n*i
        print(m,end=" ")

else:
    print("invalid")