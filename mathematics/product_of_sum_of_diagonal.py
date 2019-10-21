'''
Given a square matrix of size N x N,
find the product of the sum of diagonals.
Input Size : N <= 1000
Sample Testcase :
INPUT
2
2 4
3 7
OUTPUT
63
'''

inp=int(input())
N1,N2=map(int,input().split())
M1,M2=map(int,input().split())
sumofdiagonal1=N1+M2
sumofdiagonal12=M1+N2
product=sumofdiagonal1*sumofdiagonal12
print(product)