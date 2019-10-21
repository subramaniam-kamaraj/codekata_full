'''Given a binary number convert it to hexadecimal.
Sample Testcase :
INPUT
1100100
OUTPUT
64'''


num=int(input(),2)
h=str(hex(num))
k=h[2:]
print(int(k))

