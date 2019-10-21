'''
Given a string S of length N,
find if it can be a valid Hexadecimal representation of a number.
Input Size : N <= 10000
Sample Testcase :
INPUT
1AE23
OUTPUT
yes '''

#st=input()
#if st.isalnum()==True:
#    if 'A' in st or 'B' in st or 'C' in st or 'D' in st or 'F' in st:
#        print("yes")


s=input()
hex_digits = set("0123456789abcdefABCDEF")
for char in s:
    if char in hex_digits:
        print("yes")
