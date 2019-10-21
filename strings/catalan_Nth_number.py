'''
Given a number N, print the first N Catalan numbers.
Input Size : N <= 100
Sample Testcase :
INPUT
1
OUTPUT
1 1
'''


def catalan_number(num):
    if num <= 1:
        return 1
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num - i - 1)
    return res_num
n=int(input())
for i in range(n+1):
    print(catalan_number(i),end=" ")