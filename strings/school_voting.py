'''
In a school there are voting to choose the monitor of class.
  Your task is to tell which candidate is winner and
   if there is a tie print the name of candidate whose come first in
      lexicographical order.

Input Description:
You are given with the space separated names.

Output Description:
Print the winner’s name and the votes he earned.

Sample Input :
john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john

Sample Output :
john 4

'''

name=input().split()
l1=[]
l2=[]
l3=[]
l4=[]
coun=0
for i in name:
    if i in final:
        final.append(i)
        coun=coun+1
    else:
        final.append(i)
