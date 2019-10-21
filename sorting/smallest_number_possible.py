'''
You are given a number ‘n’. Your task is to create the smallest number
 possible using the digits of number.

Input Description:
You are given a number ‘n’,

Output Description:
Print the smallest possible number of same length

Sample Input :
123456789123456789

Sample Output :
112233445566778899
'''
lis=list(map(int,input()))
so=sorted(lis)
final=[]
for i in so:
    final.append(str(i))
k="".join(final)
con=int(k)

