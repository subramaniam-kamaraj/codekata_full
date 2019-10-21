'''
Given a string and a number K.Print every kth character from the beginning.
Sample Testcase :
INPUT
string 3
OUTPUT
r g

'''
k=int(input())
s=input()
q=s.index(k+1)
for i in s: 
    if s.index(i)%k==0:
        print(i)