n,k=map(int,input().split())
lis=list(map(int,input().split()))
if len(lis)==0:
    print("-1")
else:
    l = lis.index(k)
    print(l)
