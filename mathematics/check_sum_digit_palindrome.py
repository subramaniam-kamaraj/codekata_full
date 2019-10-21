'''

Given a number N, check if the sum of the digits is a Palindrome.
Print 'yes' or 'no' accordingly.
Input Size : 2 <= N <= 1000000000000000000
Sample Testcases :
INPUT
13
OUTPUT
yes

'''

n=list(map(int,input()))

lis=sum(n)
st=str(lis)
rev=st[::-1]
res=int(rev)

if lis is res:
    print("yes")
else:
    print("no")
