'''
Given a string S ,
print the vowels first and then
 consonants in the same order as they have occurred in the string.
Input Size : N <= 10000
Sample Testcase :
INPUT
asdaqrew
OUTPUT
aaesdqrw

'''


s=input()
vo='aeiouAEIOU'
c=''
d=''
for i in s:
    if i in vo:
        c=c+i
    else:
        d=d+i
print(c+d)