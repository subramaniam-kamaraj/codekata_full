'''
You are given a string ‘s’.Your task is to print the string in the order they are present and then sum of digits.

Input Description:
You are given a string ‘s’.

Output Description:
Print the string and then at last sum of all the digits

Sample Input :
AC30BD40

Sample Output :
ACBD7


'''
a=input()
coll=[]
final=''
for i in a:
    if i.isdigit()==True:
        coll.append(int(i))
s=sum(coll)

for i in a:
    if i.isalpha()==True:
        final=final+i
print(final+str(s))
