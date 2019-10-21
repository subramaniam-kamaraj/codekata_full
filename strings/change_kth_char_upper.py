'''

Given a string and a number K,
change every kth character to uppercase
from beginning in string.
Sample Testcase :
INPUT
string 2
OUTPUT
sTrInG
'''
s,k=(input().split())
k=int(k)
f=''
for i in s:
    if s.index(i)==(k+1):
        f.append(i.Upper())

