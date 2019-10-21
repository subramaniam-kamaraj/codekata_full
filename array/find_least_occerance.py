'''
Given a number N and array of N integers,
find the number which occurs the least number of times.
Input Size : |N| <= 1000000
Sample Testcase :
INPUT
5
3 3 4 4 7
OUTPUT
7
'''
#import collections as cs
n=int(input())
lis=list(map(int,input().split()))
#gets_indexes = lambda lis, xs: [i for (y, i) in zip(xs, range(len(xs))) if lis == y]
#print(get_indexes)
#a=cs.Counter(lis)
#print(a.values())

