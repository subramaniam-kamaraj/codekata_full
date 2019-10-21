'''

9
Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
Sample Testcase :
INPUT
hello
OUTPUT
he*lo
'''

import math
s=input()

l=len(s)
#q=math.ceil(l/2)
'''
ind=q-1
#k=s.replace(s[ind],'*')
for i in s:
    if s.index(i)==ind:
         k=k+'*'
    else:
        k=k+i
print(k)

'''
evenoutput=[]
oddoutput=[]

if l%2==0:
    res=int(l/2)
    print(res)
    for i in range(0,l):
        if i==res:
            s[i]='*'
            s[i-1]='*'
            #evenoutput=evenoutput+'*'
    print(s)


else:
    res=l//2
    print(res)

