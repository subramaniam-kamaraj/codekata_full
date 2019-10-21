'''
Given a range[l,r],
print the sum of all the odd numbers in the range(inclusive).

Sample Test case:

INPUT
5 10
OUTPUT
21
'''

l,r=map(int,input().split())
summ=0
for i in range(l,r):
    if i%2!=0:
        summ=summ+i
print(summ)