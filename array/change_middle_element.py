'''
Given a string S, print it after changing the middle element
 to * (if the length of the string is even, change the 2 middle elements to *).

Sample Testcase :
INPUT
hello

OUTPUT
he*l
'''

s=list(map(str,input()))
cpy=[]
l=len(s)
if l%2!=0:
    n=l//2
    print(n)
    val=s[n]
    for i in s:
        if s[i]==val:
            print("yes")







