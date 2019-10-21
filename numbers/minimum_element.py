'''Prateek finds it difficult to judge the minimum element in the list of elements
 given to him. Your task is to develop the algorithm
 in order to find the minimum element.

Sample Input :
5
3 4 9 1 6

Sample Output :
1
'''
num=int(input())
lis=map(int,input().split())
print(min(list(lis)))
