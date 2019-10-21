'''
Given 2 strings S,X. Print yes if their lengths are co-prime otherwise no.
Input Size : 1 <= |s|, |x| <= 100000
Sample Testcase :
INPUT
GUVI GREAT
OUTPUT
yes
'''

import math
S,X=map(str,input().split())
S_len=len(S)
X_len=len(X)

if math.gcd(S_len,X_len)==1:
    print("yes")
else:
    print("no")
