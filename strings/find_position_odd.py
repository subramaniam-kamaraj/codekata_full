'''Given a string S, print 2 strings one containing all characters in odd positions
 and other containing all characters in even positions.
Sample Testcase :
INPUT
XCODE
OUTPUT
XOE CD
'''

s=input()
w1=''
w2=''

for i in s:
    #print(i+' '+str(s.index(i)))
    if s.index(i)%2==0:
        w1=w1+i
    if s.index(i)%2!=0:
        w2=w2+i
print(w1,w2)