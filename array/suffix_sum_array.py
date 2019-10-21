'''
Given a number N and an array of N integers, print the suffix sum array.
Input Size : N <= 100000
Sample Testcase :
INPUT
4
2 4 4 2
OUTPUT
12 10 6 2 '''
n=int(input())
lis=list(map(int,input().split())) #[2,4,4,2]
em=[]

for i in range(0,len(lis)):
    em.append(sum(lis))
    del lis[0]
    i=i-1
for i in em:                        # 12 10 6 2
    print(i,end=" ")