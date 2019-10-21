'''
Swagger and Rock are playing a word game. They need to check the two strings use the same base alphabets.
 Two strings are said to have same base alphabets if the use the same characters to form the word.
 eg: rescue and curse have same base alphabets - c,e,r,s,u.
Input Size : |S| <= 1000000
Sample Testcase :
INPUT
rescue curse
OUTPUT
true
'''
S,k=input().split()
if S in k:
    print('true')
else:
    print('false')
