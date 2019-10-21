'''
You are passport issuer, but due to some problem in the system there are redundant  passport numbers. Your task is to delete all the duplicate passport numbers.You are given with a list of passport numbers.

Sample Input :
5
A23 B56 C79 D16

Sample Output :
A23 B56 C79 D16
'''

N=int(input())
d=[]
s=list(map(str,input().split()))
#print(set(s))
for i in s:
    if i in d:
        del i
    else:
        d.append(i)
for j in d:
    print(j,end=" ")