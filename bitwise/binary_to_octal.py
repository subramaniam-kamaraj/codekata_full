'''
Given a binary number convert it to octal.
Sample Testcase :
INPUT
1100100
OUTPUT
144
'''

num=int(input(),2)
convert=oct(num)
converttostring=str(convert[2:])
print(int(converttostring))