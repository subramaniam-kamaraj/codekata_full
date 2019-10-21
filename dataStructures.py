'''
Given a number N followed by a list of N numbers.
    Write a program to reverse the list and print the list.
Input Size : 1 <= N <= 10000
Sample Testcases :
INPUT
7
1 2 3 4 5 6 7
OUTPUT
7->6->5->4->3->2->1
'''
n=int(input())
li=list(map(int,input().split()))
rev=sorted(li)
cpy=[]
for i in rev:
    cpy.append(str(i))
    cpy.append('->')
del cpy[-1]
final=''.join(cpy)
print(final)
#print(i,end="->")
