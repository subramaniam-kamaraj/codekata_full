'''
You are provided with a number ’n’. Your task is to tell whether
  that number is saturated. A saturated number is a number which is made
   by exactly two digits.

Input Description:
You are given with a number n.

Output Description:
Print Saturated if it is saturated else it is Unsaturated

Sample Input :
121

Sample Output :
Saturated
'''
n=input()
cmp=[]
'''for i in n:
    if len(n)==3:
        if n[0]==n[1] or n[0]==n[2] or n[1]==n[2] or n[2]==n[0]:
            cmp.append(i)
print(cmp)
'''

for i in n:
    if cmp.count(i)>=0 and cmp.count(i)<=1:
        if n[0]==n[1] or n[0]==n[2] or n[1]==n[2]:
            cmp.append(i)

k=''.join(cmp)
if n==k:
    print("Saturated")
else:
    print("Unsaturated")


