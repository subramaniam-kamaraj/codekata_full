'''
you are given with array of numbers.you have to find whether array is beautiful or not.
A beautiful array is an
array whose sum of all numbers is divisible by 2, 3 and 5

Sample Input :
5
5 25 35 -5 30

Sample Output :
1  '''

n=int(input())
lis=list(map(int,input().split()))
tot=sum(lis)
if tot%2==0 and tot%3==0 and tot%5==0 :
    print(1)