'''

Given a number N, check whether it is a power of 2.
Sample Testcase :
INPUT
2048
OUTPUT
yes


'''

n=int(input())

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True

if isPowerOfTwo(n):
    print("yes")
else:
    print("no")