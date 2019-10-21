'''
Ram loves bit magic. He is given a set of integers, and wants
to sort them based on the number of 1s in their binary representations
(in descending order). Help Ram do a little bit of bit magic!

Input Description:
Number of elements followed by the elements

Output Description:
Sorted list of numbers

Sample Input :
6
1 2 3 4 5 6

Sample Output :
3 5 6 1 2 4
'''
n=int(input())
cpy=[]
lis=list(map(int,input().split()))
for i in lis:
    b=bin(i)
    cpy.append(b[2:])
print(cpy)
for j in cpy:
    coun=cpy.count('1')
    print(coun)
