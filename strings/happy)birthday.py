'''
Given 2 strings S,X. Print the string after deleting X.
  If X not found print the same string.

Input Size : 1 <= |s|, |x| <= 1000
Sample Testcase :
INPUT
Happy Birthday
Happy

OUTPUT
Birthday
'''
S=input().split()
X=input()


if X in S:
    for i in range(0,len(S)-1):
        if S[i]==X:
            del S[i]
            for i in S:
                print(i,end="")
            break
else:
    for i in S:
        print(i, end=" ")








'''
for i in S:
    print(i)
'''

'''if Z is S:
    print(X)
'''