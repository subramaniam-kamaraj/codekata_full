'''

you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0

Input Description:
You are given a string ‘s’

Output Description:
Print 1 for balanced and 0 for imbalanced

Sample Input :
{({})}

Sample Output :
1


'''
open=['{',')']
close=['}',')']
s=input()
stack=[]

for i in s:
    if i in open:
        stack.append(i)
    elif i in close:
        position=close.index(i)
        if ( (len(stack) > 0) and (open[position]==stack[len(stack)-1]) ):
            stack.pop()
if len(stack)==0:
    print("balanced")
else:
    print("unbalanced")
