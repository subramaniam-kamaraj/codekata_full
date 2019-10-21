'''
Given a number N, print the even factors of the number.
Input Size : 1 <= N <= 1000
Sample Testcase :
INPUT
8
OUTPUT
2 4 8
'''

n=int(input())
ap=[]
for i in range(2,n+1):
    if n%i==0:
        ap.append(i)
for i in ap:
    print(i,end=" ")
