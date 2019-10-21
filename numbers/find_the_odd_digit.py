'''
A number is given as input.
Find the odd digits in the number,
add them and find if the sum is odd or not. If even print E, if odd print O.
Input Size : N <= 10000000000
Sample Testcase :
INPUT
413
OUTPUT
E
'''

num=map(int,input())
list_num=list(num)
new_lis=[]
for i in list_num:
    if i%2!=0:
        new_lis.append(i)

check=sum(new_lis)
if check%2==0:
    print("E")
else:
    print("O")