'''
Given a string 'S' and a character 'K',
    find at what position the character 'K' occurs
      for the first time in 'S'.(Assume the index of string starts at 1).
       If the character is not found in 'S' then print -1
Input Size : |s| <= 100000
Sample Testcase :
INPUT
codekata a
OUTPUT
6
'''

S,K=input().split()
for i in S:
    if i is K:
        print(S.index(i)+1)
        break
else:
    print("-1")

