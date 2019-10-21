'''Print the position of first 1 from right to left,
   in binary representation of an Integer.
Sample Testcase :
INPUT
18
OUTPUT
2 '''
num=int(input())
pos = 1

# counting the position of first set bit
for i in range(32):
    if not (num & (1 << i)):
        pos += 1
    else:
        break
print(pos)
