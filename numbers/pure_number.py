'''
You are given a task to tell whether the number is pure or not.
 A pure number is a number whose sum of digits is multiple of 3.

O(1) time and O(1) space
Sample Input :
13
Sample Output :
Not
'''
num=map(int,input())
check=sum(list(num))
if check%3!=0:
    print('Not')
else:
    print('pure')

