'''
Given 2 numbers, perform bitwise xor and f
ind the number of ones in its binary representation.
Sample Testcase :
INPUT
10 5
OUTPUT
4
'''
a,b=map(int,input().split())
c=a^b
conv=bin(c)
d=conv.count("1")
print(d)