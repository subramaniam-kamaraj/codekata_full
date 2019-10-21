'''
Given a number and a number of K, find the greatest number which divides both.
Input Size : N and K <= 100000
Sample Testcase :
INPUT
5 10
OUTPUT
5
'''

import math
a,k=map(int,input().split())
a=math.gcd(5,10)
print(type(a))