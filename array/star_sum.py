'''
Given a number N an array of N numbers.
 The task is to find all the star and super star elements in the array
  an print in a seperate line.
  Star are those elements which are strictly greater than all the elements
  on its right side. Super star are those elements
  which are strictly greater than all the elements on its left and right side.
  Assume first element (A[0]) is greater than all the elements on its left side,
   And last element (A[n-1]) is greater than all the elements on its right side.

Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
6
4 2 5 7 2 1
OUTPUT
7 2 1
7
'''
#n=int(input())
lis=list(map(int,input().split()))
ma=max(lis)
cpy=[]
for i in range(0,len(lis)):
    if ma==lis[i]:
        for j in range(i,len(lis)):
            cpy.append(lis[j])

for k in cpy:
    print(k,end=' ')
print()
print(max(cpy))






