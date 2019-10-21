'''
Given a string S, print 'yes' if it is a palindrome or 'no' if it is not a palindrome.
Sample Testcase :
INPUT
lappal
OUTPUT
yes
'''
s=input()
rev=s[::-1]
if s ==rev:
    print("yes")
else:
    print("no")