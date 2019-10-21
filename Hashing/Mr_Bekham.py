'''
Let A[i] represent an element in A.
Mr. Beckham wants to perform an operation on the elements of A.
 He wants to choose a positive integer X and perform A[i]  := A[i] mod X
   for all i (1 <= i <= N). Help Mr.
   Beckham choose the smallest possible value of X such that the elements
    of the array remain distinct even after performing the operation.
    (It can be proven that an answer exists for all possible inputs)

Input Description:
The first line contains an integer N representing the number of elements
   in the array. The next line contains N distinct space separated integers
     denoting the array elements.

Output Description:
Print a single integer X

Sample Input :
2
21 22

Sample Output :
2
'''

n=int(input())
li=list(map(int,input().split()))
p=[]
for i in li:
    p.append(i//10)
if p[0]==p[1]:
    print(p[0])