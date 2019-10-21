'''

Given a number N, print the odd factors of the number.
Input Size : 1 <= N <= 1000
Sample Testcase :
INPUT
9
OUTPUT
1 3 9
'''

n=int(input())
ap=[]
for i in range(1,n+1):
    if n%i==0:
        ap.append(i)
for i in ap:
    print(i,end=" ")