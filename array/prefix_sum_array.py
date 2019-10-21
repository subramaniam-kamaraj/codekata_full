'''

Given a number N and an array of N integers, print the prefix sum array.
Input Size : N <= 100000
Sample Testcase :
INPUT
4
2 4 4 2
OUTPUT
2 6 10 12

'''

n=int(input())
lis=list(map(int,input().split()))
em=[]
l=len(lis)
res=0
for i in range(0,l):
    res=res+lis[i]
val=res
res=0
for i in range(0,l-1):
    res=res+lis[i]
val1=res
res=0
for i in range(0,l-2):
    res=res+lis[i]
val2=res
res=0
for i in range(0,l-3):
    res=res+lis[i]
val3=res
print(val3,val2,val1,val)


