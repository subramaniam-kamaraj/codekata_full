'''
You are given a number ‘n’. You have to tell whether a number
  is great or not. A great number is a number whose sum of digits let (m)
  and product of digits let(j) when summed together gives the number back
m+j=n
Sample Input :
59
Sample Output :
Great
'''
#import operator
num=int(input())
x=[int(i) for i in str(num)]
m=sum(x)
#print(m)
pro=1
for i in x:
    pro=pro*i
#print(pro)
wholesum=m+pro
#print(wholesum)

if num==wholesum:
    print("Great")