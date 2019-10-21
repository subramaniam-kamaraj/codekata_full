'''
Given a number N, print the sum of first and last digit.
Input Size : |N| <= 1000000000000000
Sample Testcase :
INPUT
51233
OUTPUT
8
'''
n=input()
first=int(n[0])
second=int(n[-1])
print(first+second)
