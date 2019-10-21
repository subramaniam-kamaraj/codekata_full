n=input()
fact=1
if n.isdigit()==True:
    n=int(n)

    for i in range(2,n+1):
        fact=fact*i                     #factorial
    print(fact)
else:
    print("invalid")