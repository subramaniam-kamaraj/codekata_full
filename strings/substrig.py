'''
Given a String S and a string P,
  find if P is a substring of S.
   Print 'yes' if it is a substring else 'no'.

Input Size : |s| <= 10000 |p| <= 1000.

Sample Testcase :
INPUT
sundar sun
OUTPUT
yes
'''
S,P=input().split()
if P in S:
    print("yes")
else:
    print("no")