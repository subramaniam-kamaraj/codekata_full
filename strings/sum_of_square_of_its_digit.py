'''

Given a number N, print the sum of the squares of its digits.
Input Size : 1 <= N <= 1000000000000000000
Sample Testcase :
INPUT
19
OUTPUT
82
'''
n=list(map(int,input()))
cpy=[]

for i in n:
    cpy.append(i**2)
print(sum(cpy))