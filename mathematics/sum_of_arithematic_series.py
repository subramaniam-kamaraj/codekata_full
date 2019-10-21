'''

Given 3 numbers A,B,C find the sum of Arithmetic Series
    with a=A, d=B and n=C
Sample Testcase :
INPUT
1 1 2
OUTPUT
3

'''
#formula
#nth term
#an=a1+(n-1)d
#Arithmetic sum
#Sn = n(a1+an)/2

A,B,C=map(int,input().split())
an=A+(C-1)*B
arithseries=C*(A+an)//2
print(arithseries)
