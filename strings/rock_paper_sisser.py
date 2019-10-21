'''
Let P represent Paper, R represent Rock and S represent Scissors.
  Given 2 out of the 3 determine which wins(normal rules : p). If its a draw print D.
Sample Testcase :
INPUT
R P
OUTPUT
P
'''

a,k=input().split()
if (a is 'R' and k is'P') or(a is 'P' and k is'R'):
    print("P",end="")
elif (a is 'R' and k is 'S') or (a is 'S' and k is 'R'):
    print("R",end="")
elif (a is "P" and k is 'S') or (a is 'S' and k is "p"):
    print("S",end="")
elif (a is "R" and k is "R") or (a is "S" and k is "S") or (a is "P" and k is "P"):
    print("D",end="")