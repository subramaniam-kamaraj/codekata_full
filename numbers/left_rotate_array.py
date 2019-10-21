'''You are given with an array.
Your task is to print the left rotated array after k operations.

Time:O(n)
Extra Space: O(1)

Sample Input :
7 3
1 2 3 4 5 6 7

Sample Output :
4 5 6 7 1 2 3
'''

n,k=map(int,input().split())
lis=list(map(int,input().split()))

test_lis=lis[k:]+lis[:k]
for i in test_lis:
    print(i,end=" ")