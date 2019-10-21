'''
Given base and height of a triangle find the area.
Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4
'''
b,h=map(int,input().split())
area=b*h//2
print(area)