'''

Given a binary number convert it to octal.
Sample Testcase :
INPUT
1100100
OUTPUT
144
'''

n=int(input(),2)
conv=oct(n)
print(conv[2:])