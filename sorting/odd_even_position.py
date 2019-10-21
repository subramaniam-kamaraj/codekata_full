'''
Vishal is a competitive coder and he loves problems on sorting and searching.
He is bored right now and decides to solve a sorting problem with a modification.
He decides to sort the elements at the even indices of an array in ascending order
and the elements at the odd indices in descending order.
Vishal goes outside his room after coding the solution,
but his laptop crashes and he is unable to show it to his teacher.
Can you help Vishal by coding the solution to the problem?

Constraints:

0<=array[i]<=10000

Input Description:
Size of the array followed by the elements of the array

Output Description:
Sorted elements of the array

Sample Input :
10
9 8 7 1 2 3 6 5 4 10

Sample Output :
2 10 4 8 6 5 7 3 9 1

'''

n=int(input())
lis=list(map(int,input().split()))
l1=[]
l2=[]
#res=[]
combine=[]
#final=[]

for i in lis:
    if lis.index(i)%2==0:
        l1.append(i)
    if lis.index(i)%2!=0:
        l2.append(i)


r1=sorted(l1)
r2=sorted(l2,reverse=True)

#print(r1,r2)
#combine=r1+r2

'''for i in range(0,n):
    if combine.index(i)%2==0:
        final.append(i)
    else:
        final.append(i)
'''
print(l1)
print(l2)
print(r1)
print(r2)
#print(combine)
#print(final)
