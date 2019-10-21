'''
Given a range[l,r], print the sum of all the odd numbers in the range(inclusive).
Sample Testcase:
INPUT
5 10
OUTPUT
21
'''
l,r=map(int,input().split())
s=0
c=[]
for i in range(l,r):
    if i%2!=0:
        c.append(i)


print(sum(c))
